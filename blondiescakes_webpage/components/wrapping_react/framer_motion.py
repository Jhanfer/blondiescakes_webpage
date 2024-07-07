from reflex.components.component import Component
from typing import Any, Dict, List, Union, Callable, Literal
from reflex.vars import Var



class FramerMotion(Component):
    library="framer-motion@12.0.0-alpha.0"
    tag="motion.div"
    
    
    animate:Var[dict[str,Union[float,str,list[float]]]]
    initial:Var[dict[str,Union[float,str,list[float]]]]
    transition:Var[dict[str,Union[float,str,list[float]]]]

    drag:Var[Union[str,list[str]]]
    while_hover:Var[dict[str,Union[float,str,list[float]]]]
    while_tap:Var[dict[str,Union[float,str,list[float]]]]
    while_in_view:Var[dict[str,Union[float,str,list[float]]]]
    while_focus:Var[dict[str,Union[float,str,list[float]]]]
    viewport:Var[Union[str,list[str]]]
    exit:Var[dict[str,Union[float,str,list[float]]]]


motion = FramerMotion.create





class FramerMotionSVG(Component):
    library="framer-motion@12.0.0-alpha.0"
    tag="motion.svg"
    
    
    animate:Var[Union[str,dict[str,Union[float,str,list[float]]]]]
    initial:Var[Union[str,dict[str,Union[float,str,list[float]]]]]
    viewbox:Var[list[int]]

    transition:Var[dict[str,Union[float,str,list[float]]]]
    drag:Var[Union[str,list[str]]]
    while_hover:Var[dict[str,Union[float,str,list[float]]]]
    while_tap:Var[dict[str,Union[float,str,list[float]]]]
    while_in_view:Var[dict[str,Union[float,str,list[float]]]]
    while_focus:Var[dict[str,Union[float,str,list[float]]]]
    viewport:Var[Union[str,list[str]]]
    exit:Var[dict[str,Union[float,str,list[float]]]]


motion_svg = FramerMotionSVG.create





class FramerMotionLine(Component):
    library="framer-motion@12.0.0-alpha.0"
    tag="motion.line"
    
    
    animate:Var[dict[str,Union[float,str,list[float]]]]
    initial:Var[dict[str,Union[float,str,list[float]]]]
    transition:Var[dict[str,Union[float,str,list[float]]]]

    x1:Var[str]
    x2:Var[str]
    y1:Var[str]
    y2:Var[str]
    stroke:Var[str]
    variants:Var[Union[str,dict[str,Union[float,str,list[float]]]]]
    custom:Var[int]
    
    drag:Var[Union[str,list[str]]]
    while_hover:Var[dict[str,Union[float,str,list[float]]]]
    while_tap:Var[dict[str,Union[float,str,list[float]]]]
    while_in_view:Var[dict[str,Union[float,str,list[float]]]]
    while_focus:Var[dict[str,Union[float,str,list[float]]]]
    viewport:Var[Union[str,list[str]]]
    exit:Var[dict[str,Union[float,str,list[float]]]]


motion_line = FramerMotionLine.create







class FramerMotion3D(Component):
    library="framer-motion-3d@11.2.0"
    tag="motion3d"
    lib_dependencies:list[str] = ["three@0.137.0","@react-three/fiber@8.2.2"]

    animate:Var[dict[str,Union[float,str,list[float]]]]
    initial:Var[dict[str,Union[float,str,list[float]]]]
    transition:Var[dict[str,Union[float,str,list[float]]]]

    drag:Var[Union[str,list[str]]]
    while_hover:Var[dict[str,Union[float,str,list[float]]]]
    while_tap:Var[dict[str,Union[float,str,list[float]]]]
    while_in_view:Var[dict[str,Union[float,str,list[float]]]]
    while_focus:Var[dict[str,Union[float,str,list[float]]]]
    viewport:Var[Union[str,list[str]]]
    exit:Var[dict[str,Union[float,str,list[float]]]]


motion_3D = FramerMotion3D.create