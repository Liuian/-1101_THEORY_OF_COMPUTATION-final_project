from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_message, send_button_message
from linebot.models import MessageTemplateAction

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
# user->occasion
    def is_going_to_occasion(self, event):
        text = event.message.text
        return text.lower() == "1"

    def on_enter_occasion(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "選擇活動:\n'1'職場\n'2'約會")
        # self.go_back()
# user->psychology
    def is_going_to_psychology(self, event):
        text = event.message.text
        return text.lower() == "2"

    def on_enter_psychology(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "選擇顏色:\n'1'紅色\n'2'藍色\n'3'綠色\n'4'黃色\n'5'紫色\n'6'白色\n'7'黑色")
        # self.go_back()
# psychology->red
    def is_going_to_red(self, event):
        text = event.message.text
        return text.lower() == "1"

    def on_enter_red(self, event):
        #------send text message
        # print("I'm entering state1")
        # reply_token = event.reply_token
        # send_text_message(reply_token, "red\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        #------send image message
        # url = 'https://i.imgur.com/NpPRXx3.png'
        # send_image_message(event.reply_token, url)
        
        title = '紅色-穿搭顏色心理學'
        text = 'RED describtion'
        btn = [
            MessageTemplateAction(
                label = '1',
                text ='特定場合穿搭顏色建議'
            ),
            MessageTemplateAction(
                label = '2',
                text = '穿搭顏色心理學'
            ),
        ]
        url = 'https://i.imgur.com/m2J2jdJ.png?1'
        send_button_message(event.reply_token, title, text, btn, url)

        self.go_back()

    def on_exit_red(self):
        print("Leaving state2")
# psychology->blue
    def is_going_to_blue(self, event):
        text = event.message.text
        return text.lower() == "2"

    def on_enter_blue(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "blue\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()

    def on_exit_blue(self):
        print("Leaving state2")
# psychology->green
    def is_going_to_green(self, event):
        text = event.message.text
        return text.lower() == "3"

    def on_enter_green(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "green\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()

    def on_exit_green(self):
        print("Leaving state2")
# psychology->yellow
    def is_going_to_yellow(self, event):
        text = event.message.text
        return text.lower() == "4"

    def on_enter_yellow(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "yellow\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()

    def on_exit_yellow(self):
        print("Leaving state2")
# psychology->purple
    def is_going_to_purple(self, event):
        text = event.message.text
        return text.lower() == "5"

    def on_enter_purple(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "purple\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()

    def on_exit_purple(self):
        print("Leaving state2")
# psychology->wite
    def is_going_to_wite(self, event):
        text = event.message.text
        return text.lower() == "6"

    def on_enter_wite(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "wite\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()

    def on_exit_wite(self):
        print("Leaving state2")
# psychology->black
    def is_going_to_black(self, event):
        text = event.message.text
        return text.lower() == "7"

    def on_enter_black(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "black\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()

    def on_exit_black(self):
        print("Leaving state2")
# occasion->work
    def is_going_to_work(self, event):
        text = event.message.text
        return text.lower() == "1"

    def on_enter_work(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "選擇活動:\n'1'談判\n'2'會議、外出開會\n'3'簽約、面試")
        # self.go_back()
# occasion->dating
    def is_going_to_dating(self, event):
        text = event.message.text
        return text.lower() == "2"

    def on_enter_dating(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "重新開始\n\n選擇場合 : \n'1' 職場\n'2' 約會")
        self.go_back()

    def on_exit_dating(self):
        print("Leaving state2")
# work->negotitation(work-1):
    def is_going_to_negotitation(self, event):
        text = event.message.text
        return text.lower() == "1"

    def on_enter_negotitation(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "暖色系 ex:黃色、橘色\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()

    def on_exit_negotitation(self):
        print("Leaving state2")
# work->meeting(work-2)
    def is_going_to_meeting(self, event):
        text = event.message.text
        return text.lower() == "2"

    def on_enter_meeting(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "冷色系 ex:藍色、綠色、紫色\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()

    def on_exit_meeting(self):
        print("Leaving state2")
# work->interviewcontract(work-3)
    def is_going_to_interviewcontract(self, event):
        text = event.message.text
        return text.lower() == "3"

    def on_enter_interviewcontract(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "無彩色 ex:黑色、灰色、白色\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()
    
    def on_exit_interviewcontract(self):
        print("Leaving state2")