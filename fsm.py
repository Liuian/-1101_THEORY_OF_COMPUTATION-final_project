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
        '''print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "選擇顏色:\n'1'紅色\n'2'藍色\n'3'綠色\n'4'黃色\n'5'紫色\n'6'白色\n'7'黑色")
        # self.go_back()'''
        title = '選擇顏色'
        text = '選擇你想了解的顏色穿搭心理學'
        btn = [
            MessageTemplateAction(
                label = '紅色',
                text ='1'
            ),
            MessageTemplateAction(
                label = '藍色',
                text = '2'
            ),
            MessageTemplateAction(
                label = '綠色',
                text = '3'
            ),
            MessageTemplateAction(
                label = '黃色',
                text = '4'
            ),
            MessageTemplateAction(
                label = '紫色',
                text = '5'
            ),
            MessageTemplateAction(
                label = '白色',
                text = '6'
            ),
            MessageTemplateAction(
                label = '黑色',
                text = '7'
            ),
        ]
        #url = ''
        send_button_message2(event.reply_token, title, text, btn)

        self.go_back()
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
        text = '愛穿紅色的人，具有冒險精神、勇於接受挑戰、擁有開闊的心胸接納新鮮事物，也擅長處理人際關係。'
        btn = [
            MessageTemplateAction(
                label = '特定場合穿搭顏色建議',
                text ='1'
            ),
            MessageTemplateAction(
                label = '穿搭顏色心理學',
                text = '2'
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
        '''print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "blue\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()'''
        title = '藍色-穿搭顏色心理學'
        text = '喜歡穿藍色的人往往理智且冷靜，容易接納並包容周邊的人事物。'
        btn = [
            MessageTemplateAction(
                label = '特定場合穿搭顏色建議',
                text ='1'
            ),
            MessageTemplateAction(
                label = '穿搭顏色心理學',
                text = '2'
            ),
        ]
        url = 'https://i.imgur.com/aJMwFQp.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

        self.go_back()

    def on_exit_blue(self):
        print("Leaving state2")
# psychology->green
    def is_going_to_green(self, event):
        text = event.message.text
        return text.lower() == "3"

    def on_enter_green(self, event):
        '''print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "green\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()'''
        title = '綠色-穿搭顏色心理學'
        text = '喜歡綠色的人通常處於穩定的生活環境裡，會主動關心並照顧朋友，態度積極、社交能力強。'
        btn = [
            MessageTemplateAction(
                label = '特定場合穿搭顏色建議',
                text ='1'
            ),
            MessageTemplateAction(
                label = '穿搭顏色心理學',
                text = '2'
            ),
        ]
        url = 'https://i.imgur.com/slTmgrM.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

        self.go_back()

    def on_exit_green(self):
        print("Leaving state2")
# psychology->yellow
    def is_going_to_yellow(self, event):
        text = event.message.text
        return text.lower() == "4"

    def on_enter_yellow(self, event):
        '''print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "yellow\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()'''
        title = '黃色-穿搭顏色心理學'
        text = '黃色給人活潑開朗的印象，就像小小兵一般擁有天真爛漫的內心，對生活富有熱情、擁有非凡的創意。'
        btn = [
            MessageTemplateAction(
                label = '特定場合穿搭顏色建議',
                text ='1'
            ),
            MessageTemplateAction(
                label = '穿搭顏色心理學',
                text = '2'
            ),
        ]
        url = 'https://i.imgur.com/wyeqLQ1.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

        self.go_back()

    def on_exit_yellow(self):
        print("Leaving state2")
# psychology->purple
    def is_going_to_purple(self, event):
        text = event.message.text
        return text.lower() == "5"

    def on_enter_purple(self, event):
        '''print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "purple\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()'''
        title = '紫色-穿搭顏色心理學'
        text = '喜歡紫色的人通常喜歡幻想、情感豐沛且浪漫，對生活充滿激情，在藝術方面很有天分。'
        btn = [
            MessageTemplateAction(
                label = '特定場合穿搭顏色建議',
                text ='1'
            ),
            MessageTemplateAction(
                label = '穿搭顏色心理學',
                text = '2'
            ),
        ]
        url = 'https://i.imgur.com/KxKObmx.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

        self.go_back()

    def on_exit_purple(self):
        print("Leaving state2")
# psychology->wite
    def is_going_to_white(self, event):
        text = event.message.text
        return text.lower() == "6"

    def on_enter_white(self, event):
        '''print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "wite\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()'''
        title = '白色-穿搭顏色心理學'
        text = '喜歡穿白色衣服的人是典型的完美主義者，個性樂觀、追求完美與平衡，有時候無法容忍他人缺陷。'
        btn = [
            MessageTemplateAction(
                label = '特定場合穿搭顏色建議',
                text ='1'
            ),
            MessageTemplateAction(
                label = '穿搭顏色心理學',
                text = '2'
            ),
        ]
        url = 'https://i.imgur.com/COhp0Fl.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

        self.go_back()

    def on_exit_white(self):
        print("Leaving state2")
# psychology->black
    def is_going_to_black(self, event):
        text = event.message.text
        return text.lower() == "7"

    def on_enter_black(self, event):
        '''print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "black\n（重新開始）\n'1' 特定場合顏色穿搭'2' 穿搭顏色心理學")
        self.go_back()'''
        title = '黑色-穿搭顏色心理學'
        text = '喜歡黑色的人較不善於表達情感，他們通常壓抑且不太吐露自己的感受，但也渴望被關注、被愛。'
        btn = [
            MessageTemplateAction(
                label = '特定場合穿搭顏色建議',
                text ='1'
            ),
            MessageTemplateAction(
                label = '穿搭顏色心理學',
                text = '2'
            ),
        ]
        url = 'https://i.imgur.com/xTuMynx.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

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