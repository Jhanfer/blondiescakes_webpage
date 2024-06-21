import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater import visual_database_updater
from rxconfig import config
from blondiescakes_webpage.pages import index
from blondiescakes_webpage.pages.visual_database_updater import visual_database_updater
from blondiescakes_webpage.pages.redirect_pages import backend_reloader
from blondiescakes_webpage.styles import styles as st

app = rx.App(
    stylesheets=st.STYLESHEETS,
    style=st.STYLE_SHEET
)