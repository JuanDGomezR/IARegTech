from flask_mail import Message
from extensions import mail

def enviar_notificacion(destinatario, asunto, cuerpo, adjunto_path=None):
    msg = Message(asunto, recipients=[destinatario])
    msg.body = cuerpo
    if adjunto_path:
        with open(adjunto_path, 'rb') as f:
            msg.attach(adjunto_path.split('/')[-1], "application/pdf", f.read())
    mail.send(msg)
