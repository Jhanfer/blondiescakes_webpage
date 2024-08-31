import reflex as rx
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import WinData
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import get_windows_data
from blondiescakes_webpage.pages.visual_database_updater.components_database.updater_component import updater_windows
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.Updater import IndexWindowsUpdater


class IndexWindows(rx.State):

        title:str
        description:str
        windows_data:list[WinData]
        switch:bool
        
        async def get_data(self):
                all_data = await get_windows_data()

                self.title = all_data[0][0][0]
                self.description = all_data[0][0][1]
                self.windows_data = sorted(all_data[1], key=lambda x: int(x.id))
                self.switch = all_data[1][0].switch
                



def windows() -> rx.Component:
        return motion(
                rx.cond(IndexWindows.switch,
                        rx.flex(
                                rx.text(
                                        IndexWindows.title, 
                                        size="9",
                                        padding_top="1em",
                                        padding_bottom="1em",
                                        style={"font-family":"pertili"}
                                ),
                                rx.hstack(
                                        rx.flex(
                                                rx.foreach(
                                                        IndexWindows.windows_data,
                                                        other_products
                                                ),
                                        spacing="4",
                                        display=["none","none","none","flex","flex"]
                                        ),

                                        rx.flex(
                                                rx.grid(
                                                        rx.scroll_area(
                                                                rx.flex(
                                                                        rx.foreach(
                                                                                IndexWindows.windows_data,
                                                                                other_products
                                                                        ),
                                                                spacing="4"
                                                                ),
                                                        scrollbars="horizontal",
                                                        type="always"
                                                        ),
                                        padding="1em"),
                                        display=["flex","flex","flex","none","none","none"]
                                        ),

                                justify="center",
                                align="center",
                                width="100%",
                                z_index="5",
                                ),
                                rx.flex(
                                        rx.vstack(
                                                rx.text(
                                                        IndexWindows.description,
                                                color=st.ColorPalette.ENFASIS.value,
                                                style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
                                                ),
                                        max_width="60em",
                                        width="100%",
                                        padding="3em",
                                        align="center",
                                        justify="center",
                                        spacing="6"
                                        ),
                                align="center",
                                justify="center",
                                padding_top=st.Size.MEDIUM,
                                padding_bottom=st.Size.LARGE.value
                                ),
                        direction="column",
                        align="center",
                        justify="center",
                        )
                ),
                initial={"opacity": 0, "scale": 0.5},
                animate={"opacity": 1, "scale": 1},
                transition={"duration": 0.2,"ease":"easeOut"},
                style={"display":"inline-block"}
        )


def other_products(featured:WinData) -> rx.Component:
        return motion(
                rx.flex(
                        rx.text(
                                featured.text,
                                z_index="100000",
                                color=st.ColorPalette.MAIN.value,
                                style={
                                        "font-size":"2em",
                                },
                                position="absolute"
                        ),
                        rx.flex(
                                
                                width="17em",
                                height="18em",
                                background_image=featured.image_url,
                                style={ 
                                        "filter": "brightness(0.7)",
                                        "border-radius": "30em 30em 0em 0em",
                                        "background-size": "cover"
                                },
                                align="center",
                                justify="center",
                                class_name="windows-container"
                        ),
                        align="center",
                        justify="center",
                        width="17em",
                        height="18em",
                ),
        while_hover={"opacity":0.9},
        transition={"damping":20,"swiftness":20}
        )



## Backend Component##
def windows_backend() -> rx.Component:
        return rx.card(
                rx.flex(
                        rx.text(
                                IndexWindows.title,
                                size="5"
                        ),
                        rx.hstack(
                                rx.flex(
                                        rx.foreach(
                                                IndexWindows.windows_data,
                                                other_products
                                        ),
                                spacing="4",
                                display=["none","none","none","flex","flex"]
                                ),

                                rx.flex(
                                        rx.grid(
                                                rx.scroll_area(
                                                        rx.flex(
                                                                rx.foreach(
                                                                        IndexWindows.windows_data,
                                                                        other_products
                                                                ),
                                                        spacing="4"
                                                        ),
                                                scrollbars="horizontal",
                                                type="always"
                                                ),
                                        padding="1em"
                                        ),
                                display=["flex","flex","flex","none","none","none"]
                                ),
                        justify="center",
                        align="center",
                        width="100%",
                        z_index="5",
                        ),

                        rx.text(
                                IndexWindows.description,
                                size="5",
                                
                        ),
                direction="column",
                spacing="5",
                on_mount=IndexWindows.get_data,
                on_mouse_enter=[IndexWindows.get_data,IndexWindowsUpdater.get_all_data(IndexWindows.windows_data)],
                justify="center",
                align="center"
                ),

                updater_windows(button_text="actualizar", published_title=IndexWindows.title, published_description=IndexWindows.description, all_data=IndexWindows.windows_data)
        )