import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.page_state import PageState
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import Featured
from typing import Optional

def items() -> rx.Component:
    return rx.flex(
        rx.cond(
            PageState.database_data,
                    rx.vstack(
                        rx.text("NUESTROS PRODUCTOS"),
                        rx.hstack(
                            rx.flex(
                                rx.foreach( #iteradir
                                    PageState.database_data, #elemento iterado (lista)
                                    featured_link), #llama a la función y le pasa como argumento cada elemento iterado
                                spacing="7",
                                wrap="wrap",
                                width="100%",
                                justify="center",
                                align="center"),
                            align="center"),

                        justify="center",
                        align="center",
                        width="100%",
                        padding=st.Size.DEFAULT.value,
                        spacing=st.SizeNoEm.MEDIUM.value
                    )
                ),
            wrap="wrap",
            spacing="8")
            

def featured_link(featured:Featured) -> rx.Component:
    return rx.vstack(

                rx.link(
                    rx.image(
                        src=featured.image_url,
                        background=st.ColorPalette.MAIN.value,
                        width="15em",
                        height="auto",
                        alt=f"producto: {featured.title}",
                        align="center"),
                    href=featured.url_purchase,
                    is_external=True,
                    style={"_hover":"none"}),

                    rx.text(
                        featured.title,
                        size="3",
                        align="center",
                        color=st.ColorPalette.ENFASIS.value),

                rx.link(rx.button("PEDIR",radius="none",width="100%",justify="center"),href=featured.url_purchase,is_external=True),
                
                spacing="5",
                align="center",
                justify="center",
                )