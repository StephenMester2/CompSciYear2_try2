import random


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class cardygame(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.suits = ["clubs", "hearts", "spades", "diamonds"]
        self.values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "king", "queen"]
        self.suits_num = random.randint(0, 3)
        print(self.suits_num)
        self.value_num = random.randint(0, 12)
        print(self.value_num)
        self.img_string = f"cards/{self.values[self.value_num]}_{self.suits[self.suits_num]}.jpeg"
        print(self.img_string)

        self.im = Image(source=self.img_string)
        self.window.add_widget(self.im)

        self.button_high = Button(
            text="Higher",
            size_hint=(1, 0.3),
            bold=True,
            background_color="#00FFCE")
        self.button_high.bind(on_press=self.high_test)

        self.button_low = Button(
            text="Lower",
            size_hint=(1, 0.3),
            bold=True,
            background_color="#00FFCE")

        self.button_next = Button(
            text="next",
            size_hint=(1, 0.3),
            bold=True,
            background_color="#00FFCE")

        self.window.add_widget(self.button_high)
        self.window.add_widget(self.button_next)
        self.window.add_widget(self.button_low)

        self.win_msg = Label(
                        text="WIN",
                        font_size = 38,
                        color = "#00FFCE")
        self.window.add_widget(self.win_msg)



        return self.window

    def high_test(self, event):
        current = self.value_num
        self.suits = ["clubs", "hearts", "spades", "diamonds"]
        self.values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "king", "queen"]

        self.suits_num = random.randint(0, 3)
        print(self.suits_num)
        self.value_num = random.randint(0, 12)
        print(self.value_num)

        self.img_string = f"cards/{self.values[self.value_num]}_{self.suits[self.suits_num]}.jpeg"
        print(self.img_string)

        self.window.remove_widget(self.im)
        self.im = Image(source=self.img_string)
        self.window.add_widget(self.im)

        if current < self.value_num:
            print("win")
            self.window.remove_widget(self.win_msg)
            self.window.add_widget(self.win_msg)
        else:
            print("lose")






cardygame().run()