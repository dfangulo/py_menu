from dataclasses import dataclass


@dataclass
class OptionMenu:
    """
    Descripcion: Aqui se introducen las opciones que apareceran en nustra pagina de menú

        -   user_input: Lo que se espera que introduzca el usuario.
        -   user_function: La función que se debe de llamar
        -   user_display: Lo que va a decir el menu
    """
    user_input: int
    user_function: str
    user_display: str