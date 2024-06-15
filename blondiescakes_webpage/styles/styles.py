import reflex as rx
from enum import Enum


#Sizes
class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8"
    DEFAULT="1em"
    BIG="1.5em"
    LARGE="2em"
    EXTRA="2.5em"

class SizeNoEm(Enum):
    SMALL="1"
    MEDIUM="2"
    DEFAULT="3"
    BIG="5"
    LARGE="7"
    EXTRA="9"

#Colors
class ColorPalette(Enum):
    MAIN="#F7E6DB"
    ENFASIS="#463626"
    LINES="#B6985E"
    BACKGROUND="#FFFFFF"

class TextColor(Enum):
    DEFAULT="#FFFFFF"
    TITLES="#463626"


#stylesheets
STYLESHEETS=[
    #"https://fonts.googleapis.com/css?family=JetBrains+Mono:weight@100&display=swap",
    #"https://fonts.googleapis.com/css?family=Nunito+Sans:weight@400&display=swap",
    "/CSS/css.css"
]

STYLE_SHEET={
    "background_color":ColorPalette.BACKGROUND.value,
    
    rx.link:{
        "text_decoration":"None",
        "_hover":{},
        "cursor":"pointer"
    },
    rx.button:{
        "cursor":"pointer",
        "_hover":{
        }
    }
}