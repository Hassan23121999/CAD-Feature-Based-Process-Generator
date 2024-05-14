import pandas as pd
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from OCC.Display.SimpleGui import init_display
from OCC.Extend.DataExchange import read_step_file
import os
import threading

def display_step_file(file_path):
    display, start_display, add_menu, add_function_to_menu = init_display()
    my_shape = read_step_file(file_path)
    display.DisplayShape(my_shape, update=True)
    start_display()

def main_app():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    collect_and_save_process_info(root)
    
    root.mainloop()

def collect_and_save_process_info(root):
    step_file_path = filedialog.askopenfilename(title="Select STEP File", filetypes=[("STEP files", "*.step;*.stp")])
    if not step_file_path:
        messagebox.showinfo("Information", "No STEP file selected!")
        return
    
    window = tk.Toplevel(root)
    label = tk.Label(window, text=f"Selected STEP File: {os.path.basename(step_file_path)}")
    label.pack()

    has_holes_var = tk.IntVar()
    has_holes_checkbutton = tk.Checkbutton(window, text="Has Holes", variable=has_holes_var)
    has_holes_checkbutton.pack()

    shape_var = tk.StringVar(value="symmetrical")
    symmetrical_radiobutton = tk.Radiobutton(window, text="Symmetrical", variable=shape_var, value="symmetrical")
    asymmetrical_radiobutton = tk.Radiobutton(window, text="Asymmetrical", variable=shape_var, value="asymmetrical")
    symmetrical_radiobutton.pack()
    asymmetrical_radiobutton.pack()

    submit_button = tk.Button(window, text="Submit", command=lambda: submit_info(window, has_holes_var.get(), shape_var.get(), step_file_path))
    submit_button.pack()

    display_thread = threading.Thread(target=display_step_file, args=(step_file_path,))
    display_thread.start()

def submit_info(window, has_holes, shape_type, step_file_path):
    window.destroy()
    
    processes = []
    if has_holes:
        processes.append("Drilling")

    if shape_type == "symmetrical":
        processes.append("Turning")
    else:
        processes.append("Turning")
        processes.append("Milling")
    
    # Asking if the user wants to add additional processes
    add_additional_processes = messagebox.askyesno("Question", "Do you want to add any additional processes?")
    if add_additional_processes:
        num_other_processes = simpledialog.askinteger("Input", "Enter the number of other processes", minvalue=0, maxvalue=10)
        for _ in range(num_other_processes):
            other_process = simpledialog.askstring("Input", "Enter the name of other process")
            if other_process:
                processes.append(other_process.strip())

    df = pd.DataFrame({'Processes': processes})
    excel_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    if excel_file_path:
        df.to_excel(excel_file_path, index=False)
        os.startfile(excel_file_path)
    
    main_app()

if __name__ == '__main__':
    main_app()
