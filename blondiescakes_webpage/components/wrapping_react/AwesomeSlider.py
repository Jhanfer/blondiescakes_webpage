from reflex.components.component import Component
from typing import Any, Dict, List, Union, Callable
from reflex.vars import Var

class Carousel(Component):

    library="react-awesome-slider"
    tag="AwesomeSlider"
    is_default=True

    

    width:Var[str]
    height:Var[str]
    
    name:Var[str]
    selected:Var[Union[str,int,float]]
    bullets:Var[bool]
    organic_arrows:Var[bool]
    fill_parent:Var[bool]
    infinite:Var[bool]=True
    transition_delay:Var[Union[int,float,str]]
    mobile_touch:Var[bool]=True
    buttons:Var[bool]=True
    on_first_mount:Var[Callable]
    on_transition_end:Var[Callable]
    on_transition_start:Var[Callable]
    on_transition_request:Var[Callable]
    animation:Var[str]
    slider_transition_duration:Var[Union[str,int,float]]


    slider_height_percentage:Var[str]
    organic_arrow_thickness:Var[str]
    organic_arrow_border_radius:Var[str]
    organic_arrow_height:Var[str]
    organic_arrow_color:Var[str]
    control_button_width:Var[str]
    control_button_height:Var[str]
    control_button_background:Var[str]
    control_bullet_color:Var[str]
    control_bullet_active_color:Var[str]

    loader_bar_color:Var[str]
    loader_bar_height:Var[str]

    content_background_color:Var[str]

    """usinng "_get_custom_code" we can import from js line as bellow"""
    def _get_custom_code(self) -> str | None:
        return """
                import 'react-awesome-slider/dist/styles.css';
                import 'react-awesome-slider/src/styled/fold-out-animation/fold-out-animation.scss';
                import 'react-awesome-slider/src/styled/cube-animation/cube-animation.scss';
                import 'react-awesome-slider/src/styled/fall-animation/fall-animation.scss';
                import 'react-awesome-slider/src/styled/scale-out-animation/scale-out-animation.scss';
                import 'react-awesome-slider/src/styled/open-animation/open-animation.scss';
                """
    

carousel=Carousel.create

