# WhatsApp Message Sender
A Python script that allows users to send WhatsApp messages to multiple contacts without needing to save the contacts on their phone. This script uses the pywhatkit library to facilitate message sending and can also handle PDF attachments for each contact.

# Features
Send unlimited WhatsApp messages to multiple contacts.
Attach PDF files to messages.
Works without saving phone numbers in contacts.

# Disclaimer
This script is for educational purposes only. Please use responsibly and avoid spamming or violating WhatsApp’s terms of service.

Prerequisites
Python 3.6+
pywhatkit library

# Prerequisites
Python 3.6+
pywhatkit library
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/NeduStack/whatsapp-message-sender.git
cd whatsapp-message-sender
Install Dependencies:

bash
Copy code
pip install pywhatkit
Run the Script: Update the script with your list of contacts and message, then run:

bash
Copy code
python whatsapp_sender.py

# Usage
Prepare Contacts: Prepare contact in the formats used in the example.
Modify Script: Update the script with the PDF file path and the contact list.
Run Script: The script will open WhatsApp Web and send the messages automatically.
Example
python
Copy code
# Example usage in whatsapp_sender.py
contacts = ["+1234567890", "+0987654321"]
message = "Hello from WhatsApp Message Sender!"
pywhatkit.sendwhatmsg_instantly(contacts[0], message)

# License
This project is licensed under the MIT License.

This README should help users understand and set up your project easily! Let me know if you'd like any additions.
