import reflex as rx

from arsenal_de_odio_web.styles.styles import Size 

def list_song() -> rx.Component:
    return rx.vstack(
        # rx.box(
        #     rx.text(
        #         "Aqui va a ir una descripcion del album de la banda, y todo lo que se va a tratar del disco"
        #     ),
        #     rx.text(
        #         "Mas detalles del disco como el año de lanzamiento, el genero, etc."
        #     ),   
        #     align_items="start",# Hace todo el texto para la izquierda
        #     margin_left=Size.DEFAULT.value,
        # ),
        rx.box(
            rx.vstack(
                rx.spacer(),
                rx.text("01. Cathrashers"),
                rx.spacer(),
                rx.text("02. Con Derecho a Muerte"),
                rx.spacer(),
                rx.text("03. Puños de Furia"),
                rx.spacer(),
                rx.text("04. Asesinos"),
                rx.spacer(),
                rx.text("05. Arsenal Ataca"),
                rx.spacer(),
                rx.text("06. Pisemos Pues"),
                rx.spacer(),
                rx.text("07. Larga Vida al Metal"),
                rx.spacer(),
                rx.text("08. Arsenal de Odio"),
                rx.spacer(),
                rx.text("09. Muerte en el Mosh"),
                rx.spacer(),
                rx.text("10. Siente el Fuego"),
            ),
            center_content=True,
            text_align= "center",
            font_size = Size.LARGE.value,
        ),
    )