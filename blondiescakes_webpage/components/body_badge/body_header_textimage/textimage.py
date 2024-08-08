import reflex as rx
from blondiescakes_webpage.styles import styles as st
from typing import Optional
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion


def textimage_header(image:str,text:str,color:Optional[str]=st.ColorPalette.ENFASIS.value,size:Optional[str]="6") -> rx.Component:
        return rx.vstack(

                rx.box(
                        header_letters("4em",color),
                align="center",
                justify="center",
                position="absolute",
                z_index="100",
                top="-5em",
                display=["flex", "flex", "none", "none", "none"],
                ),

                rx.box(
                        header_letters("5em",color),
                align="center",
                justify="center",
                position="absolute",
                z_index="100",
                top="-5em",
                display=["none", "none", "flex", "flex", "flex"],
                ),
                

                motion(
                        rx.flex(
                                rx.image(
                                        src=image,
                                        width="22em",
                                        max_width="28em",
                                        height="auto",
                                        position="relative",
                                        border_radius="70px 70px",
                                        object_fit="cover",
                                        top="3em",
                                        display=["flex", "flex", "none", "none", "none"],
                                ),

                                
                                rx.image(
                                        src=image,
                                        width="30em",
                                        max_width="30em",
                                        height="auto",
                                        position="relative",
                                        border_radius="70px 70px",
                                        object_fit="cover",
                                        top="3em",
                                        display=["none", "none", "flex", "flex", "flex"],
                                ),
                        ),
                        initial={"opacity":0,"y":100},
                        animate={"opacity":1,"y":0},
                        transition={"delay":0.1,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                ),
                align="center",
                justify="center"
        )





def header_letters(size:str, color:str) -> rx.Component:
        return rx.vstack(
                        motion(        
                                        rx.flex(
                                                rx.heading("Regala",
                                                        color=color,
                                                        style={f"font-size": size},
                                                        position="relative",
                                                ),
                                        ),
                                initial={"opacity":0.5,"x":100},
                                animate={"opacity":1,"x":0},
                                tansition={"delay":10,"type":"spring","duration":3,"stiffness": 260, "damping": 0,"ease":"linear"}
                        ),
                        
                        motion(
                                        rx.flex(
                                                rx.heading("Amor,",
                                                        
                                                        color=color,
                                                        style={f"font-size": size},
                                                ),
                                        ),
                                initial={"opacity":0.5,"x":100},
                                animate={"opacity":1,"x":0},
                                tansition={"delay":0.3,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                        ),

                        motion(
                                        rx.flex(
                                                rx.heading("Regala",
                                                        
                                                        color=color,
                                                        style={f"font-size": size},
                                                ),
                                        ),
                                initial={"opacity":0.5,"x":100},
                                animate={"opacity":1,"x":0},
                                tansition={"delay":0.3,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                        ),

                        motion(
                                        rx.flex(
                                                rx.heading("Dulce.",
                                                        
                                                        color=color,
                                                        style={f"font-size": size},
                                                ),
                                        ),
                                initial={"opacity":0.5,"x":100},
                                animate={"opacity":1,"x":0},
                                tansition={"delay":1,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                        ),
                spacing="7"
                ),