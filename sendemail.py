import smtplib


# Get a gmail in https://accounts.google.com/ 
MY_EMAIL = ""
PASSWORD = ""

def sendEmail(name, email, message, subject):
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                # Get a second gmail in https://accounts.google.com/
                to_addrs="", 
                msg=f"Subject:New email from the Weather Tek\n\n{subject}\nFullname: {name}\nEmail: {email}\nMessage: {message}"
            )
