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
            ),
        ),
        padding_top=Size.BIG.value,
        center_content=True,
    )





# rx.vstack( #TODO poner botones a los lados del logo
#         rx.center(
#             rx.hstack(
#                 rx.hstack(
#                     link(
#                         url.BANDCAMP, #TODO cambiar por los links correctos
#                         "MUSICA",
#                     ),    
#                     link(
#                         url.FACEBOOK,
#                         "VIDEOS",  
#                     ),
#                     link(
#                         url.INSTAGRAM,
#                         "HISTORIA",
#                     ),
#                     spacing=Size.VERY_BIG.value,
#                 ),
#                 rx.center(#Centra el logo en el navbar
#                     rx.image(
#                         src="logo_arsenal.png",
#                         alt="Logo de la banda Arsenal de Odio",
#                         width="55%",
#                         height="55%",
#                     ),
#                 ),  
#                 rx.spacer(),
#                 rx.hstack(# Pinta los botones de las redes sociales
#                     link_icon(
#                     "icons/facebook.svg",
#                     url.FACEBOOK,
#                     "FACEBOOK"
#                     ),
#                     link_icon(
#                         "icons/instagram.svg",
#                         url.INSTAGRAM,
#                         "INSTAGRAM"
#                     ),
#                     link_icon(
#                         "icons/bandcamp.svg",
#                         url.BANDCAMP,
#                         "BADNCAMP"
#                     ),
#                     spacing=Size.VERY_BIG.value,
#                 ),
#                 width="100%",
#             ),
#         ),

#     )