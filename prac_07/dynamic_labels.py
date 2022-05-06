from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamiclabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_lables = ["Bob Brown", "Cat Cyan", "Oren Ochre"]
    
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.creat_labels()
        return self.root

    def creat_labels(self):
        for name in self.name_lables:    
            temp_label = Label(text = name)
            self.root.ids.main.add_widget(temp_label)

DynamiclabelsApp().run()