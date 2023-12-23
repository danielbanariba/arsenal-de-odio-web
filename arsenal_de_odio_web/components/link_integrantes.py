import reflex as rx 
import arsenal_de_odio_web.styles.styles as styles
from arsenal_de_odio_web.styles.styles import Size as size
from arsenal_de_odio_web.styles.styles import Size, Color

def button_integrantes(image: str, nombre: str, url: str) -> rx.Component:
    return rx.box(
        rx.avatar(#TODO No se si ponerle un avatar o la imagen 
            name=nombre,
            src=image,
            size="2xl",
            # TODO hacer varias combinaciones de colores hasta que empiece a quedar bien,
            bg=Color.PRIMARY.value, # ? Fondo del avatar
            border="4px",
            border_color=Color.SECONDARY.value,
            margin_right=size.SMALL.value,
            margin_left=size.SMALL.value,
        ),
        rx.center( 
            rx.text(
                nombre,
                font_size=size.LARGE.value,
            ),    
        ),
        rx.center(#! ERROR LOGICO
            rx.link(#TODO Me dirige a la misma pagina de arsenal y no a la pagina de facebook     
                rx.text(
                    nombre
                ),
                href=url,
                is_external=True
            ),   
        ),
    )