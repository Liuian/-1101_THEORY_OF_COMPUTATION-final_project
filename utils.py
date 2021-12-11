import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage

channel_access_token = vTiKCE4ss+c7iVNJUoJuR2V/mKvqnR/Fa/3s8V+MOZiKebo6yF8+S47kpM3vLHsgZ7zMB7bas6rLwDNndQoJBqFu5vxEkk/cAm0QoMoflo2RjwI8588IdSX2Ex2Rn0Q/BWqIOCpm1Bc99I1hollieAdB04t89/1O/w1cDnyilFU=
#channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
