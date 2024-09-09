import reflex as rx 
from blondiescakes_webpage.components.body_badge.body_badge_component.badge import badge,review
from blondiescakes_webpage.components.body_products_items.products_container import products_container
from blondiescakes_webpage.components.body_sumary.sumary import index_sumary

def body() -> rx.Component:
    return rx.box(
            badge(),
            products_container(),
            review(),
            index_sumary(),
        
        direction="column",
        width="100%",
        align="center"
    )


