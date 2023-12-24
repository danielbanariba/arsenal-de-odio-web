import reflex as rx
from arsenal_de_odio_web.styles.styles import Size, Color
import arsenal_de_odio_web.styles.styles as styles

def mercaderia() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.text(
                "MERCADERIA",
            ),
            padding_top=Size.DEFAULT.value,
            font_size=Size.VERY_BIG.value,
            color = Color.SECONDARY.value,
        ),
        rx.hstack(
            rx.center(
                rx.image(
                    src="img/camisa_ejemplo.png",
                    width="30%",
                    height="auto",
                ),
                rx.image(
                    src="img/cd.png",
                    width="30%",
                    height="auto",
                ),
            ),
            padding_top=Size.BIG.value,
            padding_bottom=Size.BIG.value,
        ),
        bg_img="img/arsenal_blanc_negro.jpg",
        bg_position = "top",
        bg_repeat = "no-repeat",
        bg_attachment = "scroll",  # Cambia esto #TODO estoy indeciso si dejarlo asi o poner el fixed 
        bg_size = "cover",
        width="100%",
    )