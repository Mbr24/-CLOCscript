import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# run the cloc command 
command = "cloc C:\\test_generate.py"
subprocess.run(command, shell=True)
result = subprocess.check_output(command, shell=True, text=True)

# send email
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("insert_email", "insert_pass")
s.sendmail("insert_sent_from", "insert_sent_to", result)
s.quit()

print("CLOC report sent successfully.")
