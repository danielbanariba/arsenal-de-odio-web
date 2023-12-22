import reflex as rx
from arsenal_de_odio_web.styles.styles import Size 

def video() -> rx.Component:
    return rx.video(
        url="/arsenal_video.mp4",
        width="auto",
        height="auto",
        padding_bottom=Size.DEFAULT.value,
    )