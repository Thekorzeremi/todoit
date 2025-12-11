import pystray as pys
import tkinter as tk
import threading as th
import os
import json
from PIL import Image

window = tk.Tk()
window.withdraw()

system_tray_image = Image.open('logo.png')

todo_file = '~/.todoit/todo_items.json'

isOpen = False

def close_app():
    window.withdraw()

def open_app():
    window.deiconify()

def quit_app(icon):
    icon.stop()
    window.destroy()

def get_window_state():
    return isOpen

def load_todo_file():
    expanded_path = os.path.expanduser(todo_file)
    if not os.path.exists(expanded_path):
        create_todo_file()
    with open(expanded_path, 'r') as file:
        try:
            items = json.load(file)
            return items
        except json.JSONDecodeError:
            return []

def create_todo_file():
    expanded_path = os.path.expanduser(todo_file)
    os.makedirs(os.path.dirname(expanded_path), exist_ok=True)
    with open(expanded_path, 'w') as file:
        json.dump([], file)

def save_todo_file(items):
    expanded_path = os.path.expanduser(todo_file)
    with open(expanded_path, 'w') as file:
        json.dump(items, file, indent=2)

icon = pys.Icon(
    name='ToDoIt',
    icon=system_tray_image,
    menu=pys.Menu(
        pys.MenuItem(
            'Ouvrir l\'application',
            open_app
        ),
        pys.MenuItem(
            'Quitter l\'application',
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
    label='Quitter',
    command=close_app
)
menuBar.add_cascade(
    label='Fichier',
    menu=menu1
)

main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

input_frame = tk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=(0, 10))

entry = tk.Entry(input_frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 5))

add_button = tk.Button(input_frame, text='Ajouter', command=lambda: add_todo())
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

def add_todo():
    text = entry.get().strip()
    if text:
        todo_items.append({'text': text, 'done': False})
        save_todo_file(todo_items)
        entry.delete(0, tk.END)
        refresh_todo_list()

def toggle_todo(index):
    todo_items[index]['done'] = not todo_items[index]['done']
    save_todo_file(todo_items)
    refresh_todo_list()

def delete_todo(index):
    del todo_items[index]
    save_todo_file(todo_items)
    refresh_todo_list()

def refresh_todo_list():
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

todo_items = load_todo_file()
refresh_todo_list()

th.Thread(target=icon.run, daemon=True).start()

window.config(menu=menuBar)
window.mainloop()