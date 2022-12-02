import smtplib
import ssl
from email.message import EmailMessage
import sys

def abrir():
    with open('token') as arquivo:
        return arquivo.read()

class Email():
    def enviar(self,EmailMessage, email_receiver, subject, body):
        self.e_m = EmailMessage
        self.email_sender = 'brayanmesquita@gmail.com' 
        self.email_receiver = email_receiver
        self.subject = subject
        self.body = body
        self.e_m['From'] = self.email_sender
        self.e_m['To'] = self.email_receiver
        self.e_m['Subjecto'] = self.subject
        self.e_m.set_content(self.body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, password)
            smtp.sendmail(self.email_sender, self.email_receiver, self.e_m.as_string())
mail = Email()
mail.enviar(EmailMessage(),'patricianogueira@gmail.com', 'Teste de envio de email', 'qualquer envio')


#https://www.youtube.com/watch?v=TlvSJcoY19g&ab_channel=PythonScientist

# password = abrir()
# subject = 'Message for you'
# body = 'Example of text qualquer conteudo'

# email_receiver = 'patricianogueira@gmail.com'
# email_sender = 'brayanmesquita@gmail.com' 
# e_m = EmailMessage()
# e_m['From'] = email_sender
# e_m['To'] = email_receiver
# e_m['Subjecto'] = subject
# e_m.set_content(body)
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, password)
#     smtp.sendmail(email_sender, email_receiver, e_m.as_string())
# mail = Email(EmailMessage)
# mail.enviar(, 'subject', 'qualquer envio')

#___________________
#     #open comunication and send
#     server = smtplib.SMTP_SSL(server, port)
#     server.login(from_email, password)
#     server.send_message(msg)
#     server.quit()
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('email', type=str)
#     parser.add_argument('-c', dest='config', type=argparse.FileType('r'), default=None)

#     args = parser.parse_args()
#     if not args.config:
#         print('preencha corretamente')
#         exit(1)
#     config = configparser.ConfigParser()
#     config.read_file(args.config)

#     print(args.email)
        
#     main(args.email,
#         server=config['DEFAULT']['server'],
#         port=config['DEFAULT']['port'],
#         from_email=config['DEFAULT']['email'],
#         password=config['DEFAULT']['password'])