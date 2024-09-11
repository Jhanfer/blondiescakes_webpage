import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updaters_states.sumary_updater_state import IndexSumaryUpdater
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.supabase_database import IndexSumary

def updater_sumary(button_text:str,title:str,sumary:IndexSumary) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(button_text,background_color="#75D516",color="#000000"),
            ),
        rx.dialog.content(

            rx.vstack(
                    rx.heading("Edición del resumen de la página"),
                align="center",
                padding_bottom="3em"
            ),

            rx.vstack(
                    rx.flex(
                        rx.text("Titulo del resumen"),
                        rx.input(
                            placeholder="titulo",
                            on_blur=IndexSumaryUpdater.set_title,
                            on_change=IndexSumaryUpdater.set_title,
                            on_focus=IndexSumaryUpdater.set_title,
                            value=title,

                        ),
                            width="100%",
                            justify="between"
                    ),

                    rx.flex(
                        rx.text("Resumen de página"),
                        rx.text_area(
                            placeholder="resumen",
                            on_blur=IndexSumaryUpdater.set_texts,
                            on_change=IndexSumaryUpdater.set_texts,
                            on_focus=IndexSumaryUpdater.set_texts,
                            value=sumary,
                            size="3",
                            resize="vertical",
                            radius="full"
                        ),
                        width="100%",
                        justify="between",
                        
                    ),



                    rx.button("SUBIR",color_scheme="grass", on_click=IndexSumaryUpdater.upload_sumary_data),
                align="start",
                spacing="6",
                justify="center",
                width="100%",
                padding_bottom="3em",
                
                ),
                
                rx.vstack(
                        rx.dialog.close(
                            rx.button("cerrar",size="3",color_scheme="tomato")),
                    align="center"
                    ),

                )
        )