import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.component_login import login_component
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.cookies import CookieState

@rx.page(
    route="/backend_login",
    title="LOGIN",
    on_load=CookieState.logout
)

def login_page() -> rx.Component:
    return rx.center(
        login_component(),
        padding="18em"
    )