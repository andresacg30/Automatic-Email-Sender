# Automatic-Email-Sender
This is a program made to fulfill specific needs of a school sending grade reports.

The school have grade reports for every student as PDF files with the student's name as the file's name, and a CSV file with each student and parent's email.
The program will search trough each PDF file in a temporary folder for the program's purpose, link the file's name with the student's name in the CSV file,
take the email corresponding to that student, and send the PDF as an attatchment with a message previously given. If the program succes on sending the email,
it will erase the PDF file from the temporary folder, otherwise will print the name of the student and the possible error. At the end, it will be only the PDFs
in the folder which failed to send for further investigation.
