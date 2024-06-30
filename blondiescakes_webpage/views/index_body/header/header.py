import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_header_textimage.textimage import textimage_header

def header() -> rx.Component:
    return rx.flex(

            rx.hstack(
                    rx.spacer(),
                    rx.text("PASTELERÍA A LA CARTA",
                            color=st.ColorPalette.ENFASIS.value,
                            padding_right="3em"
                    ),
                justify="between",
                spacing="9",
                display="flex",
                position="relative",
                z_index="5",
                width="100%",
                align="center"
            ),

            rx.hstack( 
                    rx.flex(
                            rx.link(
                                    rx.text("@BLONDIES_CAKE",
                                        color=st.ColorPalette.ENFASIS.value,
                                        position="relative",
                                        size="2",
                                        align="center"
                                    ),
                            ),
                            rx.icon(tag="instagram",
                                        position="relative",
                                        width="1.09em",
                                        height="auto"
                                    ),
                            #rx.chakra.divider(decorative=True,color=st.ColorPalette.LINES.value,border_color=st.ColorPalette.LINES.value),
                            
                            
                        #width="100%",
                        position="absolute",

                        top="13em",
                        #right="auto",
                        left="1em",
                        bottom="auto",

                        justify="start",
                        align_items="center",

                        spacing="4",
                        display="flex",
                        class_name="vertical-text",
                    ),
                    textimage_header("header/header_image_example.png","Regala amor, regala dulce"),
                spacing="9",
                width="100%",
                align="center",
                display="flex",
                position="relative",
                justify="center",
                z_index="5"
            ),
        align="center",
        justify="between",
        #height="25em",
        width="100%",
        spacing="5",
        direction="column",
        padding_bottom="5em"

    )









"""spacing="4",
    height="1em",

    display="flex",

    padding_bottom="30em",
    direction="row",

    margin_left="-18em",

    class_name="vertical-text",
    position="absolute","""



"""rx.vstack(

                rx.tablet_and_desktop(
                    rx.hstack(
                        rx.box(
                                rx.text("PASTELERÍA A LA CARTA",
                                        color=st.ColorPalette.ENFASIS.value,
                                        position="absolute",
                                ),
                            width="10%",
                            padding_left="30em",
                            padding_bottom="2em",
                            position="absolute"
                        ),
                    ),

                    
                    rx.hstack(
                        rx.hstack(
                                
                                rx.link(
                                    rx.text("@BLONDIES_CAKE",
                                        color=st.ColorPalette.ENFASIS.value,
                                        position="absolute",
                                        ),
                                    ),
                                rx.chakra.divider(decorative=True,color=st.ColorPalette.LINES.value,border_color=st.ColorPalette.LINES.value,padding="1em",position="absolute"),
                    
                            spacing="5",
                            height="1em",
                            padding_left="10em",
                            padding_bottom="50em",
                            direction="row",
                            class_name="vertical-text",
                            position="absolute"
                        ),
                        textimage_header("header/header_image_example.png","Regala amor, regala dulce"),
                        
                    ),
                ),


                rx.mobile_only(
                rx.vstack(
                        rx.text("PASTELERÍA A LA CARTA"),
                        textimage_header("header/header_image_example.png","Regala amor, regala dulce"),
                    align="center",
                    justify="center",
                    padding_top="7em"),
                ),



        height="25em",
        align="center",
        justify="center",
        padding_top="5em",
        padding_bottom="5em"
    )


"""

"""rx.vstack(

                rx.tablet_and_desktop(
                        rx.hstack(
                            rx.box(
                                    rx.link(
                                        rx.text("@BLONDIES_CAKE",
                                            color=st.ColorPalette.ENFASIS.value,
                                            position="absolute",
                                        )
                                    ),
                                width="50%",
                                height="1em",
                                margin_bottom="5em",
                                class_name="vertical-text",
                                padding_bottom="20em"
                                
                            ),
                        
                            textimage("header/header_image_example.png","Regala amor, regala dulce"),
                            rx.box(
                                    rx.text("PASTELERÍA A LA CARTA",
                                            color=st.ColorPalette.ENFASIS.value,
                                            position="absolute"
                                    ),
                                width="10%",
                                margin="5em",
                            )
                        ),

            ),
            rx.mobile_only(
                rx.vstack(
                        rx.text("PASTELERÍA A LA CARTA"),
                        textimage("header/header_image_example.png","Regala amor, regala dulce"),
                    align="center",
                    justify="center",
                    padding_top="7em"),
            ),

        align="center",
        justify="center",
        width="100%",
        #padding_top="3em",
        #padding_left="3em",
        #padding_right="3em",
        #padding_bottom="5em",
        height="40em",
        z_index="6",
        margin_bottom="1em"
) """