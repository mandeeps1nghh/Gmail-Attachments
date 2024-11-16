# Email Attachment Organizer 🚀

A Python project that automates the tedious process of organizing emails and attachments. This script scans PDFs containing embedded Gmail attachment links, downloads the attachments via the Gmail API, and organizes them into structured folders. Perfect for handling large volumes of email attachments efficiently!

## Features 🛠️
- Extracts embedded Gmail attachment links from PDF files.
- Downloads attachments automatically using the Gmail API.
- Organizes emails into folders named after their subject.
- Saves the full email content as a `message.pdf` file.
- Creates subfolders named `downloads` to store attachments.

## Project Workflow 📂
1. **Bulk Download Emails**: Export your emails into PDF format.
2. **Run the Script**:
   - Extract links from PDFs.
   - Authenticate with Gmail API.
   - Download attachments and sort them into folders.
3. **Automated Organization**: Each email is stored in a unique folder with attachments neatly organized.

## Folder Structure 📁
- **Main Folder**: Named after the email subject.
- **Subfolder (`downloads`)**: Contains all attachments from the email.
- **PDF File**: Full email content saved as `message.pdf`.

## Installation & Setup 🖥️
### Prerequisites
- Python 3.7+
- Gmail API credentials
- Required Python libraries:
  - `PyPDF2`
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-auth-httplib2`
  - `google-api-python-client`

### Steps to Set Up:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/email-attachment-organizer.git
   cd email-attachment-organizer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Enable Gmail API and download the `credentials.json` file from the [Google Cloud Console](https://console.cloud.google.com/).
4. Place `credentials.json` in the project directory.

## Usage 🚀
1. Place your email PDFs in the project directory.
2. Run the script:
   ```bash
   python email_attachment_organizer.py
   ```
3. Authenticate with your Gmail account when prompted.
4. Watch the magic! Folders will be created and attachments downloaded.

## Example Output 🎉
After running the script, your directory will look like this:

```
email-attachment-organizer/
│
├── Example Email 1/
│   ├── message.pdf
│   └── downloads/
│       ├── attachment1.jpg
│       └── attachment2.pdf
│
├── Example Email 2/
│   ├── message.pdf
│   └── downloads/
│       ├── attachment1.docx
│       └── attachment2.png
```

## Contribution 🤝
Feel free to submit pull requests, report bugs, or suggest features. Contributions are always welcome!

## Connect 🌐
If you find this project helpful or have questions, feel free to reach out or connect on [LinkedIn](https://www.linkedin.com/in/mandeeps1nghh).

