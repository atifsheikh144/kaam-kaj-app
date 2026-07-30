from kivy.app import App
from kivy.uix.label import Label

class KaamKajApp(App):
    def build(self):
        return Label(text="Hello, yeh meri pehli app hai!")

if __name__ == '__main__':
    KaamKajApp().run()
