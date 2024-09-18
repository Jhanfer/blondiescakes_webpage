import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database import api as api
from blondiescakes_webpage.components.index_edit_components.highlight import highlight_backend
from blondiescakes_webpage.components.index_edit_components.other_products_windows import windows_backend
from blondiescakes_webpage.state_general.google_reviews_api import GoogleMapsReviewsUpdater
from blondiescakes_webpage.components.body_sumary.sumary import sumary_backend
from blondiescakes_webpage.components.about_us_components.about_us_component import about_us_component_backend
from blondiescakes_webpage.components.about_us_components.pros_component import pros_backend
from blondiescakes_webpage.components.about_us_components.purposes_component import purposes_backend_component

def index_text_updater() -> rx.Component:
    return rx.flex(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Pagina principal", value="tab1", color="black", color_scheme="crimson"),
                rx.tabs.trigger("Sobre Nosotros", value="tab2", color="black", color_scheme="crimson"),
                style={"justify-content":"center"},
                size="1"
            ),

            rx.tabs.content(
                rx.vstack(
                    highlight_backend(),
                    windows_backend(),
                    sumary_backend(),
                    google_reviews(),
                    justify="center",
                    align="center"
                ),
                value="tab1",
            ),

            rx.tabs.content(
                rx.vstack(
                    about_us_component_backend(),
                    pros_backend(),
                    purposes_backend_component(),
                    justify="center",
                    align="center"
                ),
                value="tab2",
            ),
        ),
        align="center",
        justify="center",
        direction="column"
    )

def google_reviews() -> rx.Component:
    return  rx.card(
                rx.text("Actualizar datos de las reviews"),
                rx.alert_dialog.root(
                    rx.alert_dialog.trigger(
                        rx.button("Actualizar datos"),
                    ),
                    rx.alert_dialog.content(
                        rx.alert_dialog.title("Actualizar datos de las reviews"),
                        rx.alert_dialog.description(
                            "¿Estás seguro de querer hacerlo? Recuerda que no se pueden actualizar más de 100 veces por mes.",
                        ),
                        rx.flex(
                            rx.alert_dialog.cancel(
                                rx.button("Cancelar",background_color="red"),
                            ),
                            rx.alert_dialog.action(
                                rx.button("Actualizar",on_click=GoogleMapsReviewsUpdater.update_google_reviews_database,background_color="green"),
                            ),
                            spacing="3",
                            justify="between"
                        ),
                    ),
                ),
                rx.text("AVISO! NO ACTUALIZAR MÁS DE 100 VECES AL MES"),

        size="5"
    )