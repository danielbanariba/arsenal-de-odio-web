import reflex as rx

def hada () -> rx.Component:
    return rx.html(
        '''
            <head>
                <style>
                    @keyframes shakeAndScale {
                        0% { transform: translate(1px, 1px) rotate(0deg) scale(1); }
                        10% { transform: translate(-1px, -2px) rotate(-1deg) scale(1.05); }
                        20% { transform: translate(-3px, 0px) rotate(1deg) scale(1.1); }
                        30% { transform: translate(3px, 2px) rotate(0deg) scale(1.15); }
                        40% { transform: translate(1px, -1px) rotate(1deg) scale(1.2); }
                        50% { transform: translate(-1px, 2px) rotate(-1deg) scale(1.5); }
                        60% { transform: translate(-3px, 1px) rotate(0deg) scale(1.2); }
                        70% { transform: translate(3px, 1px) rotate(-1deg) scale(1.15); }
                        80% { transform: translate(-1px, -1px) rotate(1deg) scale(1.1); }
                        90% { transform: translate(1px, 2px) rotate(0deg) scale(1.05); }
                        100% { transform: translate(1px, -2px) rotate(-1deg) scale(1); }
                    }

                    #myImage {
                        position: absolute;
                        width: 5%;
                        height: 5%;
                        transition: top 2s ease-in-out, left 2s ease-in-out; /* Agregar transición */
                        animation: shakeAndScale 2s infinite; /* Agregar animación de temblor y escala */
                    }
                </style>
            </head>
            <body>
                <img id="myImage" src="img/el_hada_de_las_birrias.png" alt="My Image">
                <script>
                    function moveImage() {
                        var img = document.getElementById('myImage');
                        var x = Math.floor(Math.random() * window.innerWidth);
                        var y = Math.floor(Math.random() * window.innerHeight);
                        img.style.left = x + 'px';
                        img.style.top = y + 'px';
                    }
                    setInterval(moveImage, 2000); // Mueve la imagen cada 2 segundos
                </script>
            </body>
        '''
    )