import reflex as rx
from arsenal_de_odio_web.styles.styles import MAX_WIDTH, Size, Color
import arsenal_de_odio_web.styles.styles as styles
from arsenal_de_odio_web.components.producto import producto

def mercaderia() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.text(
                "MERCADERIA",
            ),
            padding_top=Size.VERY_SMALL.value,
            font_size=Size.VERY_BIG.value,
            color = Color.SECONDARY.value,
        ),
        rx.hstack(
            rx.flex(
                rx.center(
                    producto(
                        imagen="img/camisa_ejemplo.png",
                        descripcion="CAMISA OFICAL DE ARSENAL DE ODIO",
                        precio="L. 450.00",
                    ),
                    margin_top=Size.BIG.value,
                    margin_bottom=Size.BIG.value,
                ),
                rx.spacer(),
                rx.center(
                    producto(
                        imagen="img/cd.png",
                        descripcion="CD OFICIAL DE ARSENAL DE ODIO - MUERTE EN EL MOSH",
                        precio="L. 200.00",
                    ),
                ),
                width="100%",
            ),
        ),
        bg_img="img/arsenal_blanc_negro.jpg",
        bg_position = "top",
        bg_repeat = "no-repeat",
        bg_attachment = "scroll", #TODO estoy indeciso si dejarlo asi o poner el fixed 
        bg_size = "cover",
        width="100%",
        # max_width=MAX_WIDTH, # quiero encerrar todo en la caja, pero no me deja xd 
    )