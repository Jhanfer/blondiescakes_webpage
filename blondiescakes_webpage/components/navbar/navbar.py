import reflex as rx
from blondiescakes_webpage.styles import styles as st
from reflex.components import chakra as ch

def navbar() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            navbar_content(),
            width="100%"),
        bg=st.ColorPalette.MAIN.value,
        padding=st.Size.SMALL.value,
        class_name="gradient-element",
        position="sticky",
        width="100%",
        top="0",
        z_index = "999"
)



#Navbar components

def text(text:str) -> rx.Component:
    return rx.link(
            rx.text(text,
                    color=st.TextColor.TITLES.value),
                is_external=False,
                href="",
                padding_left="1em",
                padding_right="1em")

def navbar_content() -> rx.Component:
    return rx.hstack(

        rx.vstack(
            rx.hstack(
                text("INICIO"),
                text("CONTACTO"),
                text("ENVÍOS"),
                spacing="9"),
            rx.separator(decorative=True,color_scheme="gold")),

        rx.spacer(direction="row"),

        rx.image(src="/navbar/navbar.png",
                width="6.9em",
                height="4em",
                position="relative"),

        rx.spacer(direction="row"),

        rx.vstack(
            rx.hstack(
                text("SOBRE NOSOTROS"),
                text("VISIÓN"),
                text("MISIÓN"),
                spacing="9"),
            rx.separator(decorative=True,color_scheme="gold")),

        width="100%",
        align="center",
        justify="center",
        padding_left="3em",
        padding_right="3em"
        )
