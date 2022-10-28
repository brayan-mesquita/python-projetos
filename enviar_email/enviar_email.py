import argparse
import configparser
import smtplib
from email.message import EmailMessage

def main(to_mail, server, port, from_email, password):

    subject = 'Message for you'
    text = 'Example of text'
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subjecto'] = subject
    msg['From'] = from_email
    msg['To'] = 'patricianogueiranm@gmail.com'

    #open comunication and send
    server = smtplib.SMTP_SSL(server, port)
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email', type=str)
    parser.add_argument('-c', dest='config', type=argparse.FileType('r'), default=None)

    args = parser.parse_args()
    if not args.config:
        print('preencha corretamente')
        exit(1)
    config = configparser.ConfigParser()
    config.read_file(args.config)

    print(args.email)
        
    main(args.email,
        server=config['DEFAULT']['server'],
        port=config['DEFAULT']['port'],
        from_email=config['DEFAULT']['email'],
        password=config['DEFAULT']['password'])