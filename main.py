from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        # Get user input
        query = self.manager.current_screen.ids.user_query.text
        # Get wiki page
        page = wikipedia.page(query)
        image_link = page.images[0]
        # Download image
        req = requests.get(image_link)
        image_path = 'images/image.jpg'

        with open(image_path, 'wb') as file:
            file.write(req.content)

        self.manager.current_screen.ids.img.source = image_path


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
