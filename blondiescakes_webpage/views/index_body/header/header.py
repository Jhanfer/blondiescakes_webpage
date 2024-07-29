import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_header_textimage.textimage import textimage_header
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion


def header() -> rx.Component:
    return rx.flex(
                    rx.hstack(
                            rx.spacer(),
                            motion(
                                    rx.flex(
                                        rx.image(src="/header/back.svg",width="15em",height="auto"),
                                        rx.text("PASTELERÍA A LA CARTA",
                                                color=st.ColorPalette.ENFASIS.value,
                                                padding_left="1.7em",
                                                padding_top="2em",
                                                position="absolute"
                                        ),
                                    ),
                                initial={"opacity":0,"x":-50},
                                animate={"opacity":1,"x":0},
                                transition={"delay":0.1,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                            ),
                        padding_bottom="5em",
                        justify="between",
                        spacing="9",
                        display="flex",
                        position="relative",
                        z_index="5",
                        width="100%",
                        align="center",  
                    ),

            rx.hstack(
                    motion(         
                            motion(        
                                    rx.flex(
                                            rx.link(
                                                    rx.text("@BLONDIES_CAKE",
                                                        color=st.ColorPalette.ENFASIS.value,
                                                        position="relative",
                                                        size="3",
                                                        align="center",
                                                        
                                                    ),
                                                href="https://www.instagram.com/blondies_cake/"
                                            ),
                                            rx.icon(
                                                tag="instagram",
                                                position="relative",
                                                width="1.09em",
                                                height="auto",
                                                color=st.ColorPalette.ENFASIS.value,
                                                top="-0.1em"
                                            ),
                                            
                                        justify="start",
                                        align_items="center",
                                        spacing="4",
                                        display="flex",
                                        class_name="vertical-text",
                                        z_index="101"
                                    ),
                                
                                initial={"opacity":0,"y":-50},
                                animate={"opacity":1,"y":0},
                                transition={"delay":0.1,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                            ),
                        z_index="101",
                        position="absolute",
                        top="25em",
                        #top="30em",
                        left="-3em",
                        #left="1em",
                        while_hover={"scale":1.1},
                        while_tap={"scale":0.8},
                        transition={"type":"spring","stiffness":260,"damping":10}
                    ),
                    textimage_header("header/header.jpeg","Regala amor, regala dulce",size="9"),
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
        padding_top="8em",
        width="100%",
        spacing="5",
        direction="column",
        padding_bottom="10em",
        

    )


