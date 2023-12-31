import reflex as rx 

def grain() -> rx.Component:
    return rx.vstack(
        padding_top="0px",
        margin_top="0px",
        id="grain", #Efecto de ruido
    )