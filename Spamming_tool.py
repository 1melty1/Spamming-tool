# -*- coding: UTF-8 -*-
import time, threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener, KeyCode, Controller as KeyboardController
from random import uniform, randrange

print("Made by WYW")
message_variation_number = int(input("How many string do you want to enter ? "))
random_or_not = input("Do you want make the message random ( inverted ) ? (y/n)")
time_random_or_not = input("Do you want the sending time to be random ? (y/n)")
if time_random_or_not == "y" :
    time_random_upper_limit = float(input("Random time upper limit ( s )? "))
    time_random_lower_limit = float(input("Random time lower limit ( s )? "))
else:
    delay = float(input('Delay ( Recommend 0.1s ) : '))

i2 = 0
message_list = []
while i2 < message_variation_number :
    i2 += 1
    original_string = input(f'Your string {i2} : ')
    message_list.append(original_string)
    if random_or_not == 'y' :
        return_string = ""
        i = -1
        string_length = len(original_string)
        index_counting = 0
        while index_counting != string_length:
            return_string += original_string[i]
            i -= 1
            index_counting = -(i+1)
        message_list.append(return_string)
    else :
        continue

if random_or_not == "y" :
    total_variation = message_variation_number * 2
else :
    total_variation = message_variation_number

print(f"Now {total_variation} variations of message is applied.")
print("Press ` to start or stop ( on the top left corner of your keyboard )\nPress - to quit")

keyboard = KeyboardController()
mouse = MouseController()

start_stop_key = KeyCode(char='`')
exit_key = KeyCode(char='-')

class Spamming(threading.Thread):
    def __init__(self):
        super(Spamming, self).__init__()
        self.running = False
        self.program_running = True
    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                global delay
                if time_random_or_not == "y" :
                    delay = uniform(time_random_lower_limit, time_random_upper_limit)
                    print(f"Current delay is : {delay}s")
                keyboard.type(message_list[randrange(0, total_variation)])
                time.sleep(delay)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)

spamming = Spamming()
spamming.start()

def on_press(key):
    if key == start_stop_key:
        if spamming.running:
            spamming.stop_clicking()
        else:
            spamming.start_clicking()
    elif key == exit_key:
        spamming.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
