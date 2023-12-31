import reflex as rx 

def reproductor_spotify() -> rx.Component:
    return rx.box(  
    rx.html(
            """
                <iframe style="border-radius:12px" 
                    src="https://open.spotify.com/embed/artist/5eEqNJZFQBKgTL0mcnQ2iA?utm_source=generator&theme=0" width="100%" height="420" 
                    frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media;   
                    fullscreen; picture-in-picture" loading="lazy">
                </iframe>
            """
        ),
        width="100%",
        align_items="center",
    )
