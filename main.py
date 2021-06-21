from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def get_image_link(self):
        # Get user input
        query = self.manager.current_screen.ids.user_query.text
        # Get wiki page
        page = wikipedia.page(query)
        image_link = page.images[0]

        return image_link

    def down_load_image(self):
        # Download image
        req = requests.get(self.get_image_link())
        image_path = 'images/image.jpg'
        with open(image_path, 'wb') as file:
            file.write(req.content)
        return image_path

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.down_load_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
