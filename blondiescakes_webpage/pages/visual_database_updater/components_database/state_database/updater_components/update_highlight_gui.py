import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updaters_states.index_highlight_updater import IndexHighlightUpdater

## Highlight Updater ##
def updater_highlight(*,button_text:str,published_title:str,published_description:str,published_img_url:str):
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(button_text,background_color="#75D516",color="#000000")),
        rx.dialog.content(
            rx.vstack(
                    rx.heading("Edición del destacado"),
                align="center",
                padding_bottom="3em"),
        

            rx.vstack(
                    rx.flex(
                        rx.text("Titulo del destacado"),
                        rx.input(
                            placeholder="titulo",
                            on_blur=IndexHighlightUpdater.set_title,
                            on_change=IndexHighlightUpdater.set_title,
                            on_focus=IndexHighlightUpdater.set_title,
                            value=published_title
                        ),
                        width="100%",
                        justify="between"
                    ),
                    
                    rx.flex(
                        rx.text("Descripción del destacado"),
                        rx.text_area(
                            placeholder="descripción",
                            on_blur=IndexHighlightUpdater.set_description,
                            on_change=IndexHighlightUpdater.set_description,
                            on_focus=IndexHighlightUpdater.set_description,
                            value=published_description,
                            size="3"
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("URL de la imagen(URL directa)"),
                        rx.input(
                            placeholder="url de imagen",
                            on_blur=IndexHighlightUpdater.set_image_url,
                            on_change=IndexHighlightUpdater.set_image_url,
                            on_focus=IndexHighlightUpdater.set_image_url,
                            value=published_img_url,
                            
                        ),
                        width="100%",
                        justify="between",
                        on_mount=[IndexHighlightUpdater.set_all(published_title,published_img_url,published_description)]
                    ),



                    rx.button("SUBIR",color_scheme="grass",on_click=lambda:[IndexHighlightUpdater.update_data]),
                align="start",
                spacing="5",
                justify="center",
                width="100%",
                padding_bottom="3em",
                ),
                
                rx.vstack(
                        rx.dialog.close(
                            rx.button("cerrar",size="3",color_scheme="tomato",on_click=IndexHighlightUpdater.reset_data)),
                    align="center"),
                )
        )