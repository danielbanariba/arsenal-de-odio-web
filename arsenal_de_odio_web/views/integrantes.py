import reflex as rx
import arsenal_de_odio_web.styles.styles as styles
import arsenal_de_odio_web.url as URL
from arsenal_de_odio_web.components.link_integrantes import button_integrantes

def integrantes() -> rx.Component:
    return rx.center(
        rx.hstack(
            button_integrantes(
                "integrantes/9.jpg",
                "Emerson Guevara",
                URL.GUITARRISTA_PRINCIPAL_FACEBOOK,
            ),
            button_integrantes(
                "integrantes/8.jpg",
                "Oscar Osorto",
                URL.VOCALISTA_FACEBOOK,
            ),
            button_integrantes(
                "integrantes/10.jpg",
                "Gerardo Irias",
                URL.BATERISTA_FACEBOOK,
            ),
            button_integrantes(
                "integrantes/11.jpg",
                "Saddy Rueda",
                URL.BAJISTA_FACEBOOK,    
            ),
            button_integrantes(
                "integrantes/12.jpg",
                "Marco Rodriguez",
                URL.GUITARRISTA_SECUNDARIO_FACEBOOK,
            ),
            width="100%",
        )
    )