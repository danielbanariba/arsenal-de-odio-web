import reflex as rx 
from arsenal_de_odio_web.styles.styles import MAX_WIDTH , Size, Color
from arsenal_de_odio_web.components.link_icons import link, linkv2 #link_icon,
import arsenal_de_odio_web.url as url
from arsenal_de_odio_web.components.icons import iconv2
#TODO investigar porque al momento de desplegar en la pagina vercel no funciona el navbarv2
class DrawerState(rx.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)

def navbarv2() -> rx.Component:
    return rx.hstack(
    rx.box(
        rx.link(
            iconv2(
                "bars",
                Size.BIG.value,
                Color.PRIMARY.value,
                "0 0 512 512"
            ),
            on_click=DrawerState.right
        ),
        rx.drawer(
            rx.drawer_overlay(
                rx.drawer_content(
                    rx.drawer_header(
                        rx.link(
                            iconv2(
                                "close",
                                Size.BIG.value,
                                Color.PRIMARY.value,
                                "0 0 512 512"
                            ),
                            display="flex",
                            justify_content="flex-start",
                            on_click=DrawerState.right,
                        ),
                    ),
                    rx.drawer_body(
                        rx.box(#rx.drawer_body
                            rx.vstack(
                                linkv2(
                                    url.MUSICA, #TODO Hacer una pagina aparte para todos los links de las diferentes plataformas de streaming
                                    "MUSICA",
                                    "right"
                                    ),
                                link(
                                    url.FACEBOOK,
                                    "VIDEOS",
                                    "right"  
                                ),
                                linkv2(
                                    url.MERCADERIA,
                                    "MERCADERIA",
                                    "right"
                                ),    
                            ),
                        ),
                        display="flex",
                        justify_content = "center",
                        align_items = "center",
                    ),
                    bg="rgba(0, 0, 0, 0.3)",
                )
            ),
            is_open=DrawerState.show_right,
        ),
    ),
    position="sticky",
    #padding_x=Size.VERY_SMALL.value,
    padding_top=Size.ZERO.value,
    #z_index="999",
    # top="0",
    width="100%",
)