import tkinter as tk
from time import strftime
from datetime import datetime

root = tk.Tk()
root.title("Clock with Date")

# No border and transparent background
root.overrideredirect(True)
root.attributes('-alpha', 1)  # transparent
root.attributes('-topmost', False)  # Don't stay on top
root.wm_attributes('-transparentcolor', 'black')  # black will be fully transparent
root.configure(bg='black')

# Fixed position (bottom right)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("+20+20")

# Date label
date_label = tk.Label(root, font=('Algerian', 30), fg='white', bg='black', anchor='w', justify='left')
# Time label
clock_label = tk.Label(root, font=('Algerian', 30), fg='white', bg='black', anchor='w', justify='left')
# Static message
massage = tk.Label(root, text="Hello, Pawan!", font=('Algerian', 30), fg='white', bg='black', anchor='w', justify='left')


massage.pack(fill='x', padx=5, pady=(0, 0))
date_label.pack(fill='x', padx=5, pady=(0, 0))
clock_label.pack(fill='x', padx=5, pady=(0, 0))


# Update function
def update():
    current_time = strftime('%H:%M:%S')
    current_date = datetime.now().strftime('Today is %A, %d %B %Y')  # Example: Friday, 02 May 2025

    date_label.config(text=current_date)
    clock_label.config(text=current_time)

    root.after(1000, update)

update()

# Make draggable
def move(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

clock_label.bind('<B1-Motion>', move)
date_label.bind('<B1-Motion>', move)
massage.bind('<B1-Motion>', move)

root.mainloop()
