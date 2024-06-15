import reflex as rx
from rxconfig import config
from blondiescakes_webpage.pages import index
from blondiescakes_webpage.styles import styles as st

app = rx.App(
    stylesheets=st.STYLESHEETS,
    style=st.STYLE_SHEET
)