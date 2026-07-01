import tkinter as tk
from app.db.connection import db_instance, db

class InsertView:
    def __init__(self, root):
        self.root = root
        self.input = {
            "id": "",
            "name": "",
            "phone": ""
        }

        # Background
        self.root.configure(bg="#e9ecef")

        # Card
        self.main_frame = tk.Frame(
            root,
            bg="white",
            bd=1,
            relief="solid",
            padx=25,
            pady=20
        )
        self.main_frame.pack(padx=20, pady=20)

        # Title
        tk.Label(
            self.main_frame,
            text="Insert Contact",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#2c3e50"
        ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.id_entry = self.create_field("ID", 1)
        self.name_entry = self.create_field("Name", 2)
        self.phone_entry = self.create_field("Phone", 3)

        # Save Button
        button_frame = tk.Frame(self.main_frame, bg="red")
        button_frame.grid(row=4, column=0, columnspan=2, pady=(5, 0))
        tk.Button(
            button_frame,
            text="Cancel",
            bg="#0d6efd",
            fg="#000",
            activebackground="#0b5ed7",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI", 11, "bold"),
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.save
        ).grid(row=0, column=0, sticky="w")

        tk.Button(
            button_frame,
            text="Save",
            bg="#0d6efd",
            fg="#000",
            activebackground="#0b5ed7",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI", 11, "bold"),
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.save
        ).grid(row=0, column=1, sticky="w")

        # self.main_frame.columnconfigure(1, weight=1)

    def create_field(self, label, row):
        tk.Label(
            self.main_frame,
            text=label,
            bg="white",
            fg="#495057",
            font=("Segoe UI", 11)
        ).grid(row=row, column=0, sticky="e", padx=(0, 15), pady=8)

        entry = tk.Entry(
            self.main_frame,
            font=("Segoe UI", 11),
            relief="solid",
            bd=1,
            width=30
        )
        entry.insert(0, self.input.get(label.lower(), ""))
        entry.grid(row=row, column=1, sticky="ew", pady=8)
        entry.bind("<KeyRelease>", lambda event, field=label.lower(): self.handle_input_change(event, field))

        return entry

    def handle_input_change(self, event, field):
        widget = event.widget
        self.input[field] = widget.get()
        print("widget.get() -->", widget.get())
        print("self.input -->", self.input)


    def save(self):
        try:
            print("Saving contact:", self.input)
            db.execute(
                """
                INSERT INTO contacts (id, name, phone)
                VALUES (%s, %s, %s)
                """,
                (
                    self.input["id"],
                    self.input["name"],
                    self.input["phone"],
                ),
            )

            db_instance.commit()
            self.input["id"] = ""
            self.input["name"] = ""
            self.input["phone"] = ""
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            
            print("Contact saved successfully.")

        except Exception as e:
            db_instance.rollback()
            print("Error:", e)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Insert View")
    root.geometry("420x320")

    InsertView(root)

    root.mainloop()