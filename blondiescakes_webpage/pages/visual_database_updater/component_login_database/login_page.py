import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.component_login import login_component
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.cookies import CookieState

@rx.page(
    route="/backend_login",
    title="LOGIN",
    on_load=CookieState.logout
)

def login_page() -> rx.Component:
    return rx.flex(

        rx.vstack(
            rx.flex(
                    login_component(),
                align="center",
                justify="center"
                ),
            display=["none","flex","flex","flex"],
            padding_top="10em",
            align="center",
            justify="center",
            width="100%"
        ),

        rx.vstack(
            rx.flex(
                login_component(),
            align="center",
            justify="center"
            ),
        display=["flex","none","none","none"],
        padding_top="5em",
        align="center",
        justify="center",
        width="100%"
        )   
    )