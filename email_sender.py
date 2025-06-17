import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com",port=597)
    server.starttls()

    ##receiver email
    receiver_mail = input("Enter the receiver email:")

    ##small credentials
    sender_email = "abhi09p8@gmail.com"
    password = "srmu hyrd mwdo vavg"

    ##login
    server.login(sender_email,password)


    subject = input("enter the subject:")
    body = input("enter the body:")
    message = f"subject :{subject} \n\n {body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("mail send")

    server.quit()
except Exception as e:
    print("An Error occured",e)