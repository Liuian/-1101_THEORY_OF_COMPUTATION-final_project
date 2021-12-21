import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate

channel_access_token = 'vTiKCE4ss+c7iVNJUoJuR2V/mKvqnR/Fa/3s8V+MOZiKebo6yF8+S47kpM3vLHsgZ7zMB7bas6rLwDNndQoJBqFu5vxEkk/cAm0QoMoflo2RjwI8588IdSX2Ex2Rn0Q/BWqIOCpm1Bc99I1hollieAdB04t89/1O/w1cDnyilFU='
#channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_message(reply_token, url):
    #pass
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url = url,
        preview_image_url = url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_button_message(reply_token, title, text, btn, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='button template',
        template = ButtonsTemplate(
            title = title,
            text = text,
            thumbnail_image_url = url,
            actions = btn
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

"""
def send_button_message(id, text, buttons):
    pass
"""
