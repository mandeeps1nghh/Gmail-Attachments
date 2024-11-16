

# Email Attachment Organizer 🚀

This Python project automates the process of organizing emails and attachments. The script extracts Gmail attachment links from PDFs, downloads the attachments via the Gmail API, and organizes them into structured folders. It’s designed to handle large volumes of emails efficiently, saving countless hours of manual effort.

## Key Features 🛠️
- **Bulk Processing**: Handles hundreds of emails in one go.
- **Attachment Extraction**: Identifies Gmail attachment links embedded in PDFs.
- **Automated Download**: Downloads attachments directly using the Gmail API.
- **Organized Folders**: Creates folders named after email subjects, storing the email as a PDF and attachments in a dedicated subfolder.

## Workflow 📂
1. **Input**: PDFs containing email data and embedded attachment links.  
2. **Processing**:  
   - Extract attachment links from PDFs.  
   - Authenticate with Gmail API.  
   - Download attachments.  
   - Organize folders and rename files.  
3. **Output**: Structured folders with organized emails and attachments.

## Folder Structure 📁
After running the script, the directory will look like this:

```
email-attachment-organizer/
│
├── Email_Subject_1/
│   ├── message.pdf
│   └── downloads/
│       ├── attachment1.jpg
│       ├── attachment2.pdf
│
├── Email_Subject_2/
│   ├── message.pdf
│   └── downloads/
│       ├── attachment1.docx
│       ├── attachment2.png
```

## Installation & Setup 🖥️
### Prerequisites
- **Python 3.7+**
- **Gmail API credentials**: Set up in [Google Cloud Console](https://console.cloud.google.com/).
- Required Python libraries:
  - `PyPDF2`
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-auth-httplib2`
  - `google-api-python-client`

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/email-attachment-organizer.git
   cd email-attachment-organizer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Enable Gmail API and download the `credentials.json` file.
4. Place `credentials.json` in the project directory.

## Usage 🚀
1. Place your email PDFs in the project directory.
2. Run the script:
   ```bash
   python email_attachment_organizer.py
   ```
3. Authenticate with your Gmail account when prompted.
4. The script processes the PDFs and organizes emails and attachments into folders.

## Example Output 🎉
Once processed, all emails and their attachments will be organized neatly into folders.

## Technical Highlights 🔧
- **Gmail API Integration**: Used for accessing and downloading attachments.
- **PDF Parsing**: Leveraged PyPDF2 to extract embedded Gmail links.
- **Folder Automation**: Dynamically creates folders and subfolders based on email content.

## Contribution 🤝
Feel free to fork this repository, report issues, or suggest improvements. Contributions are always welcome!

## Connect 🌐
If you find this project interesting or have questions, feel free to connect on [LinkedIn](https://www.linkedin.com/in/mandeeps1nghh).
