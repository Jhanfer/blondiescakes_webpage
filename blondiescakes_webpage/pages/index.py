import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.navbar.navbar import navbar
from blondiescakes_webpage.views.index_body.header.header import header
from blondiescakes_webpage.views.index_body.body.body import body
from blondiescakes_webpage.views.index_body.footer.footer import footer
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.page_state import PageState


@rx.page(
        route="/",
        title="BlondiesCake's",
        #image=None,
        description="Los mejores pasteles",
        #meta=,
        #script_tags: list[Any] | None = None,
        
)

def index() -> rx.Component:
    """Main page"""
    return rx.box(
                rx.vstack(
                    navbar(),
                    header(),
                    body(),
                    footer(),
            
                    width="100%",
                    spacing="0",
                    align="center",
                ),
            style={"overflow":"hidden"}
        )