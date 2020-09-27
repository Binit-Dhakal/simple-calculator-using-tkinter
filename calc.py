import tkinter as tk
from tkinter import ttk

expression = ""


class calc_keys(tk.Button):
    def __init__(
        self,
        parent,
        cmd,
        text=None,
        fg="black",
        bg="yellow",
        height=4,
        width=9,
        input_args=None,
        **kwargs
    ):
        super().__init__(parent, text=text, fg=fg, bg=bg, height=height, width=width)

        self.configure(command=lambda: self._on_click(cmd))
        self.equation = kwargs.get("equation", None)

    def _on_click(self, cmd):
        global expression
        if cmd == "clear":
            expression = ""
            self.equation.set(expression)
        elif cmd == "=":
            try:
                total = str(eval(expression))
                self.equation.set(total)
                expression = ""
            except:
                self.equation.set("error")
                expression = ""
        else:
            expression += str(cmd)
            self.equation.set(expression)

    def grids(self, row, column, sticky=(tk.W)):
        self.grid(row=row, column=column, sticky=sticky)


class Calculator(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        equation = tk.StringVar()

        # row0
        calc_keys(self, cmd=1, text="1", equation=equation).grids(row=0, column=0)
        calc_keys(self, cmd=2, text="2", equation=equation).grids(row=0, column=1)
        calc_keys(self, cmd=3, text="3", equation=equation).grids(row=0, column=2)
        calc_keys(self, cmd="*", text="x", equation=equation).grids(row=0, column=3)

        # row1
        calc_keys(self, cmd=4, text="4", equation=equation).grids(row=1, column=0)
        calc_keys(self, cmd=5, text="5", equation=equation).grids(row=1, column=1)
        calc_keys(self, cmd=6, text="6", equation=equation).grids(row=1, column=2)
        calc_keys(self, cmd="+", text="+", equation=equation).grids(row=1, column=3)

        # row2
        calc_keys(self, cmd=7, text="7", equation=equation).grids(row=2, column=0)
        calc_keys(self, cmd=8, text="8", equation=equation).grids(row=2, column=1)
        calc_keys(self, cmd=9, text="9", equation=equation).grids(row=2, column=2)
        calc_keys(self, cmd="-", text="-", equation=equation).grids(row=2, column=3)

        # row3
        calc_keys(self, cmd="clear", text="Clear", equation=equation).grids(
            row=3, column=0
        )
        calc_keys(self, cmd=0, text="0", equation=equation).grids(row=3, column=1)
        calc_keys(self, cmd="/", text="/", equation=equation).grids(row=3, column=2)
        calc_keys(self, cmd="=", text="=", equation=equation).grids(row=3, column=3)

        # row4
        expression_field = tk.Entry(self, textvariable=equation)
        expression_field.grid(columnspan=4, ipadx=90, ipady=7)
        equation.set("Enter your expression here")


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x315")
        self.title("Tkinter-Calculator")
        Calculator().pack()


if __name__ == "__main__":
    root = Application()
    root.mainloop()
