from pynput.mouse import Controller
import tkinter as tk

def update_coordinates_label():
    if is_program_running:
        x, y = mouse.position
        coordinates_label.config(text=f"X: {x}, Y: {y}")
    root.after(50, update_coordinates_label)

def toggle_program():
    global is_program_running
    is_program_running = not is_program_running
    if is_program_running:
        toggle_button.config(text="Turn Off")
    else:
        toggle_button.config(text="Turn On")

mouse = Controller()
is_program_running = True

root = tk.Tk()
root.title("Mouse Coordinates Display")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 200
window_height = 80

window_x = screen_width - window_width
window_y = 0

root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

coordinates_label = tk.Label(root, text="")
coordinates_label.pack()

toggle_button = tk.Button(root, text="Turn Off", command=toggle_program)
toggle_button.pack()

update_coordinates_label()

root.mainloop()
