import reflex as rx
from arsenal_de_odio_web.styles.styles import Size

# def link_icon(image: str, url: str, alt: str) -> rx.Component:
#     return rx.link(
#         rx.text(
#             alt,
#             font_size=Size.BIG.value,
#         ),
#         rx.center(
#             rx.image(
#                 src=image,
#                 width=Size.VERY_BIG.value,
#                 height=Size.VERY_BIG.value,
#                 alt=alt,
#             ),
#         ),
#         href=url,
#         is_external=True
#         #padding=Size.VERY_BIG.value,
#     )
    
def link(url: str, alt: str, margin_side: str) -> rx.Component:
    style = {
        "margin_{}".format(margin_side): Size.DEFAULT.value
    }
    return rx.link(
        rx.text(
            alt,
            font_size=Size.BIG.value,
            style=style
        ),
        href=url,
        is_external=True
    )