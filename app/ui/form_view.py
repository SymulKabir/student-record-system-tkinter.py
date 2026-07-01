import tkinter as tk
from tkinter import ttk
from app.ui.insert_view import InsertView

class FormView:
    def __init__(self, root):
        self.show = {
            "insert_frame": False,
        }
        self.root = root
        self.title_label = ttk.Label(root, text="Form View", foreground="blue")
        self.title_label.pack(pady=10)
        self.tree_view = ttk.Treeview(root, columns=("ID", "Name", "Phone"), show="headings")
        self.tree_view.heading("ID", text="ID")
        self.tree_view.heading("Name", text="Name")
        self.tree_view.heading("Phone", text="Phone")

        # self.tree_view.insert("", "end", values=("1", "John Doe", "01881"))
        self.tree_view.pack(padx=50)


        footer_frame = ttk.Frame(root)
        footer_frame.pack(fill="x", padx=10, pady=10)

        # Make all 3 columns expand equally
        footer_frame.columnconfigure(0, weight=1)
        footer_frame.columnconfigure(1, weight=1)
        footer_frame.columnconfigure(2, weight=1)

        insert_button = ttk.Button(
            footer_frame,
            text="Insert",
            command=self.open_insert_window
        )
        insert_button.grid(row=0, column=0, padx=5, sticky="ew")

        update_button = ttk.Button(
            footer_frame,
            text="Update",
            command=self.open_update_window
        )
        update_button.grid(row=0, column=1, padx=5, sticky="ew")

        delete_button = ttk.Button(
            footer_frame,
            text="Delete",
            command=self.open_delete_window
        )
        delete_button.grid(row=0, column=2, padx=5, sticky="ew")
        self.insert_view = InsertView(self.root)




    def open_insert_window(self): 
        if self.show.get("insert_frame"):
            self.insert_view.main_frame.pack_forget()
        else:
            self.insert_view.main_frame.pack()
        self.show["insert_frame"] = not self.show.get("insert_frame")
    
    def open_update_window(self):
        pass

    def open_delete_window(self):
        pass
        