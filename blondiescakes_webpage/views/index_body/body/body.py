import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_header_textimage.textimage import textimage
from blondiescakes_webpage.components.body_badge.body_badge_component.badge import badge

def body() -> rx.Component:
    return rx.vstack(
        badge(),
        width="100%"
)