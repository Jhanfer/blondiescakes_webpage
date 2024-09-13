import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updaters_states.about_us_updater import AboutUsUpdater

## About Us Updater ##
def update_about_us(*,button_text:str, title:str, sub_title:str, sumary:str, image_url:str):
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(button_text,background_color="#75D516",color="#000000")),
        rx.dialog.content(
            
            rx.vstack(
                    rx.heading("Edición del destacado"),
                align="center",
                padding_bottom="3em"),

            rx.vstack(
                    rx.flex(
                        rx.text("Titulo de página"),
                        rx.input(
                            placeholder="titulo",
                            #on_blur=IndexHighlightUpdater.set_title,
                            #on_change=IndexHighlightUpdater.set_title,
                            #on_focus=IndexHighlightUpdater.set_title,
                            value=title
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Subtítulo"),
                        rx.input(
                            placeholder="subtitulo",
                            #on_blur=IndexHighlightUpdater.set_title,
                            #on_change=IndexHighlightUpdater.set_title,
                            #on_focus=IndexHighlightUpdater.set_title,
                            value=sub_title
                        ),
                        width="100%",
                        justify="between"
                    ),
                    
                    rx.flex(
                        rx.text("Descripción del destacado"),
                        rx.text_area(
                            placeholder="descripción",
                            #on_blur=IndexHighlightUpdater.set_description,
                            #on_change=IndexHighlightUpdater.set_description,
                            #on_focus=IndexHighlightUpdater.set_description,
                            value=sumary,
                            size="3"
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("URL de la imagen(URL directa)"),
                        rx.input(
                            placeholder="url de imagen",
                            on_blur=AboutUsUpdater.set_image,
                            on_change=AboutUsUpdater.set_image,
                            on_focus=AboutUsUpdater.set_image,
                            value=image_url,
                            
                        ),
                        width="100%",
                        justify="between",
                    ),

                    rx.flex(
                        rx.text("Preview de imagen"),
                        rx.image(
                            src=AboutUsUpdater.image_url,
                            width="10em"
                        ),
                        width="100%",
                        justify="between",
                        #on_mount=[IndexHighlightUpdater.set_all(published_title,published_img_url,published_description)]
                    ),

                    rx.button("SUBIR",color_scheme="grass"),
                align="start",
                spacing="5",
                justify="center",
                width="100%",
                padding_bottom="3em",
                ),
                
                rx.vstack(
                        rx.dialog.close(
                            rx.button("cerrar",size="3",color_scheme="tomato")),
                    align="center"),
                )
        )