import PyPDF2
import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle
import urllib.parse

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    """Get Gmail API service."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return build('gmail', 'v1', credentials=creds)

def extract_gmail_links_from_pdf(pdf_path):
    """Extract only Gmail attachment links from a PDF file."""
    try:
        links = []
        message_ids = set()  # To track unique message IDs
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                
                if '/Annots' in page:
                    annotations = page['/Annots']
                    for annotation in annotations:
                        annotation_object = annotation.get_object()
                        if annotation_object['/Subtype'] == '/Link':
                            if '/A' in annotation_object and '/URI' in annotation_object['/A']:
                                uri = annotation_object['/A']['/URI']
                                if 'mail.google.com' in uri and 'th=' in uri:
                                    # Extract message ID
                                    parsed_url = urllib.parse.urlparse(uri)
                                    query_params = urllib.parse.parse_qs(parsed_url.query)
                                    message_id = query_params.get('th', [None])[0]
                                    
                                    if message_id and message_id not in message_ids:
                                        message_ids.add(message_id)
                                        links.append(uri)
                                        print(f"Found message ID: {message_id}")
        
        return links

    except Exception as error:
        print(f"An error occurred while extracting links: {str(error)}")
        return []

def download_gmail_attachment(service, url, download_folder):
    """Download attachment from Gmail URL."""
    try:
        # Parse message ID and attachment ID from URL
        parsed_url = urllib.parse.urlparse(url)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        
        # Get the message ID from 'th' parameter
        message_id = query_params.get('th', [None])[0]
        
        if not message_id:
            print(f"Could not find message ID in URL: {url}")
            return
        
        print(f"\nProcessing message ID: {message_id}")
        
        # Get the message first
        message = service.users().messages().get(userId='me', id=message_id).execute()
        
        # Debug: Print message structure
        print("Message parts structure:")
        def print_parts_structure(parts, level=0):
            for part in parts:
                indent = "  " * level
                print(f"{indent}Part ID: {part.get('partId', 'None')}")
                print(f"{indent}Filename: {part.get('filename', 'None')}")
                print(f"{indent}MIME Type: {part.get('mimeType', 'None')}")
                if 'parts' in part:
                    print_parts_structure(part['parts'], level + 1)
        
        parts = message['payload'].get('parts', [])
        print_parts_structure(parts)
        
        # Try to find attachments
        def get_all_attachments(parts):
            attachments = []
            for part in parts:
                if part.get('filename') and 'body' in part and 'attachmentId' in part['body']:
                    attachments.append(part)
                if 'parts' in part:
                    attachments.extend(get_all_attachments(part['parts']))
            return attachments
        
        attachments = get_all_attachments(parts)
        
        if attachments:
            print(f"Found {len(attachments)} attachments in message")
            for part in attachments:
                try:
                    attachment = service.users().messages().attachments().get(
                        userId='me',
                        messageId=message_id,
                        id=part['body']['attachmentId']
                    ).execute()
                    
                    filename = part.get('filename')
                    if not filename:
                        filename = f"attachment_{message_id}_{part['body']['attachmentId']}"
                    
                    # Save the attachment
                    file_data = base64.urlsafe_b64decode(attachment['data'])
                    filepath = os.path.join(download_folder, filename)
                    with open(filepath, 'wb') as f:
                        f.write(file_data)
                    print(f"Successfully downloaded: {filename}")
                except Exception as e:
                    print(f"Error downloading attachment {filename}: {str(e)}")
        else:
            print("No attachments found in message")
        
    except Exception as e:
        print(f"Error processing message: {str(e)}")

def create_folder_structure(pdf_path):
    """Create folder structure and move PDF."""
    # Get the base folder name from PDF
    base_folder = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Create main folder with unique name
    folder_path = base_folder
    counter = 1
    while os.path.exists(folder_path):
        folder_path = f"{base_folder} ({counter})"
        counter += 1
    
    os.makedirs(folder_path)
    print(f"Created main folder: {folder_path}")
    
    # Create downloads subfolder
    downloads_folder = os.path.join(folder_path, 'downloads')
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)
        print(f"Created downloads folder: {downloads_folder}")
    
    # Move and rename PDF to 'message.pdf' in main folder
    new_pdf_path = os.path.join(folder_path, 'message.pdf')
    os.rename(pdf_path, new_pdf_path)
    print(f"Moved and renamed PDF to: {new_pdf_path}")
    
    return downloads_folder, new_pdf_path

if __name__ == '__main__':
    # Process all PDF files in the current directory
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        exit(1)

    for pdf_path in pdf_files:
        print(f"Processing PDF: {pdf_path}")
        
        # Create folder structure and move PDF
        download_folder, new_pdf_path = create_folder_structure(pdf_path)
        
        # Initialize Gmail service
        service = get_gmail_service()
        if not service:
            print("Failed to initialize Gmail service")
            exit(1)
        
        # Use new PDF path after moving
        gmail_links = extract_gmail_links_from_pdf(new_pdf_path)
        
        if gmail_links:
            print(f"\nFound {len(gmail_links)} Gmail attachments to download")
            for link in gmail_links:
                download_gmail_attachment(service, link, download_folder)
            print("\nDownload complete for:", pdf_path)
        else:
            print("No Gmail attachments found in the PDF:", pdf_path)
