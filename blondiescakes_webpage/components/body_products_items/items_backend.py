import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.page_state import PageState
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import Featured
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updaters_states.item_updater import BackendUpdater


def backend_items(categorie:str,database_content:list[Featured]) -> rx.Component:
    return rx.flex(
        rx.separator(size="4"),
        rx.heading(categorie),
        rx.cond(
            PageState.general_database_data,
                    rx.vstack(

                        rx.hstack(
                            rx.flex(
                                rx.foreach( #iteradir
                                    database_content, #elemento iterado (lista)
                                    backend_featured_link), #llama a la función y le pasa como argumento cada elemento iterado
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
            

def backend_featured_link(featured:Featured) -> rx.Component:
    return   rx.vstack(
                rx.card(
                    rx.checkbox(value=featured.id,on_change=BackendUpdater.select(featured.id)),
                        rx.image(
                            src=featured.image_url,
                            background=st.ColorPalette.MAIN.value,
                            width="15em",
                            height="auto",
                            alt=f"producto: {featured.title}",
                            align="center"
                            ),
                    rx.vstack(
                            rx.text(
                                featured.title,
                                size="3",
                                align="center",
                                color=st.ColorPalette.ENFASIS.value),
                            rx.text(featured.image_url,
                                    size="3",
                                    align="center",
                                    color=st.ColorPalette.ENFASIS.value),
                            rx.text(featured.item_description,
                                    size="3",
                                    align="center",
                                    color=st.ColorPalette.ENFASIS.value),
                            rx.text(f"{featured.upload_time[0:10]} {featured.upload_time[11:20]}",
                                    size="3",
                                    align="center",
                                    color=st.ColorPalette.ENFASIS.value),
                            spacing="4"),
                    align="center",
                    justify="center"
                ),
            spacing="5",
            align="center",
            justify="center",
            )
