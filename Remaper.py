import keyboard
import ctypes

def is_num_lock_active():
    hllDll = ctypes.WinDLL("User32.dll")
    vk_num_lock = 0x90
    return hllDll.GetKeyState(vk_num_lock) & 1

# method for the key hooks
def dynamic_create_keys(key, new_key):
     def hook(event):
         print("hook function called")
         if event.event_type == 'down':
             if is_num_lock_active() == 1:
                 print(f"num lock is active. sending {new_key}")
                 keyboard.send(new_key)  # Send assigned number when Num Lock is active
             else:
                 print(f"num lock is inactive. sending {key}")
                 keyboard.send(key)  # Send letter when Num Lock is inactive
     return hook

# list of the keys to remap
key_list = {
    'q': '1',
    'w': '2',
    'e': '3',
    'r': '4',
    't': '5',
    'y': '6',
    'u': '7',
    'i': '8',
    'o': '9',
    'p': '0',
}

# Hook keys to call the hook function
for key, new_key in key_list.items():
     keyboard.hook_key(key, dynamic_create_keys(key, new_key), suppress=True)

# Wait for the 'esc' key to exit the program
keyboard.wait('esc+c+l')