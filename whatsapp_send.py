import pywhatkit
import time
from datetime import datetime
import os
import webbrowser
from urllib.parse import quote
import pyautogui
import subprocess

def send_whatsapp_bulk(phone_numbers, message, pdf_path=None, delay_between_messages=5):
    """
    Send WhatsApp messages and PDFs to multiple numbers.
    
    Args:
        phone_numbers (list): List of phone numbers with country code (e.g., '+2348135827111')
        message (str): Message to send
        pdf_path (str, optional): Path to PDF file to send
        delay_between_messages (int): Delay in seconds between messages (default: 5)
    """
    # Check if PDF exists and convert path format
    if pdf_path:
        pdf_path = os.path.normpath(pdf_path)
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found at {pdf_path}")
        print(f"PDF file found at: {pdf_path}")
    
    successful = []
    failed = []
    
    print("Starting bulk send process...")
    print("Please ensure WhatsApp Web is connected")
    
    for phone in phone_numbers:
        try:
            # Clean the phone number
            clean_phone = ''.join(filter(str.isdigit, phone))
            if clean_phone.startswith('+'):
                clean_phone = clean_phone[1:]
            
            # Open WhatsApp Web for this contact
            web_url = f"https://web.whatsapp.com/send?phone={clean_phone}"
            webbrowser.open(web_url)
            
            # Wait for WhatsApp Web to load
            time.sleep(15)  # Increased wait time for loading
            
            # Send text message
            pyautogui.write(message)
            pyautogui.press('enter')
            time.sleep(2)
            
            if pdf_path:
                # Click attachment button (paperclip icon)
                # These coordinates might need adjustment based on your screen resolution
                pyautogui.click(x=700, y=700)  # Adjust these coordinates
                time.sleep(1)
                
                # Click document option
                pyautogui.click(x=700, y=600)  # Adjust these coordinates
                time.sleep(1)
                
                # Type the PDF path and press enter
                pyautogui.write(pdf_path)
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(2)
                
                # Press enter to send the file
                pyautogui.press('enter')
                time.sleep(5)
            
            successful.append(phone)
            print(f"Sent successfully to {phone}")
            
            # Close the current tab
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(delay_between_messages)
            
        except Exception as e:
            failed.append((phone, str(e)))
            print(f"Failed to send to {phone}: {str(e)}")
            continue
    
    return {
        "successful": successful,
        "failed": failed
    }

# Example usage
if __name__ == "__main__":
    # List of Nigerian phone numbers
    numbers = [
        "+2348101001154",
        "+2348021111698",
        "+2348131000000",
        "+2348090909011"
    ]
    
    message = "https://drive.google.com/file/d/1YjyVpwVEWv1APqei8KhgJzh5yYH0uYiY/view?usp=drive_link"
    pdf_path = ""
    
    # Important instructions for the user
    print("IMPORTANT INSTRUCTIONS:")
    print("1. Make sure WhatsApp Web is already open and logged in")
    print("2. Do not move your mouse or use your keyboard while the script is running")
    print("3. Keep the WhatsApp Web window maximized")
    print("4. Wait for 5 seconds after running the script before it starts")
    print("\nStarting in 5 seconds...")
    time.sleep(5)
    
    # Send message and PDF
    results = send_whatsapp_bulk(numbers, message, pdf_path=pdf_path, delay_between_messages=5)
    
    print("\nFinal Results:")
    print(f"Successfully sent to {len(results['successful'])} numbers")
    print(f"Failed to send to {len(results['failed'])} numbers")
    
    if results['failed']:
        print("\nFailed deliveries:")
        for number, error in results['failed']:
            print(f"{number}: {error}")