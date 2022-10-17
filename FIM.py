import smtplib,hashlib

filepath = input("Enter file path(eg. /home/desktop/important_files): ")

def send_mail():
    email = "your-email@gmail.com"
    password = "**********"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    message = "Alert! there has been a breach!! "
    server.sendmail(email, email, message)
    server.quit()

def hash_encode(filepath):
    sha256 = hashlib.sha256()
    with open(filepath,'rb') as file:
        hash = file.read()
        sha256.update(hash)
        return sha256.hexdigest()

baseline = hash_encode(filepath)
print("calculated the baseline")
print("script in progress.....")
while True:
    check = hash_encode(filepath)
    if check != baseline:
        send_mail()
        print("Alerted")
        baseline = check
