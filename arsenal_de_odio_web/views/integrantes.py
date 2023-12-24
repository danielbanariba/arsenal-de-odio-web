import reflex as rx
import arsenal_de_odio_web.styles.styles as styles
import arsenal_de_odio_web.url as URL
from arsenal_de_odio_web.components.link_integrantes import button_integrantes
from arsenal_de_odio_web.components.icons import icon

def integrantes() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.box(
                button_integrantes(
                    "integrantes/9.jpg",
                    "Emerson Guevara",
                ),
                rx.center(
                    icon(
                        URL.GUITARRISTA_PRINCIPAL_FACEBOOK,
                        "facebook"
                    ),
                    icon(
                        URL.GUITARRISTA_PRINCIPAL_YOUTUBE,
                        "tiktok"
                    ),
                ),
            ),
            rx.box(
                button_integrantes(
                    "integrantes/8.jpg",
                    "Oscar Osorto",
                ),
                rx.center(
                    icon(
                        URL.VOCALISTA_FACEBOOK,
                        "facebook"
                    ),
                ),
            ),
            rx.box(
                button_integrantes(
                    "integrantes/10.jpg",
                    "Gerardo Irias",
                ),
                rx.center(
                    icon(
                        URL.BATERISTA_FACEBOOK,
                        "facebook"
                    ),
                ),
            ),
            rx.box(
                button_integrantes(
                    "integrantes/11.jpg",
                    "Saddy Rueda", 
                ),
                rx.center(
                    icon(
                        URL.BAJISTA_FACEBOOK,
                        "facebook"
                    ),
                ), 
            ),
            rx.box(
                button_integrantes(
                    "integrantes/12.jpg",
                    "Marco Rodriguez",
                ),
                rx.center(
                    icon(
                        URL.GUITARRISTA_SECUNDARIO_FACEBOOK,
                        "facebook"
                    ),
                ),
            ),
            width="100%",
        ),
    )