import reflex as rx 
from arsenal_de_odio_web.styles.styles import Size, Color
from arsenal_de_odio_web.components.link_icons import link #link_icon,
import arsenal_de_odio_web.url as url
# ME quede por aqui https://youtu.be/h8Tn0ITRoQs?si=q-yUYV-8gr-oEMLk&t=4207

def navbar() -> rx.Component:
    return rx.container(
        rx.hstack(
                rx.center(
                link(
                    url.BANDCAMP, #TODO cambiar por los links correctos
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
                    width="35%", 
                    height="35%"
                ),
                link(
                    url.FACEBOOK,
                    "FACEBOOK",
                    "left",
                ),
                link(
                    url.INSTAGRAM,
                    "INSTAGRAM",
                    "left",
                ),
                link(
                    url.BANDCAMP,
                    "BADNCAMP",
                    "left",
                ),
                flex_direction=["column", "column", "column", "row", "row"], #TODO Responsive, cambiar los  nombres, por iconos al detectar que se trata de un dispositivo movil 
                #?ENCONTRE UNA POISBLE SOLUCION AQUI https://youtu.be/h8Tn0ITRoQs?si=TEXvWLFatM8urvGf&t=7046
                #rx.mobie_only()
            ),
            
        ),
        position="sticky",
        padding_top=Size.MEDIUM.value,
        center_content=True,
        # ? estoy en duda si fija la barrar de navegacion o no
        z_index="999",
        top="0",
    )