import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.supabase_database import IndexSumary
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import get_sumary_data
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updater_components.update_sumary_gui import updater_sumary

class IndexSumaryTexts(rx.State):
    paragraphs_list:list[IndexSumary]
    title:str
    data_for_backend:str

    async def set_sumary_data(self):
        data = await get_sumary_data()
        self.title = data[1] 
        self.paragraphs_list = data[0]
        self.data_for_backend = data[0][0].paragraph

def index_sumary():
    return  rx.flex(
                rx.cond(IndexSumaryTexts.title,
                    rx.vstack(
                            rx.icon(tag="wheat",color=st.ColorPalette.LINES.value),
                            rx.heading(IndexSumaryTexts.title,
                                    color=st.ColorPalette.ENFASIS.value,
                                    style={"font-size":"clamp(1rem, 0.5vw + 2.1rem, 3.5rem)"}
                            ),

                            rx.foreach(
                                IndexSumaryTexts.paragraphs_list,
                                paragraph
                            ),

                            rx.icon(tag="cherry",color=st.ColorPalette.LINES.value),
                        max_width="60em",
                        width="100%",
                        padding="3em",
                        align="center",
                        justify="center",
                        spacing="6"
                    ),

                    rx.vstack(
                        rx.skeleton(rx.button("button-small"), width="40em",height="5em",loading=True),
                        rx.skeleton(rx.button("button-small"), width="40em",height="50em",loading=True),
                        padding="2em"
                    ),
                ),
        align="center",
        justify="center",
        padding_top=st.Size.MEDIUM,
        padding_bottom=st.Size.MEDIUM.value,
        on_mount=IndexSumaryTexts.set_sumary_data
    )


def paragraph(featured:IndexSumary) -> rx.Component:
    return rx.markdown(
                featured.paragraph,
                color=st.ColorPalette.ENFASIS.value,
                style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
    )




def sumary_backend() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text("~Editar el texto de resumén de página~", size="8"),
            rx.heading(
                    IndexSumaryTexts.title,
                    color=st.ColorPalette.ENFASIS.value,
            ),
            rx.foreach(
                    IndexSumaryTexts.paragraphs_list,
                    paragraph
            ),
            updater_sumary("Actualizar datos", IndexSumaryTexts.title, IndexSumaryTexts.data_for_backend)
        ),
        size="5",
        on_mount=IndexSumaryTexts.set_sumary_data
    )