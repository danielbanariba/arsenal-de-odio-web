import reflex as rx 
import arsenal_de_odio_web.styles.styles as styles
from arsenal_de_odio_web.styles.styles import Size as size
from arsenal_de_odio_web.styles.styles import Size, Color

def button_integrantes(image: str, nombre: str) -> rx.Component:
    return rx.box(
        rx.avatar(
            name=nombre,
            src=image,
            size="9",
            bg=Color.PRIMARY.value, # ? Fondo del avatar
            border="4px",
            border_color=Color.SECONDARY.value,
            margin_right=size.SMALL.value,
            margin_left=size.SMALL.value,
            box_shadow = "7px 7px 10px rgba(0, 0, 0, 0.9)"#sombra
        ),
        rx.center( 
            rx.text(
                nombre,
                font_size=size.LARGE.value,
                padding_y=size.VERY_SMALL.value,
            ),    
        ),
    )