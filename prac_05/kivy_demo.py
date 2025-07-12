from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class SimpleApp(App):
    def build(self):
        self.title = "Kivy Demo"
        self.root = Builder.load_file('kivy_layout.kv')
        return self.root

    def greet(self):
        name = self.root.ids.name_input.text
        self.root.ids.output_label.text = f"Hello {name}!"


SimpleApp().run()
