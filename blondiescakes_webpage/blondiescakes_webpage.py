import reflex as rx

#import pages
from blondiescakes_webpage.pages.visual_database_updater import visual_database_updater
from blondiescakes_webpage.pages import index
from blondiescakes_webpage.pages.redirect_pages import backend_reloader
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_page import login_page
###

from blondiescakes_webpage.styles import styles as st
from fastapi import FastAPI

app = rx.App(
    stylesheets=st.STYLESHEETS,
    style=st.STYLE_SHEET
)


