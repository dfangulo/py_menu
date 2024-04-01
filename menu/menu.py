import importlib.machinery
from .relative_path import resource_path
from .option_menu import OptionMenu
from .page_menu import PageMenu
from .view_menu import ViewMenu

"""
Desarrollado por: David Angulo
Colaborador: ChatGPT 3.5, free
Modulo para crear un menu sencillo
con una minima configuración.
"""


class Menu:
    view_menu = ViewMenu()
    menu_dict: dict = {}
    current_menu: dict[str | list[str]] = None
    before_menu: dict[str | list[str]] = None
    functions: dict = {}

    def run(self) -> None:
        while True:
            try:
                user_input = self.user_input()
                if user_input == "quit":
                    print("Salir del sistema")
                    break
                elif user_input == "return":
                    self.set_menu(menu=self.before_menu)
                else:
                    try:
                        if self.call_func(user_input) is None:
                            for page in self.menu_dict.items():
                                if page[0] == user_input:
                                    self.set_menu(menu=self.get_menu(user_input))
                    except Exception as e:
                        print(f"menu.run error: {str(e)}")
                        input()

            except ValueError:
                print("introduzca un valor correcto")
                input("Enter para continuar")

    def add_page(
        self, new_page: str, header: str, footer: str, options: list[tuple]
    ) -> None:
        new_option: str = None
        if self.menu_dict.get(new_page) is not None:
            self.menu_dict[new_page] = {}
        self.menu_dict[new_page] = PageMenu(
            header=header,
            footer=footer,
            options=[
                OptionMenu(index + 1, option[0], option[1])
                for index, option in enumerate(options)
            ],
        )
        if new_page == "main_menu":
            new_option = OptionMenu(
                len(self.menu_dict[new_page].options) + 1, "quit", "Cerrar Aplicación!"
            )
            self.set_menu(menu=self.get_menu(new_page))
        elif new_page == "login_menu":
            new_option = OptionMenu(
                len(self.menu_dict[new_page].options) + 1, "quit", "Cerrar Aplicación!"
            )
            self.set_menu(menu=self.get_menu(new_page))
        else:
            new_option = OptionMenu(
                len(self.menu_dict[new_page].options) + 1, "return", "Regresar!"
            )
        self.menu_dict[new_page].options.append(new_option)

    # Define una función para agregar las páginas al menú
    def add_pages_to_menu(self, pages):
        for page, data in pages.items():
            self.add_page(
                new_page=page,
                header=data["header"],
                footer=data["footer"],
                options=data["options"],
            )

    def user_input(self) -> str:
        while True:
            try:
                self.view_menu.display()
                user_entry = input("Seleciona una opción de la lista: ")
                for option in self.view_menu.options:
                    if int(user_entry) == option.user_input:
                        return option.user_function
            except ValueError:
                print("Introduzca un valor valido")
                input("Enter para continuar")

    def set_menu(self, menu: object) -> None:
        self.before_menu = (
            self.current_menu
            if self.before_menu != self.current_menu
            else self.before_menu
        )
        self.current_menu = menu
        self.view_menu.set_menu_options(menu)

    def get_menu(self, page_name: str) -> PageMenu:
        if self.menu_dict[page_name]:
            return self.menu_dict[page_name]
        else:
            print(f"No existe el menu {page_name}")

    def call_func(self, func_name) -> None:
        # Busca la función por su nombre en el diccionario de funciones
        func = self.functions.get(func_name)
        # Verifica si la función existe y es callable
        if func and callable(func):
            func()

    def set_func(self, functions) -> None:
        self.functions = functions

    def load_functions(self, functions_path) -> None:
        loader = importlib.machinery.SourceFileLoader(
            "functions", resource_path(functions_path)
        )
        functions_module = loader.load_module()

        functions = {}
        for name in dir(functions_module):
            attr = getattr(functions_module, name)
            if callable(attr):
                functions[name] = attr
        self.functions = functions
