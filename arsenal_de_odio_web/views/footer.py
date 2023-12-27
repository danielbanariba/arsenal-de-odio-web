import reflex as rx 
import datetime
import arsenal_de_odio_web.url as URL
import arsenal_de_odio_web.styles.styles as styles
from arsenal_de_odio_web.styles.styles import Size, Color, TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.link(# * Cuando empiece a crear las paginas web a las bandas amigas, lo que tengo planeado hacer es que poner el mismo footer en todas las paginas web, pero que el footer tenga un link a mi pagina web
            rx.box(
                rx.span(
                    """DANIEL\nBANARIBA""",
                    style=styles.logo_canal,
                ),
            ),
            href=URL.DANIEL_BANARIBA,
            is_external=True,
            _hover={"color": "#ffc435"},
            alt="Logotipo de DanielBanariba.",
        ),
        rx.span(
            rx.span(
                f" © 2023-{datetime.datetime.today().year}, ",
                font_size=Size.PEQUENIO.value,
            ),
            "TODOS LOS DERECHOS RESERVADOS.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_botoom=Size.BIG.value, # Para que se separare el texto de la parte de abajo
        padding_x=Size.BIG.value, # Responsive, se separe el texto de los lados
        spacing=Size.DEFAULT.value
    )