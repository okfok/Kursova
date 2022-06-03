import GUI.click_actions as ca
from GUI.main import app


def pack():
    app.labelX.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    app.entryX.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    app.button_add.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    app.button_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    app.labelY.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    app.entryY.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
    app.button_delete.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
    app.button_graph.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

    app.labelX0.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
    app.entryX0.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
    app.checkbox_linear.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
    app.checkbox_newton.grid(row=3, column=2, sticky="ew", padx=5, pady=5)

    app.frameInput.grid(row=0, column=0, sticky="ns")
    app.scrollbar.grid(row=1, column=0, padx=5, pady=5)
    app.pointsListBox.grid(row=1, column=0, sticky="ew")

    app.frameMenu.grid(row=0, column=0, sticky="ns")

    app.labelResult.pack(padx=5, pady=10)
    app.graph.get_tk_widget().pack()

    app.frameOutput.grid(row=0, column=1, sticky="ns")


def bind_click_actions():
    app.button_add.bind("<Button>", ca.add_clicked)
    app.button_delete.bind("<Button>", ca.delete_clicked)
    app.button_clear.bind("<Button>", ca.clear_clicked)
    app.button_graph.bind("<Button>", ca.graph_clicked)


def bind_menu():
    app.menu_file.add_command(label='Open', command=ca.open_clicked)
    app.menu_file.add_command(label='Save', command=ca.save_clicked)
    app.menu_file.add_command(label='Exit', command=ca.app.exit)

    app.menu.add_cascade(label='File', menu=app.menu_file)

    app.menu_examples.add_command(label='Sqrt', command=ca.sqrt_example)
    app.menu_examples.add_command(label='Quadratic', command=ca.quadratic_example)
    app.menu_examples.add_command(label='Cubic', command=ca.cubic_example)
    app.menu_examples.add_command(label='Sin', command=ca.sin_example)
    app.menu_examples.add_command(label='Cos', command=ca.cos_example)
    app.menu_examples.add_command(label='Rand', command=ca.rand_example)

    app.menu.add_cascade(label='Examples', menu=app.menu_examples)
