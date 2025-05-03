# Transparent Clock with Date and Custom Message

This project is a simple, draggable, and transparent clock application built using Python's `tkinter` library. It displays the current time, date, and a static custom message in a visually appealing format. The application is designed to run as a desktop widget with a transparent background, making it blend seamlessly with the desktop environment.

---

## Features

### 1. **Live Clock**
- Displays the current time in `HH:MM:SS` format.
- Updates every second to ensure accurate timekeeping.

### 2. **Date Display**
- Shows the current date in a friendly format, such as:
- Today is Friday, 02 May 2025

### 3. **Custom Message**
- Displays a static message ("Hello, Pawan!") at the top of the widget.
- The message can be customized to display any text.

### 4. **Transparent Background**
- The widget has a transparent background, allowing it to blend seamlessly with the desktop.
- The color `black` is treated as fully transparent.

### 5. **Draggable**
- The widget can be dragged to any position on the screen by clicking and holding the labels.

### 6. **Always-On-Top Option**
- The widget can optionally be configured to stay on top of other windows.

### 7. **Lightweight and Portable**
- The application is lightweight and can be easily packaged into an executable for distribution.

---

## How It Works

### 1. **Initialization**
- The script initializes a `tkinter` window (`root`) with the following properties:
- No border (`overrideredirect(True)`).
- Transparent background (`wm_attributes('-transparentcolor', 'black')`).
- Positioned at the bottom-right corner of the screen by default.

### 2. **Labels**
- Three labels are created:
- **Static Message Label**: Displays a custom message.
- **Date Label**: Displays the current date.
- **Clock Label**: Displays the current time.

### 3. **Update Function**
- The `update` function is responsible for:
- Fetching the current time using `strftime`.
- Fetching the current date using `datetime.now()`.
- Updating the text of the `date_label` and `clock_label` every second using `root.after`.

### 4. **Draggable Feature**
- The `move` function allows the widget to be dragged by binding the `<B1-Motion>` event to the labels.

### 5. **Main Loop**
- The `root.mainloop()` method starts the `tkinter` event loop, keeping the application running.

---

## Installation

### Prerequisites
- Python 3.x
- `tkinter` (comes pre-installed with Python)

### Steps
1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Run the script using the following command:
 ```bash
 python clock.py
