from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from Functions import filer


class Txt2dxf:
    def __init__(self, root):
        root.title("Txt2dxf")

        mframe = ttk.Frame(root, padding=10, width=400, height=400)
        mframe.grid(column=0, row=0, sticky=(W, S, E, N))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.path_in = StringVar()
        self.path_out = StringVar()
        self.text_field = Text(mframe, state="disabled")
        self.text_field.grid(column=1, columnspan=2, row=1, sticky=(W, S, E, N))

        self.label_in = ttk.Label(mframe, relief="sunken", borderwidth=5)
        self.label_in.grid(row=2, column=1, columnspan=2, sticky=(W, E))

        button_path = ttk.Button(mframe, text="Plik wejściowy...", command=self.ask_path)
        button_path.grid(row=3, column=1, sticky=W)

        self.label_out = ttk.Label(mframe, relief="sunken", borderwidth=5)
        self.label_out.grid(row=4, column=1, columnspan=2, sticky=(W, E))

        button_path = ttk.Button(mframe, text="Plik wyjściowy...", command=self.ask_path_out)
        button_path.grid(row=5, column=1, sticky=W)

        button_gen = ttk.Button(mframe, text="Generuj", command=lambda: filer(self.path_in, self.path_out))
        button_gen.grid(row=5, column=2, sticky=E)

    def ask_path(self):
        self.path_in = filedialog.askopenfilename()
        self.label_in.configure(text=self.path_in)
        temp = self.path_in[:-3]
        self.label_out.configure(text=temp+"dxf")
        self.path_out = temp+"dxf"
        with open(self.path_in, "r") as f:
            read_lines = f.read()
        self.text_field.configure(state="normal")
        self.text_field.insert("1.0", read_lines)
        self.text_field.configure(state="disabled")

    def ask_path_out(self):
        self.path_out = filedialog.asksaveasfile()
        self.path_out = self.path_out.name
        self.label_out.configure(text=self.path_out)
        print(self.path_out)
