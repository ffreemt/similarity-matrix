"""Define TypeWidget for tf_ idf_ dl_ norm widget."""
from typing import List
import tkinter as tk
from tkinter import ttk

from rich import inspect
from logzero import logger


class TypeWidget(tk.LabelFrame):
    """Define typeWidget for tf_ idf_ dl_ norm widget."""

    def __init__(self, parent=None, *args, type_list: List = None, **kwargs):
        """Init.

        Arguments:
            text: labelframe title
            type_list: values for the radiobutton
        Returns
            a label frame packed with radiobuttons

        self: tk.LabelFrame
        make_widget: make it happen
        """
        super().__init__(parent, *args, **kwargs)

        # setup initial radiobutton state
        if type_list is None:
            self.type_list = ["type1", "type2"]
        else:
            self.type_list = type_list  # type: List
        self.var = tk.StringVar()
        if self.type_list:
            self.var.set(self.type_list[0])

        self.make_widget()

    def create_radio(self, option: str):
        """Make a radiobutton."""
        text, value = option, option
        return tk.Radiobutton(
            self, text=text, value=value, command=self.print_option, variable=self.var
        )

    def print_option(self):
        """Fake callback."""
        logger.debug("""self.cget("text"): %s, self.var.get(): %s""", self.cget("text"), self.var.get())

    def make_widget(self):
        """Layout the widget based on label and types."""
        # self.buttons = [self.create_radio(c) for c in COLORS]
        for type_ in self.type_list:
            button = self.create_radio(type_)
            button.pack(side=tk.LEFT, anchor=tk.W, padx=5, pady=5)

    def quit(self, evt=None):
        logger.debug(evt)
        # self.destroy()
        self.winfo_toplevel().destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.bind("<Escape>", lambda evt: inspect(evt) or print(evt) or root.destroy(), add="+")  # type: ignore

    widget = TypeWidget(
        root, text="tf_type", type_list=["linear", "sqrt"]  # LabelFrame's label
    )
    # root.bind("<Escape>", widget.quit, add="+")  # type: ignore

    widget1 = TypeWidget(
        root, text="tf_type1", type_list=["linear", "sqrt"]  # LabelFrame's label
    )

    widget.pack()
    widget1.pack()


    root.mainloop()
