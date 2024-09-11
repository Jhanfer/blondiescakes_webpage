import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.page_state import PageState
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.supabase_database import Featured
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updaters_states.item_updater import BackendUpdater
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion
from blondiescakes_webpage.components.items_dialog_roots.dialogs_roots import dialog


def items() -> rx.Component:
    return rx.flex(
                    rx.box(
                        rx.cond(
                            PageState.class_buttercream,
                                    rx.vstack(
                                        
                                        rx.heading("Buttercream",size="8",color=st.ColorPalette.ENFASIS.value,padding_bottom="1em",style={"font-family":"'playwrite ar'"}),
                                        rx.hstack(
                                            rx.flex(

                                                rx.foreach( #iterar
                                                    PageState.class_buttercream, #elemento iterado (lista)
                                                    featured_link
                                                ), #llama a la función y le pasa como argumento cada elemento iterado
                                                
                                                spacing="7",
                                                wrap="wrap",
                                                width="100%",
                                                justify="center",
                                                align="center"),
                                            align="center"
                                            ),

                                        justify="center",
                                        align="center",
                                        width="100%",
                                        padding=st.Size.DEFAULT.value,
                                        spacing=st.SizeNoEm.MEDIUM.value
                                    ),
                        ),
                    on_mount=PageState.get_database_data_alter("buttercream"),
                    padding_top="1em"
                    ),


                    rx.box(
                        rx.cond(
                            PageState.class_frias,
                                rx.vstack(
                                    rx.heading("Frias",size="8",color=st.ColorPalette.ENFASIS.value,padding_bottom="1em",style={"font-family":"'playwrite ar'"}),
                                    rx.hstack(
                                        rx.flex(
                                            rx.foreach( #iterar
                                                PageState.class_frias, #elemento iterado (lista)
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
                                ),
                            ),
                        on_mount=PageState.get_database_data_alter("frias"),
                        direction="row"
                        ),

                        rx.box(
                            rx.cond(
                                PageState.class_tradicionales,
                                    rx.vstack(
                                        rx.heading("Tradicionales",size="8",color=st.ColorPalette.ENFASIS.value,padding_bottom="1em",style={"font-family":"'playwrite ar'"}),
                                        rx.hstack(
                                            rx.flex(
                                                rx.foreach( #iterar
                                                    PageState.class_tradicionales, #elemento iterado (lista)
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
                                    ),
                            ),
                        on_mount=PageState.get_database_data_alter("tradicionales")
                        ),


                        rx.box(
                        rx.cond(
                            PageState.class_saludables,
                                rx.vstack(
                                    rx.heading("Saludables",size="8",color=st.ColorPalette.ENFASIS.value,padding_bottom="1em",style={"font-family":"'playwrite ar'"}),
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
                                ),
                            ),
                        on_mount=PageState.get_database_data_alter("saludables"),
                        direction="row"
                        ),

                    wrap="wrap",
                    spacing="8",
                    justify="center",
                    direction="column"
                    )
            

def featured_link(featured:Featured) -> rx.Component:
    return rx.vstack(
                    motion(
                        rx.vstack(
                                    dialog(featured.title,featured.image_url,featured.item_description,True),

                                    rx.text(
                                        featured.title,
                                        size="6",
                                        align="center",
                                        color=st.ColorPalette.ENFASIS.value
                                    ),

                                    dialog(featured.title,featured.image_url,featured.item_description,False),
                                    
                            align="center",
                            justify="center",
                            spacing="5"
                        ),
                        
                        initial={"opacity": 0, "scale": 0.5},
                        while_in_view={"opacity": 1, "scale": 1},
                        while_focus={"opacity": 1, "scale": 1},
                        transition={"duration": 0.2,"ease":"easeOut"},
                        style={"display":"inline-block"}
                    ),
                spacing="6",
                align="center",
                justify="center",
    )        

