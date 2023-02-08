from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play=True
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera.opacity = 1

    def stop(self):
        self.ids.camera.play=False
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0


    def capture(self):
        current_time = time.strftime("%Y%m%d-%H%M%S")
        filename = f"files/{current_time}.png"
        self.ids.camera.export_to_png(filename)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filename



class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()


# Running the App
MainApp().run()