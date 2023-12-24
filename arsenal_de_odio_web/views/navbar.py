import reflex as rx 
from arsenal_de_odio_web.styles.styles import Size, Color
from arsenal_de_odio_web.components.link_icons import link #link_icon,
import arsenal_de_odio_web.url as url
from arsenal_de_odio_web.components.icons import icon, icon_rojo
# ME quede por aqui https://youtu.be/h8Tn0ITRoQs?si=q-yUYV-8gr-oEMLk&t=4207

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.center(
            link(
                url.BANDCAMP, #TODO Hacer una pagina aparte para todos los links de las diferentes plataformas de streaming
                "MUSICA",
                "right"
                ),
            link(
                url.FACEBOOK,
                "VIDEOS",
                "right"  
            ),
            link(
                url.INSTAGRAM,
                "HISTORIA",
                "right"
            ),
            rx.image(# TODO poner una url que al hacerle click al logo me lleve al inicio de la pagina 
                src="logo_arsenal.png", 
                alt="Logo de la banda Arsenal de Odio", 
                margin_top=Size.VERY_SMALL.value,
                width="14%", 
                height="14%"
            ),
            rx.hstack(
                link(
                    url.FACEBOOK,
                    "FACEBOOK",
                    "left",
                ),
            rx.center(
                icon_rojo(
                    url.FACEBOOK,
                    "facebook",
                    ),
                ),        
            ),
            rx.hstack(
                link(
                    url.INSTAGRAM,
                    "INSTAGRAM",
                    "left",
                ),
            rx.center(
                icon_rojo(
                    url.INSTAGRAM,
                    "instagram",
                    ),
                ),        
            ),
            flex_direction=["column", "column", "column", "row", "row"], #TODO Responsive, cambiar los  nombres, por iconos al detectar que se trata de un dispositivo movil 
            #?ENCONTRE UNA POISBLE SOLUCION AQUI https://youtu.be/h8Tn0ITRoQs?si=TEXvWLFatM8urvGf&t=7046
            #rx.mobie_only()
            width="100%",
        ),
        width="100%"
    ),
    position="sticky",
    bg=Color.SECONDARY.value,
    padding_x=Size.BIG.value, # El padding es el espacio que hay entre el borde y el texto
    padding_y=Size.VERY_SMALL.value,
    padding_top=Size.ZERO.value,
    # ? estoy en duda si fija la barrar de navegacion o no
    # z_index="999",
    # top="0",
    width="100%"
)