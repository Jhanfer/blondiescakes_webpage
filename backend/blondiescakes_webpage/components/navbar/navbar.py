import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.navbar.drawer import drawer


def navbar() -> rx.Component:
    return rx.hstack(
        
            rx.box(
                    navbar_content(),
                display=["none", "none", "flex", "flex", "flex"],
                height="100%",
                width="100%"),
                

            rx.box(
                    navbar_content_mobile(),
                display=["flex", "flex", "none", "none", "none"],
                height="100%",
                width="100%",
                justify="center",
                align="center"),

        justify="center",
        align="center",
        bg=st.ColorPalette.MAIN.value,
        padding=st.Size.SMALL.value,
        class_name="gradient-element",
        position="fixed",
        width="100%",
        z_index = "999"
)



#Navbar components

def text(text:str) -> rx.Component:
    return rx.link(
            rx.text(text,
                    color=st.TextColor.TITLES.value,
                    ),
                is_external=False,
                href="",
                padding_left="1em",
                padding_right="1em")

def navbar_content() -> rx.Component:
    return rx.hstack(

        rx.vstack(
            rx.flex(
                text("INICIO"),
                text("CONTACTO"),
                text("ENVÍOS"),
                display=["none", "none", "flex", "flex", "flex"],
                direction="row"
                ),

            rx.separator(decorative=True,color_scheme="gold")),

        rx.image(src="/navbar/navbar.png",
                width="6.9em",
                height="4em",
                position="sticky"),

        rx.vstack(
            rx.flex(
                text("NOSOTROS"),
                text("VISIÓN"),
                text("MISIÓN"),
                display=["none", "none", "flex", "flex", "flex"],
                direction="row"
                ),
            rx.separator(decorative=True,color_scheme="gold")),

        width="100%",
        align="center",
        justify="center",
        spacing="9"
        )


def navbar_content_mobile() -> rx.Component:
    return rx.hstack(

        rx.divider(size="3",color_scheme="gold"),
        drawer(),
        rx.divider(size="3",color_scheme="gold"),
        
        spacing="8",
        justify="center",
        align="center",
        width="100%",
        padding_left="1em",
        padding_right="1em"
    )

