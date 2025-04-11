import schedule
import time
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import os

def job():
    print("I'm working...")
    # Load environment variables from .env file
    load_dotenv()

    # Define email sender and receiver
    email_sender = os.getenv('EMAIL_SENDER')
    email_password = os.getenv('EMAIL_PASSWORD')
    # alternate syntax by declaring global variable with python os module --> email_password = os.environ.get("EMAIL_PASSWORD")                  
    email_receiver = os.getenv('EMAIL_RECEIVER')       

    # Set the subject and body of the email
    subject = '2nd automatic email'
    body = """
    email automation working fine!!
    2nd automatic email success
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

# Schedule the job to run at 14:30 every day
#schedule.every().day.at("14:30").do(job)

# Schedule the email to be sent every 20 seconds
schedule.every(5).seconds.do(job)
print("Email scheduler started. Sending emails every 20 seconds...")

while True:
    schedule.run_pending()
    time.sleep(15)   # checks every 30 seconds
