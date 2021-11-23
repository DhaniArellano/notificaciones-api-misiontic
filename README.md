# API Notificaciones
## MisionTic API python + twilio + sendgrid

please create a configuration file on the aplication folder called config.json 

`{
	"TWILIO_ACCOUNT_SID" : "AquiSid",
	"TWILIO_AUTH_TOKEN" : "AquiToken", 
	"TWILIO_PHONE_NUMBER" : "+NumeroTwilio",
	"SENDGRID_FROM_EMAIL" : "CorreoRegistradoTwilio",
	"SENDGRID_API_KEY" : "ApiKeyAqui"
}`

Requirements
- install twilio library
pip
`pip install twilio`
or if you are using conda 
`conda install -c conda-forge twilio`
- install sendgrid library
pip 
`pip install sendgrid`
or if you are using conda 
 `conda install -c conda-forge sendgrid`
 ## How it works
 this server runs on 127.0.0.1:5000
 ### localhost/sms
 request parameters 
 POST /sms 
 contenido
 destino 
 POST /email
 destino
 asunto
 contenido
 
 
 
 
 
 
 





