import time
import sys
import pyautogui
print(pyautogui.size())

def right(x):
    pyautogui.dragRel(x, 0, duration = 0.01)

def left(x):
    pyautogui.dragRel(-x, 0, duration = 0.01)

def down(x):
    pyautogui.dragRel(0, x, duration = 0.01)

def up(x):
    pyautogui.dragRel(0, -x, duration = 0.01)

def rightclick(x, y):
    pyautogui.rightClick(x, y)

def leftclick(x, y):
    pyautogui.leftClick(x, y)

str = ''
while str != 'end':
    str = input("enter your value: ")
    if str != 'end':
        argv = str.split()
        input1 = argv[0]
        input2 = int(argv[1])
        if input1 == 'right':
            right(input2)
        elif input1 == 'left':
            left(input2)
        elif input1 == 'up':
            up(input2)
        elif input1 == 'down':
            down(input2)
        elif input1 == 'rightclick':
            input3 = int(argv[2])
            rightclick(input2, input3)
        elif input1 == 'leftclick':
            input3 = int(argv[2])
            leftclick(input2, input3)



