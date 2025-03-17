random_text=[
    "Cool, I'm on it sir",
    "okay sir ,I'm working on it",
    "just a sec sir",
]


from kivy.config import Config


width,height=1980,1080

Config.set('graphics','width',width)
Config.set('graphics','height',height)
Config.set('graphics','fullscreen','True')


SCREEN_WIDTH= Config.getint('graphics','width')
SCREEN_HEIGHT= Config.getint('graphics','height')