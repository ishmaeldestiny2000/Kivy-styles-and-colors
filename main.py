from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class DroneApp(MDApp):
    def build(self):
        label = MDLabel(
            text="Hello world!",
            halign="center",
            theme_text_color = "Custom",
            text_color = (128/255, 108/255 ,238/255 , 1)
        )
        return label



if __name__ == "__main__":
    DroneApp().run()
        


