import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.pages.visual_database_updater.components_database import component_login
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.page_state import PageState
from blondiescakes_webpage.components.body_products_items.items import items
from blondiescakes_webpage.pages.visual_database_updater.components_database.updater_component import updater


@rx.page(
    route="/database_updater",
    title="Database",
    on_load=PageState.get_database_data
)


def index() -> rx.Component:
    return rx.vstack(
    
        rx.hstack(
                updater(),

                rx.button("eliminar artículo",background_color="#ec1c1c",color="#000000"),

            width="90%",
            bg="grey",
            height="5em",
            align="center",
            justify="between",
            padding_left="3em",
            padding_right="3em"),
        rx.text("ITEMS DE LA TIENDA"),
        items(),
        

    align="center",
    justify="center",
    padding_top="10em")




