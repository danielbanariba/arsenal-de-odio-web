import reflex as rx
import arsenal_de_odio_web.styles.styles as styles
import arsenal_de_odio_web.url as URL
from arsenal_de_odio_web.components.link_integrantes import button_integrantes
from arsenal_de_odio_web.components.icons import icon
from arsenal_de_odio_web.styles.styles import Size, Color
import arsenal_de_odio_web.styles.const as view

def integrantes() -> rx.Component:
    return rx.vstack(
        rx.center(# responsive, apila cada uno encima del otro cuando detecta que la pantalla es pequeña
            rx.responsive_grid(
                rx.box(
                    button_integrantes(
                        "integrantes/9.jpg",
                        "Emerson Guevara",
                    ),
                    rx.center(# da un espacio entro los iconos
                        rx.hstack(
                            icon(
                                URL.GUITARRISTA_PRINCIPAL_FACEBOOK,
                                "facebook",
                                Size.BIG.value,
                                Color.SECONDARY.value,
                                view.viewBox_0
                            ),
                            icon(
                                URL.GUITARRISTA_PRINCIPAL_INSTAGRAM,
                                "instagram",
                                Size.BIG.value,
                                Color.SECONDARY.value,
                                view.viewBox_0
                            ),
                            spacing=Size.SMALL.value,    
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
                            "facebook",
                            Size.BIG.value,
                            Color.SECONDARY.value,
                            view.viewBox_0
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
                            "facebook",
                            Size.BIG.value,
                            Color.SECONDARY.value,
                            view.viewBox_0
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
                            "facebook",
                            Size.BIG.value,
                            Color.SECONDARY.value,
                            view.viewBox_0
                        ),
                    ), 
                ),    
                rx.box(
                    button_integrantes(
                        "integrantes/12.jpg",
                        "Marco Rodriguez",
                    ),
                    rx.center(
                        icon(URL.GUITARRISTA_SECUNDARIO_FACEBOOK,
                            "facebook",
                            Size.BIG.value,
                            Color.SECONDARY.value,
                            view.viewBox_0
                        ),
                    ),
                ),
            columns=[1, 2, 3, 4, 5],
            spacing="6",
        ),
    ),
    width="100%",
)