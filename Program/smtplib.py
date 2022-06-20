
import smtplib

def automaticemail():
    user_name = input("Enter your name: ")
    Email_id = input("Your email id: ")
    Email_content = f"Hai {user_name}, Welcome to Gmail"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your Gmail Account", "Your App Password")
    s.sendemail('&&&&&&&&&&&', Email_id, Email_content)
    print("email sent")

automaticemail()
