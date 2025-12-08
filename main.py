# Alarmo/main.py

import tkinter as tk
from gui.alarmo_app import AlarmoApp # Import from the gui package

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmoApp(root)
    root.mainloop()