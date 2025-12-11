# ToDoIt 📝

A lightweight and fast ToDo list application written in Python with system tray integration for Linux desktop environments.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)

## Disclaimer
UI is horrible I know

## ✨ Features

- 🎯 **Simple & Intuitive** - Clean interface for managing your daily tasks
- 🔔 **System Tray Integration** - Quick access from your notification area
- 💾 **Persistent Storage** - Your tasks are automatically saved in JSON format
- ⚡ **Lightweight** - Minimal resource usage
- 🖥️ **Desktop Environment Support** - Optimized for XFCE and other Linux DEs
- ✅ **Task Management** - Add, complete, and delete tasks effortlessly

## 📋 Requirements

- Python 3.x
- tkinter (usually included with Python)
- pystray
- Pillow (PIL)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Thekorzeremi/todoit.git
cd todoit
```

2. Install dependencies:
```bash
pip install pystray Pillow
```

3. Make sure you have a `logo.png` file in the project directory for the system tray icon.

## 💻 Usage

Run the application:
```bash
python app.py
```

The application will start minimized in the system tray. Click the tray icon to access:
- **Ouvrir l'application** - Show the main window
- **Quitter l'application** - Close the application

### Main Window

- **Add tasks**: Type your task in the input field and click "Ajouter"
- **Complete tasks**: Click the checkbox next to a task to mark it as done
- **Delete tasks**: Click the ❌ button to remove a task
- **Hide window**: Use the File menu → Quitter to minimize to tray

## 📁 File Structure

```
gtk-todo/
├── app.py              # Main application file
├── logo.png            # System tray icon
├── README.md           # This file
└── ~/.todoit/          # Configuration directory
    └── todo_items.json # Tasks storage
```

## 🗂️ Data Storage

Tasks are stored in `~/.todoit/todo_items.json` with the following format:

```json
[
  {
    "text": "My first task",
    "done": false
  },
  {
    "text": "Completed task",
    "done": true
  }
]
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🐛 Known Issues

- The application is optimized for Linux desktop environments
- System tray integration may vary depending on your desktop environment

## 💡 Future Enhancements

- [ ] Better UI LOL
- [ ] Dark mode support
- [ ] Task categories/tags
- [ ] Task priority levels
- [ ] Due dates and reminders
- [ ] Export/Import functionality
- [ ] Keyboard shortcuts
- [ ] Multi-language support
- [ ] Notification alerts

## 👨‍💻 Author

Made with ❤️ by Thekorzeremi

## 🙏 Acknowledgments

- Built with Python and tkinter for GUI
- System tray integration powered by pystray
- Icons and images processed with Pillow

---

⭐ If you find this project useful, please consider giving it a star!