import tkinter as tk
from app.ui.form_view import FormView

class InitUi:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello")
        app_height = 700
        app_width = 600
        y_position = 0
        x_position = root.winfo_screenwidth() - app_width
        self.root.geometry(f"{app_width}x{app_height}+{x_position}+{y_position}")
        FormView(self.root)
        
        
        
        





if __name__ == "__main__":
    root = tk.Tk()
    InitUi(root)
    root.mainloop()