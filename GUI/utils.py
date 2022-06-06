import tkinter as tk

import core
from GUI.app import app


def get_point() -> core.Point:
    x, y = None, None
    try:
        x = float(app.entryX.get())
        y = float(app.entryY.get())
    except ValueError:
        pass
    app.entryX.delete(0, tk.END)
    app.entryY.delete(0, tk.END)
    return core.Point(x, y) if None not in (x, y) else None


def get_x0():
    try:
        x0 = float(app.entryX0.get())
        return x0 if app.interp.x_validate(x0) else None
    except ValueError:
        return


def delete_selected_points() -> None:
    for index in reversed(app.listbox_points.curselection()):
        app.interp.del_point(index)


def display_points():
    app.listbox_points.delete(0, tk.END)
    for text in map(str, app.interp.points):
        app.listbox_points.insert(tk.END, text)


def display_result(x: float, ly: float, ny: float):
    app.label_result['text'] = \
        'Result:\n' + \
        (f'Linear ({round(x, 5)}, {round(ly, 5)})\n'
         if app.checkbox_linear.get() and ly is not None
         else 'Linear -\n') + \
        (f'Newton ({round(x, 5)}, {round(ny, 5)})'
         if app.checkbox_newton.get() and ny is not None
         else 'Newton -')


def draw_graph(x0: float = None):
    app.figure.clear()
    ax = app.figure.add_subplot(111)

    ax.plot(app.interp.x, app.interp.y, '.', color='black')

    if len(app.interp.points) >= 2:
        interval = app.interp.get_interval()
        ly = ny = None

        if app.checkbox_linear.get():
            linear = app.interp.linear_interpolation_func
            ax.plot(
                interval,
                list(map(linear, interval)),
                '--',
                label="linear interpolation",
                color='blue'
            )
            if isinstance(x0, float):
                ly = linear(x0)
                ax.plot(x0, ly, 'o', color='blue')

        if app.checkbox_newton.get():
            import warnings
            warnings.filterwarnings('error')
            try:
                newton = app.interp.get_newton_interpolation_func()
                y = list(map(newton, interval))
                ax.plot(
                    interval,
                    y, '-.',
                    label="newton interpolation",
                    color='green'
                )
                if isinstance(x0, float):
                    ny = newton(x0)
                    ax.plot(x0, ny, 'o', color='green')
            except Warning:
                pass

        display_result(x0, ly, ny)

        ax.legend(loc='best')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

    app.canvas.draw()
    app.toolbar.update()
