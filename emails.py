import smtplib
import os
import pandas as pd
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_email():
    folder = os.fsdecode("Enviar")
    emails = pd.read_csv("emails.csv")

    for file in os.listdir(folder):
        student = os.path.basename(file).replace(".","").split("pdf")[0].lstrip().rstrip()  # First character of series as String, erasing possible whitespaces and removing dot for 1st and 2nd grade files

        # Credentials
        email_address = "notificaciones@sns.edu.do"
        email_password = "SNS#391997"
        try:
            recipient_email = (emails["Correo electrónico"][emails["Nombre y apellido del estudiante"] == student]).values[0].lstrip().rstrip()  # Email matched with student name, erasing possible whitespaces
        except:
            print(f"No hay correo para {student}. Verificar que el nombre del estudiante corresponda con su correo en el archivo emails. Leer README para mas informacion.")
            continue
        host_address = "smtp.office365.com"
        host_port = 587

        # Connection with server
        server = smtplib.SMTP(host=host_address, port=host_port)
        server.starttls()
        server.login(email_address, email_password)

        # MIMEMultipart Object
        message = MIMEMultipart()

        # Setup for MIMEMultipart Object Header
        message['From'] = email_address
        message["To"] = recipient_email
        message["Subject"] = "Reporte de calificaciones"

        # Creation of MIMEText part
        textpart = MIMEText(f"""Representante de {student}, 
        Este es un correo automatizado, en caso de algún reclamo, por favor contactase directamente con las oficinas.""")
        filename = f"{os.getcwd()}\\Enviar\\{os.path.basename(file)}"
        filepart = MIMEApplication(open(filename, "rb").read(), Name=filename)
        filepart['Content-Disposition'] = 'attatchment; filename="%s.pdf' % student

        # Attatchment
        message.attach(textpart)
        message.attach(filepart)

        # Send and close
        try:
            server.send_message(message)
            os.remove(f"{folder}\\{file}")
        except:
            print(f"Correo incorrecto para {student}.")
        server.quit()
    print("Los reportes fueron enviados!")
    

send_email()
input("Presione enter para salir")