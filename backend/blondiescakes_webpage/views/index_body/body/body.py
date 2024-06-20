import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_badge_component.badge import badge,review
from blondiescakes_webpage.components.body_products_items.products_container import products_container

def body() -> rx.Component:
    return rx.vstack(
            badge(),
            products_container(),
            review(),
            rx.vstack(
                    rx.heading("Quienes somos",style={"font_family":"pertili"}),
                    rx.text("Blondiescake's ofrece una porción de la cultura venezolana y deliciosos postres. El uso de ingredientes frescos y de primera calidad en cada postre se basa en recetas antiguas, pero con un toque creativo que los hace irresistibles."),
                width="60%",
                padding="3em"
            ),
        width="100%",
        align="center"
)