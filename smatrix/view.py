"""View."""
from dataclasses import dataclass
import tkinter as tk
from .type_widget import TypeWidget
from .max_df_widget import MaxDfWidget


@dataclass
class View(tk.Frame):
    typew: tk.LabelFrame = TypeWidget()
    maxdfw: tk.Frame = MaxDfWidget()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        options = {"padx": 20}
        self.typew.pack(anchor="nw", **options)
        self.maxdfw.pack(anchor="nw", **options)
