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
        self.layer_point_var = StringVar()
        self.layer_point_var.set("0_pomiar")
        self.layer_text_var = StringVar()
        self.layer_text_var.set("0_pomiar_tekst")
        self.text_h_var = StringVar()
        self.text_h_var.set("0.2")
        self.with_z_var = BooleanVar()

        self.text_field = Text(mframe, state="disabled")
        self.text_field.grid(column=1, columnspan=8, row=1, sticky=(W, S, E, N))

        self.layer_point_label = Label(mframe, text="Warstwa dla punktów:", borderwidth=5)
        self.layer_point_label.grid(column=1, row=2, sticky=W)
        self.layer_point = Entry(mframe, textvariable=self.layer_point_var)
        self.layer_point.grid(column=2, row=2, sticky=W)
        self.layer_text_label = Label(mframe, text="Warstwa dla tekstów:", borderwidth=5)
        self.layer_text_label.grid(column=3, row=2, sticky=W)
        self.layer_text = Entry(mframe, textvariable=self.layer_text_var)
        self.layer_text.grid(column=4, row=2, sticky=W)

        self.text_h_label = Label(mframe, text="Wysokość tekstów:", borderwidth=5)
        self.text_h_label.grid(column=1, row=3, sticky=W)
        self.text_h = Entry(mframe, textvariable=self.text_h_var)
        self.text_h.grid(column=2, row=3, sticky=W)
        self.with_z = Checkbutton(mframe, text="Punkty z wysokością", variable=self.with_z_var)
        self.with_z.grid(column=3, columnspan=2, row=3, sticky=W)

        self.label_in = ttk.Label(mframe, relief="sunken", borderwidth=5)
        self.label_in.grid(row=4, column=1, columnspan=8, sticky=(W, E))

        button_path = ttk.Button(mframe, text="Plik wejściowy...", command=self.ask_path)
        button_path.grid(row=5, column=1, sticky=W)

        self.label_out = ttk.Label(mframe, relief="sunken", borderwidth=5)
        self.label_out.grid(row=6, column=1, columnspan=8, sticky=(W, E))

        button_path = ttk.Button(mframe, text="Plik wyjściowy...", command=self.ask_path_out)
        button_path.grid(row=7, column=1, sticky=W)

        button_gen = ttk.Button(mframe, text="Generuj", command=lambda: filer(self.path_in, self.path_out,
                                                                              self.layer_point_var.get(),
                                                                              self.layer_text_var.get(),
                                                                              self.text_h_var.get(),
                                                                              str(self.with_z_var.get())))
        button_gen.grid(row=7, column=6, sticky=E)

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
