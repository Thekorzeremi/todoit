"""A simple to-do list application with system tray integration."""
import os
import json
import threading as th
import tkinter as tk
from tkinter.messagebox import showinfo
import pystray as pys
from PIL import Image

LOGO_FILE = './logo.png'
TODO_FILE = '~/.todoit/todo_items.json'

window = tk.Tk()
window.title('ToDoIt')
window.iconphoto(False, tk.PhotoImage(file=LOGO_FILE))
window.withdraw()

system_tray_image = Image.open('logo.png')


def close_app():
    """Close the application window"""
    window.withdraw()


def open_app():
    """Open the application window"""
    window.deiconify()


def quit_app(tray_icon):
    """Kill the application process"""
    tray_icon.stop()
    window.destroy()


def load_todo_file():
    """Load to-do items from the JSON file"""
    expanded_path = os.path.expanduser(TODO_FILE)
    if not os.path.exists(expanded_path):
        create_todo_file()
    with open(expanded_path, 'r', encoding='utf-8') as file:
        try:
            items = json.load(file)
            return items
        except json.JSONDecodeError:
            return []


def create_todo_file():
    """Create the to-do JSON file if it doesn't exist"""
    expanded_path = os.path.expanduser(TODO_FILE)
    os.makedirs(os.path.dirname(expanded_path), exist_ok=True)
    with open(expanded_path, 'w', encoding='utf-8') as file:
        json.dump([], file)


def save_todo_file(items):
    """Save to-do items to the JSON file"""
    expanded_path = os.path.expanduser(TODO_FILE)
    with open(expanded_path, 'w', encoding='utf-8') as file:
        json.dump(items, file, indent=2)


def add_todo():
    """Add a new to-do item from the entry input"""
    text = entry.get().strip()
    if text:
        todo_items.append({'text': text, 'done': False})
        save_todo_file(todo_items)
        entry.delete(0, tk.END)
        refresh_todo_list()


def toggle_todo(index):
    """Toggle the 'done' status of a to-do item"""
    todo_items[index]['done'] = not todo_items[index]['done']
    save_todo_file(todo_items)
    refresh_todo_list()


def delete_todo(index):
    """Delete a to-do item"""
    del todo_items[index]
    save_todo_file(todo_items)
    refresh_todo_list()


def refresh_todo_list():
    """Refresh the displayed to-do list"""
    for widget in todo_frame.winfo_children():
        widget.destroy()

    for i, item in enumerate(todo_items):
        item_frame = tk.Frame(todo_frame)
        item_frame.pack(fill=tk.X, pady=2)

        checkbox = tk.Checkbutton(
            item_frame,
            text=item['text'],
            command=lambda idx=i: toggle_todo(idx)
        )
        if item['done']:
            checkbox.select()
        checkbox.pack(side=tk.LEFT, fill=tk.X, expand=True)

        delete_btn = tk.Button(
            item_frame,
            text='❌',
            command=lambda idx=i: delete_todo(idx),
            width=3
        )
        delete_btn.pack(side=tk.RIGHT)


def show_infos():
    """Show an about alert dialog"""
    showinfo(
        title='À propos de ToDoIt',
        message='ToDoIt v0.1\n\n' \
        'Une application simple de liste de tâches avec intégration système pour Xfce.' \
        '\n\nDéveloppé par Thekorzeremi.'
    )

icon = pys.Icon(
    name='ToDoIt',
    icon=system_tray_image,
    menu=pys.Menu(
        pys.MenuItem(
            'Ouvrir l\'application',
            open_app
        ),
        pys.MenuItem(
            'Quitter',
            quit_app
        )
    )
)

label = tk.Label(window, text='ToDoIt')
label.pack()

menuBar = tk.Menu(window)

menu1 = tk.Menu(
    menuBar,
    tearoff=0
)
menu1.add_command(
    label='Fermer',
    command=close_app
)
menu1.add_command(
    label='Quitter',
    command=lambda: quit_app(icon)
)
menuBar.add_cascade(
    label='Fichier',
    menu=menu1
)

menu2 = tk.Menu(
    menuBar,
    tearoff=0
)
menu2.add_command(
    label='À propos',
    command=show_infos
)
menuBar.add_cascade(
    label='Aide',
    menu=menu2
)

main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

input_frame = tk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=(0, 10))

entry = tk.Entry(input_frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 5))

add_button = tk.Button(input_frame, text='Ajouter', command=add_todo)
add_button.pack(side=tk.LEFT)

canvas_frame = tk.Frame(main_frame)
canvas_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(canvas_frame)
scrollbar = tk.Scrollbar(canvas_frame, orient='vertical', command=canvas.yview)
todo_frame = tk.Frame(canvas)

todo_frame.bind(
    '<Configure>',
    lambda e: canvas.configure(scrollregion=canvas.bbox('all'))
)

canvas.create_window((0, 0), window=todo_frame, anchor='nw')
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

todo_items = []

todo_items = load_todo_file()
refresh_todo_list()

th.Thread(target=icon.run, daemon=True).start()

window.config(menu=menuBar)
window.protocol('WM_DELETE_WINDOW', close_app)
window.mainloop()
