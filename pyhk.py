from pynput.keyboard import Listener, Key

key = Key

key_set = set()

hot_key_list = []

all_key = set()


def press(key):
    if key in all_key:
        if key in key_set:
            key_set.clear()
        key_set.add(key)
        func = matching_hot_key(key_set)
        if func:
            func()
    else:
        key_set.clear()


def matching_hot_key(keys):
    func = None
    for hot_kye in hot_key_list:
        if keys == set(hot_kye[0]):
            func = hot_kye[1]
    return func


def add_hot_key(hotkey, fhot):
    all_key.update(hotkey)
    if hotkey not in hot_key_list:
        hot_key_list.append((hotkey, fhot))


def start():
    with Listener(on_press=press) as listener:
        listener.join()
