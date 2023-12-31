import reflex as rx

def hada () -> rx.Component:
    return rx.html(
        '''
            <head>
                <style>
                    #myImage {
                        position: absolute;
                        width: 5%;
                        height: 5%;
                        transition: top 2s ease-in-out, left 2s ease-in-out; /* Agregar transición */
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