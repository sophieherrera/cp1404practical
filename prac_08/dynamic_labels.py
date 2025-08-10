from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # List of names
        self.names = ["Alice", "Bob", "Charlie", "Daisy"]

    def build(self):
        """Build the Kivy GUI."""
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name and add to GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

DynamicLabelsApp().run()
