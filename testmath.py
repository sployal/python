import PySimpleGUI as sg
import numpy as np

def divided_diff(x, y):
    # Calculate divided differences recursively
    n = len(x)
    coef = np.zeros((n, n))
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef

# Create the GUI layout
layout = [
    [sg.Text("Enter x values (comma-separated):"), sg.InputText(key="x_values")],
    [sg.Text("Enter y values (comma-separated):"), sg.InputText(key="y_values")],
    [sg.Button("Calculate"), sg.Button("Exit")],
    [sg.Multiline(size=(40, 10), key="output", disabled=True)],
]

window = sg.Window("Newton's Divided Difference Table", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    try:
        x_values = np.array([float(x) for x in values["x_values"].split(",")])
        y_values = np.array([float(y) for y in values["y_values"].split(",")])

        coef_matrix = divided_diff(x_values, y_values)

        # Display the divided difference table
        output_text = ""
        for i in range(len(x_values)):
            output_text += f"x{i} = {x_values[i]:.2f}: {', '.join(f'{coef_matrix[i][j]:.6f}' for j in range(i+1))}\n"

        window["output"].update(output_text)

    except ValueError:
        sg.popup_error("Invalid input. Please enter valid numeric values.")

window.close()
