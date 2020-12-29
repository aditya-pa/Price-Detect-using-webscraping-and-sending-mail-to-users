    import smtplib
    def send(price):
        sender_email = "developmentadityahere@gmail.com"
        rec_email = "zaosut@gmail.com"
        password = "99971725082734781160"
    ##    message = f"""\
    ##    Subject: Hi there
    ##
    ##    This message is sent from Python{str(price)}."""
    ##
        m=f"The price of  MI NoteBook is {str(price)}.\n Buy now! HURRY!!!"  
        message = f'Subject: {"Price REDUCTION ALERT!!!"}\n\n{m}'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login success")
        server.sendmail(sender_email, rec_email, message)
        print("Email has been sent to ", rec_email)





