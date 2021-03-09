import requests
from webScraping import  precioaActual 
from webScraping import  precioDeseado 

def telegram_bot_sendtext(bot_message):

    bot_token  = ''

    bot_chatID = ''

    enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(enviar_text)

    return response.json()


if precioaActual < precioDeseado:
    test = telegram_bot_sendtext(f" ¡ATENCION! Hay oferta, bajo el precio! Esta en:  {'$'+str(precioaActual)}\nEnlace: https://computacion.mercadolibre.com.ar/computacion/procesador")
else:
    test = telegram_bot_sendtext(f" ¡El precio sigue muy alto! Esta en:  {'$'+str(precioaActual)}")



