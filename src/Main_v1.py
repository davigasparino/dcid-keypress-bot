import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Layout Personalizado")
        self.root.geometry("800x600")

        frame = tk.Frame(self.root)
        frame.pack(side="top", fill="x", padx=5)

        self.checkbox_var = tk.BooleanVar()
        self.checkbox_var.set(True)
        
        self.checkbox = tk.Checkbutton(frame, text="Random", variable= self.checkbox_var)
        self.checkbox.pack(side="left", padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
