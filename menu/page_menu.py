from dataclasses import dataclass


@dataclass
class PageMenu:
    """
    Descripción: El armado de la pagina que va ser parte de nuestro Menú
        -   header, Texto que va ir como titulo de la pagina
        -   foooter, el texto en la parte de abajo de la pagina
        -   Lista de objetos para cada opción

    """
    header: str
    footer: str
    options: list[object]