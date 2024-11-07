import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updaters_states.item_updater import BackendUpdater


##Items updater##
def updater(button_text:str):
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(button_text,background_color="#75D516",color="#000000")),
        rx.dialog.content(
            rx.vstack(
                    rx.heading("Creación de artículo"),
                align="center",
                padding_bottom="3em"),

            rx.vstack(
                    rx.flex(
                        rx.text("Título del artículo"),
                        rx.input(
                            placeholder="titulo del artículo",
                            on_blur=BackendUpdater.set_title,
                            on_change=BackendUpdater.set_title,
                            on_focus=BackendUpdater.set_title
                        ),
                        width="100%",
                        justify="between"
                    ),
                    
                    rx.flex(
                        rx.text("Descripción del articulo"),
                        rx.text_area(
                            placeholder="descripción",
                            on_blur=BackendUpdater.set_item_description,
                            on_change=BackendUpdater.set_item_description,
                            on_focus=BackendUpdater.set_item_description
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("URL de la imagen(URL directa)"),
                        rx.input(
                            placeholder="url de imagen",
                            on_blur=BackendUpdater.set_image_url,
                            on_change=BackendUpdater.set_image_url,
                            on_focus=BackendUpdater.set_image_url
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Precio del artículo"),
                        rx.input(
                            placeholder="precio",
                            type="number",
                            on_blur=BackendUpdater.set_price,
                            on_change=BackendUpdater.set_price,
                            on_focus=BackendUpdater.set_price
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Categoría"),
                        rx.select(["Pagina principal","Buttercream","Frios","Saludables","Tradicionales"],
                            placeholder="seleccione categoría",
                            on_change=BackendUpdater.set_categorie,
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.button("SUBIR",background_color="green",on_click=lambda:[BackendUpdater.update_data,rx.call_script("window.location.reload()")]),
                align="start",
                spacing="5",
                justify="center",
                width="100%",
                padding_bottom="3em",
                on_mount=BackendUpdater.refresh_state_refresh
                ),
                
                rx.vstack(
                        rx.dialog.close(
                            rx.button("cerrar",size="3",background_color="red",on_click=BackendUpdater.reset_data)),
                    align="center"),
                )
        )
