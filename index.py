from flask import Flask, request
import json
from twilio.rest import Client
import sendgrid
import os
from sendgrid.helpers.mail import *

app = Flask(__name__)
"""
el programa necesita un archivo llamado config.json junto al script 
con el siguiente formato
{
	"TWILIO_ACCOUNT_SID" : "AquiSid",
	"TWILIO_AUTH_TOKEN" : "AquiToken", 
	"TWILIO_PHONE_NUMBER" : "+NumeroTwilio",
	"SENDGRID_FROM_EMAIL" : "CorreoRegistradoTwilio",
	"SENDGRID_API_KEY" : "ApiKeyAqui"
}    
"""
f = open("config.json", "r")
env = json.loads(f.read())

@app.route('/test', methods=['GET'])
def test():
    return "hello world"

@app.route('/sms', methods=['POST'])
def sms():
    try:
        account_sid = env['TWILIO_ACCOUNT_SID']
        auth_token = env['TWILIO_AUTH_TOKEN']
        origen = env['TWILIO_PHONE_NUMBER']
        client = Client(account_sid, auth_token)
        contenido = request.args.get("contenido")
        destino = request.args.get("destino")
        message = client.messages.create(
                            body=contenido,
                            from_=origen,
                            to='+57' + destino
                        )
        print(message)
        return "[SMS] envio exitoso"
    except Exception as e:
        print(e)
        return "[SMS] error al enviar"

@app.route('/email', methods=['POST'])
def email():
    data = request.json
    destino = request.args.get("destino")
    asunto = request.args.get("asunto")
    contenido = request.args.get("contenido")
    try:
        sg = sendgrid.SendGridAPIClient(env['SENDGRID_API_KEY'])
        from_email = Email(env['SENDGRID_FROM_EMAIL'])
        to_email = To(destino)
        subject = asunto
        content = Content("text/plain", contenido)
        mail = Mail(from_email, to_email, subject, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        return "email enviado exitosamente"
    except Exception as e:
        print(e)
        return "error al enviar email"

if __name__ == '__main__':
    app.run()