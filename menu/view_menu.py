import os


class ViewMenu:
    header: str = None
    footer: str = None
    options: list[object] = None
    max_line_size_menu = 10
    max_col_size_menu = 40

    def set_menu_options(self, page: object) -> None:
        self.header = page.header
        self.footer = page.footer
        self.options = page.options
        # Ajustar el tamaño maximo
        self.update_size_menu(len(self.header) + 2)
        self.update_size_menu(len(self.footer) + 2)
        for option in self.options:
            self.update_size_menu(len(option.user_display) + 9)
        self.display()

    def update_size_menu(self, size: int) -> None:
        self.max_col_size_menu = (
            size if size > self.max_col_size_menu else self.max_col_size_menu
        )

    def display(self) -> None:
        os.system("cls")
        line = (self.max_col_size_menu) * "─"
        header = "┌" + line + "┐"
        separator = "├" + line + "┤"
        footer = "└" + line + "┘\n"
        blank_space = "│" + len(line) * " " + "│"
        spaces: int = round(self.max_line_size_menu / 2) - round(len(self.options) / 2)
        print(header)
        print("│", self.header.center(self.max_col_size_menu - 2), "│")
        print(separator)
        for _ in range(spaces):
            print(blank_space)
        for option in self.options:
            option_line = f" {option.user_input} => {option.user_display}"
            print(
                "│",
                option_line,
                (self.max_col_size_menu - len(option_line) - 3) * " ",
                "│",
            )
        for _ in range(self.max_line_size_menu - (spaces + len(self.options))):
            print(blank_space)
        print(separator)
        print("│", self.footer.center(self.max_col_size_menu - 2), "│")
        print(footer)
