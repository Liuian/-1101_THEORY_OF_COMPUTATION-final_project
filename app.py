import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

'''
# origional code
machine = TocMachine(
    states=["user", "state1", "state2"],    # 總共有的states
    transitions=[
        {
            "trigger": "advance",   # ???
            "source": "user",   # 現在的state
            "dest": "state1",   # 會去到哪個state
            "conditions": "is_going_to_state1", # ???
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
        {"trigger": "go_back", "source": ["state1", "state2"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)
'''
machine = TocMachine(
    states=[
        "user",
        "work",
        "dating",
        "negotitation",
        "meeting",
        "interviewcontract",
        "occasion"

    ],    # 總共有的states
    transitions=[
        {   # user->occasion
            "trigger": "advance",   # ???
            "source": "user",   # 現在的state
            "dest": "occasion",   # 會去到哪個state
            "conditions": "is_going_to_occasion", # ???
        },
        {   # occasion->work
            "trigger": "advance",   # ???
            "source": "occasion",   # 現在的state
            "dest": "work",   # 會去到哪個state
            "conditions": "is_going_to_work", # ???
        },
        {   # occasion->dating
            "trigger": "advance",
            "source": "occasion",
            "dest": "dating",
            "conditions": "is_going_to_dating",
        },
        {   # work->negotitation
            "trigger": "advance",
            "source": "work",
            "dest": "negotitation",
            "conditions": "is_going_to_negotitation",
        },
        {   # work->meeting
            "trigger": "advance",
            "source": "work",
            "dest": "meeting",
            "conditions": "is_going_to_meeting",
        },
        {   # work->interviewcontract
            "trigger": "advance",
            "source": "work",
            "dest": "interviewcontract",
            "conditions": "is_going_to_interviewcontract",
        },
        {       #go_back
            "trigger": "go_back", 
            "source": [
                "dating",
                "negotitation",
                "meeting",
                "interviewcontract"
            ], 
            "dest": "user"
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = 'c61e38da1d1c0595e925dc13b7495018'
channel_access_token = 'vTiKCE4ss+c7iVNJUoJuR2V/mKvqnR/Fa/3s8V+MOZiKebo6yF8+S47kpM3vLHsgZ7zMB7bas6rLwDNndQoJBqFu5vxEkk/cAm0QoMoflo2RjwI8588IdSX2Ex2Rn0Q/BWqIOCpm1Bc99I1hollieAdB04t89/1O/w1cDnyilFU='
#channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
#channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


# 接收line的資訊：誰傳了怎麼樣的信息給我們的聊天機器人->所以要用POST
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    '''
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"
    '''
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            # origional code
            send_text_message(event.reply_token, "選項 : \n'1' 特定場合穿搭\n'2' 穿搭顏色心理學")

    return "OK"
    
'''
@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"
'''

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    # port = "8000"
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
