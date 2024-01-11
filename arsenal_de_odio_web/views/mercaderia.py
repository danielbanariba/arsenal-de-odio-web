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
        rx.center(
            rx.responsive_grid(
                producto("img/merch/camisa_hada_de_las_birrias.png", 
                         "CAMISA DEL HADA DE LAS BIRRIAS", 
                         "L. 350.00"),
                producto("img/merch/cd2.png", 
                         "CD - MUERTE EN EL MOSH", 
                         "L. 450.00"),
                columns=[1, 1, 1, 2],#ALV, esto es oro para lo responsive
                spacing="6",
            ),
            width="100%",
            padding=Size.BIG.value,
        ),
        bg_img="img/arsenal_blanc_negro.jpg",
        bg_position = "top",
        bg_repeat = "no-repeat",
        bg_attachment = "scroll", #TODO estoy indeciso si dejarlo asi o poner el fixed 
        bg_size = "cover",
        width="100%",
        id="mercaderia",
        spacing=Size.BIG.value,
    )