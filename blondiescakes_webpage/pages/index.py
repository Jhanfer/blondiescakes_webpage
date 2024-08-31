import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.navbar.navbar import navbar
from blondiescakes_webpage.views.index_body.header.header import header
from blondiescakes_webpage.views.index_body.body.body import body
from blondiescakes_webpage.views.index_body.footer.footer import footer
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.page_state import PageState
from blondiescakes_webpage.utils import utils as ut
from blondiescakes_webpage.components.index_edit_components.highlight import IndexHighLight


@rx.page(
        route=ut.INDEX_ROUTE,
        title=ut.index_title,
        image=ut.preview,
        description=ut.index_description,
        meta=ut.index_meta,


        #script_tags: list[Any] | None = None,
)

def index() -> rx.Component:
    """Main page"""
    return rx.box(
                rx.vstack(
                    ut.lang(),
                    navbar(),
                    header(),
                    body(),
                    footer(),
            
                    width="100%",
                    spacing="0",
                    align="center",
                ),
            style={"overflow":"hidden"},

        )