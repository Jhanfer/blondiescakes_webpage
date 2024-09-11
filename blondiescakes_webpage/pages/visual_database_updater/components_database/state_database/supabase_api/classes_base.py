import reflex as rx
from typing import Optional

##Bases##
#Featured index items#
class Featured(rx.Base):
    id:str
    image_url:str
    item_description:str
    title:str
    upload_time:str
    categorie:str

#Highlight#
class Highlights(rx.Base):
    title:str
    description:str
    image_url:str
    switch:bool

#Windata#
class WinData(rx.Base):
    id:str
    text:str
    image_url:str
    switch:bool

#reviews#
class ReviewsBase(rx.Base):
    username:str
    rating:str
    date:str
    description:str

#Index Summary#
class IndexSumary(rx.Base):
    paragraph:str

#About us#
class AboutUs(rx.Base):
    title:str
    sub_title:str
    sumary:str
    image_url:str

class Purposes(rx.Base):
    title:str
    sumary:str
    type:Optional[str]