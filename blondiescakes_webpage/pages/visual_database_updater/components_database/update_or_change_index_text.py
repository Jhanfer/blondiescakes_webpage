import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database import api as api
from blondiescakes_webpage.components.index_edit_components.highlight import highlight_backend
from blondiescakes_webpage.components.index_edit_components.other_products_windows import windows_backend


def index_text_updater() -> rx.Component:
    return rx.flex(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Pagina principal", value="tab1"),
                rx.tabs.trigger("Sobre Nosotros", value="tab2"),
            ),

            rx.tabs.content(
                rx.vstack(
                    highlight_backend(),
                    windows_backend(),
                    rx.text(" -Reviews"),
                    rx.text(" -Resumen")
                ),
                value="tab1",
            ),

            rx.tabs.content(
                rx.text(" -Titulo"),
                rx.text(" -Encabezado"),
                rx.text(" -Ventajas"),
                rx.text(" -Visión"),
                rx.text(" -Misión"),


                value="tab2",
            ),
        ),
        align="center",
        justify="center",
        direction="column"
    )