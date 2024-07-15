import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_badge_component.badge import badge,review
from blondiescakes_webpage.components.body_products_items.products_container import products_container

def body() -> rx.Component:
    return rx.box(
            badge(),
            products_container(),
            review(),
            rx.flex(
                    rx.vstack(
                            rx.heading("Quienes somos",color=st.ColorPalette.ENFASIS.value,style={"font_family":"pertili"}),
                            rx.text("""Blondiescake's ofrece una porción de la cultura venezolana y deliciosos postres. 
                                    El uso de ingredientes frescos y de primera calidad en cada postre se basa en recetas 
                                    antiguas, pero con un toque creativo que los hace irresistibles.""",color=st.ColorPalette.ENFASIS.value),
                        width="80%",
                        padding="3em",
                        align="center",
                        justify="center",
                        spacing="4"
                    ),
                align="center",
                justify="center",
                padding_top=st.Size.MEDIUM,
                padding_bottom=st.Size.MEDIUM.value
            ),
        
        direction="column",
        width="100%",
        align="center"
    )