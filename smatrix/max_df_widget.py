"""Define MaxDfWidget widget for max_df."""
from typing import List
import tkinter as tk
from tkinter import ttk

from rich import inspect
from logzero import logger


class MaxDfWidget(tk.Frame):
    """Define MaxDfWidget widget for max_df."""

    def __init__(self, parent=None, *args, **kwargs):
        """Init.

        Arguments:
            text: labelframe title?
        """
        super().__init__(parent, *args, **kwargs)

        # container self: tk.Frame
        self.var_spinbox = tk.DoubleVar(value=1)
        self.var_scale = tk.DoubleVar(value=500)
        self.var = tk.DoubleVar(value=1)

        self.frame_status = tk.Frame(self)
        self.statustext_var = tk.StringVar(value=f"max_df: {self.var.get()}")
        self.label_status = tk.Label(
            # self,
            self.frame_status,
            justify=tk.LEFT,
            textvariable=self.statustext_var,
            # width=50,  # chars
            # wraplength=250,
        )
        self.label_status.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

        # self.bind('<Configure>', lambda evt: self.config(wraplength=self.winfo_width()))
        # wrap dynamically
        _ = self.label_status.winfo_width()
        # _ = self.winfo_width()  # container width
        # _ = self.winfo_toplevel().winfo_width()  # container's parent width
        self.label_status.bind('<Configure>', lambda evt: self.label_status.config(wraplength=self.label_status.winfo_width()))

        # self.label_status.bind('<Configure>', lambda evt: self.label_status.config(wraplength=self.winfo_toplevel().winfo_width()))

        self.make_widget()

    def create_spinbox(self, show: bool = False, **kwargs):
        """Make a spinbox.

        Arguments
            from_, to, increment = 0, 1, 0.01
            show: display spinbox value, default False
        """
        frame = tk.Frame(self)

        # textvariable = tk.DoubleVar(value=1)
        textvariable = self.var_spinbox

        spinbox = tk.Spinbox(
            frame, textvariable=textvariable, from_=0,  to=1,
            increment=0.01,
            # command=self.print_option,
            # command=lambda: self.update_var(textvariable.get()) or self.print_option(),
            command=lambda: self.update_var(self.var_spinbox.get()) or self.print_option(),
            wrap=True,
            width=5,  # chars
        )
        spinbox.config(font=("Times", 18))

        label = tk.Label(
            frame, textvariable=textvariable,
            anchor=tk.CENTER,
        )

        spinbox.pack(side=tk.LEFT)
        label.pack(side=tk.LEFT)

        # spinbox.bind("<KeyRelease>", self.update_var)
        spinbox.bind("<KeyRelease>", lambda evt: self.update_var(self.var_spinbox.get()) or self.print_option())

        return frame

    def create_scale(self, from_=500, to=100000, resolution=500, **kwargs):
        """Make a scale.

        Arguments
            scale_list: default to 500, 500, 10000
        Returns
        """
        # if scale_list is None:
            # scale_list = [*range(500, 500, 10000)]

        return tk.Scale(
            self,
            from_=from_,
            resolution=resolution,
            to=to,
            variable=self.var_scale,
            # command=self.print_option,
            command=lambda evt: self.update_var(self.var_scale.get()) or self.print_option(),
            orient=tk.HORIZONTAL,
            **kwargs,
        )

    def make_widget(self):
        """Layout the widgets in self (tk.Frame): spinbox + scale + label.

        spinbox, scale
        label: explain meaning -- 0 or 1: all df, 0-1: max_df in percent; > 1: absolute
        """
        # container self: tk.Frame
        # self.create_spinbox().pack(side=tk.LEFT)
        # self.create_scale().pack(side=tk.LEFT)

        # defualt column=0, default row=the next higher-numbered unoccupied row
        self.create_spinbox().grid(column=0, row=0, sticky=tk.NSEW)
        self.create_scale().grid(column=1, row=0, sticky=tk.NSEW)

        # self.labe_status.grid(column=0, columnspan=2, row=1)
        # self.label_status.grid(columnspan=2, sticky=tk.NW)
        self.frame_status.grid(columnspan=2, sticky=tk.NW)

    def update_var(self, value: float):
        """Update self.var and self.statustext_var."""
        try:
            value = float(value)
            if value <= 1:
                self.var.set(value)
            elif int(value + 0.5) < 500:
                self.var.set(1)
            else:
                self.var.set(int(value + 0.5))
        except ValueError:
            logger.warning("Upable to convert %s to float, setting self.vat to to 1", value)
            self.var.set(1)
        except Exception as e:
            logger.error("exception: %s, setting self.vat to 1", e)
            self.var.set(1)

        _ = ""
        val = float(self.var.get())
        # if val == 1 or val < 500:
        if val < 1:
            _ = f"max_df: {val}, relative, {val:.0%} docus will be taken into account."
        elif val < 500:
            _ = f"max_df: {val}, relative, all docus with bottom {val:.0%} of the docu frequences will be taken into account."
        else:  # val > 1:
            val = int(val)
            _ = f"max_df: {val}, absolute, docu with frequences smaller than {val} will be taken into account."

        self.statustext_var.set(_)

    def print_option(self, evt=None):
        """Fake callback."""
        logger.debug("""self.var.get(): %s""", self.var.get())

    def quit(self, evt=None):
        """Kill the widget: callback winfo_toplevel().destroy()."""
        logger.debug("evt: %s, dir(evt): %s", evt, dir(evt) if evt is not None else None)
        self.winfo_toplevel().destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("max_df")

    root.bind("<Escape>", lambda evt: logger.debug(inspect(evt)) or print(dir(evt)) or print(evt) or root.destroy(), add="+")  # type: ignore

    widget = MaxDfWidget()
    widget.pack(fill=tk.BOTH)

    # widget1 = MaxDfWidget()
    # widget1.pack()

    # root.geometry("300x100")
    root.geometry("420x200")
    root.mainloop()
