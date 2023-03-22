from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def search_image(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        # Use any browser you want
        headers = {'User-agent': 'Mozilla/5.0'}
        # Get wiki page and list from image url
        page = wikipedia.page(query, auto_suggest=False)
        image_link = page.images[0]
        print(image_link)
        # Download the image
        req = requests.get(image_link, headers=headers)
        imagepath = 'files/images.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        # Set the image in the Image widget
        self.manager.current_screen.ids.img.source = imagepath
class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()