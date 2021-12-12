from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
# work
    def is_going_to_work(self, event):
        text = event.message.text
        return text.lower() == "1"

    def on_enter_work(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "輸入:\n'1'談判\n'2'會議、外出開會\n'3'簽約、面試")
        # self.go_back()
# work-1:negotitation
    def is_going_to_negotitation(self, event):
        text = event.message.text
        return text.lower() == "1"

    def on_enter_negotitation(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "暖色系 ex:黃色、橘色\n\n重新開始\n\n選擇場合 : \n'1' 職場\n'2' 約會")
        self.go_back()

    def on_exit_negotitation(self):
        print("Leaving state2")
# work-2:meeting
    def is_going_to_meeting(self, event):
        text = event.message.text
        return text.lower() == "2"

    def on_enter_meeting(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "冷色系 ex:藍色、綠色、紫色\n\n重新開始\n\n選擇場合 : \n'1' 職場\n'2' 約會")
        self.go_back()

    def on_exit_meeting(self):
        print("Leaving state2")
# work-3:interviewcontract
    def is_going_to_interviewcontract(self, event):
        text = event.message.text
        return text.lower() == "3"

    def on_enter_interviewcontract(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "無彩色 ex:黑色、灰色、白色\n\n重新開始\n\n選擇場合 : \n'1' 職場\n'2' 約會")
        self.go_back()
    
    def on_exit_interviewcontract(self):
        print("Leaving state2")
# dating
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
    '''
    #origional code
    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "state1"
    
    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
    '''