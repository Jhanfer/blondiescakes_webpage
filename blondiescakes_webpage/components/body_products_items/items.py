import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.page_state import PageState
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import Featured
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.Updater import BackendUpdater
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion

def items() -> rx.Component:
    return rx.flex(
                rx.cond(
                    PageState.class_saludables,
                            rx.vstack(
                                rx.text("NUESTROS PRODUCTOS",color=st.ColorPalette.ENFASIS.value,size="4",padding_bottom="2em"),
                                rx.hstack(
                                    rx.flex(
                                        rx.foreach( #iterar
                                            PageState.class_saludables, #elemento iterado (lista)
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
                    spacing="8",
                    on_mount=[PageState.get_database_data_alter("saludables")]
                    )
            

def featured_link(featured:Featured) -> rx.Component:
    return rx.vstack(
                    motion(
                        rx.vstack(
                                motion(
                                    rx.image(
                                            src=featured.image_url,
                                            background=st.ColorPalette.MAIN.value,
                                            width="15em",
                                            height="15em",
                                            alt=f"producto: {featured.title}",
                                            align="center",
                                            on_click=rx.redirect(featured.url_purchase),
                                            display="block",#con esto hacemos que la imagen sea cuadrada sin estrechar
                                            style={"overflow":"hidden", #con esto hacemos que la imagen sea cuadrada sin estrechar
                                                    "object-fit":"cover"},
                                            ),
                                    while_hover={"scale":1.1},
                                    while_tap={"scale":0.9},
                                    transition={"type": "spring", "stiffness":300,"damping":20}
                                ),
                                    rx.text(
                                        featured.title,
                                        size="3",
                                        align="center",
                                        color=st.ColorPalette.ENFASIS.value
                                    ),

                                rx.link(
                                        motion(
                                            rx.button("PEDIR",
                                                radius="none",
                                                width="100%",
                                                justify="center",
                                                ),
                                        while_hover={"scale":1.1},
                                        while_tap={"scale":0.9},
                                        transition={"type": "spring", "stiffness":300,"damping":20}
                                        ),
                                    href=featured.url_purchase,is_external=True
                                ),
                            align="center",
                            justify="center",
                        ),
                        
                        initial={"opacity": 0, "scale": 0.5},
                        #animate={"opacity":1,"scale":1},
                        while_in_view={"opacity": 1, "scale": 1},
                        while_focus={"opacity": 1, "scale": 1},
                        transition={"duration": 0.2,"ease":"easeOut"},#"repeatType":"reverse","repeat":"Infinity"},
                        style={"display":"inline-block"}
                    ),
                spacing="5",
                align="center",
                justify="center",
    )        




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
    return rx.vstack(
                rx.card(
                    rx.checkbox(value=featured.id,on_change=BackendUpdater.select(featured.id)),
                        rx.image(
                            src=featured.image_url,
                            background=st.ColorPalette.MAIN.value,
                            width="15em",
                            height="auto",
                            alt=f"producto: {featured.title}",
                            align="center"),
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
                            rx.text(featured.url_purchase,
                                    size="3",
                                    align="center",
                                    color=st.ColorPalette.ENFASIS.value),
                            rx.text(f"{featured.upload_time[0:10]} {featured.upload_time[11:20]}",
                                    size="3",
                                    align="center",
                                    color=st.ColorPalette.ENFASIS.value),
                            spacing="4"),
                    align="center",
                    justify="center"),

                
                spacing="5",
                align="center",
                justify="center",
                )