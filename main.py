import os
import pprint
import pygame
import threading
from tkinter import *
from tkinter.ttk import Progressbar
import time

from PIL import Image, ImageTk


image = Image.open('wheel.png')


ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x150')
ws.config(bg='#345')




st = Tk()
st.title("wheel")
st.geometry('200x200')
st.configure(bg='#345')


bg = '#345'

fg = '#fff'

stearingOffset = 45

throttleGraph = Progressbar(ws, orient=VERTICAL, length=100, mode='determinate')
throttleGraph.place(x=118, y=stearingOffset)


brakeGraph = Progressbar(ws, orient=VERTICAL, length=100, mode='determinate')
brakeGraph.place(x=79, y=stearingOffset)

clutchGraph = Progressbar(ws, orient=VERTICAL, length=100, mode='determinate')
clutchGraph.place(x=40, y=stearingOffset)

wheelGraph = Progressbar(ws, orient=HORIZONTAL, length=100, mode='determinate')
wheelGraph.place(x=40, y=20)

throttleLable = Label(ws, text="\n".join("Go Go"),bg=bg, fg=fg )
throttleLable.place(x=140,y=stearingOffset)

brakeLable = Label(ws, text="\n".join("Brakes"),bg=bg, fg=fg )
brakeLable.place(x=103,y=stearingOffset)

clutchLable = Label(ws, text="\n".join("Clutch"),bg=bg, fg=fg )
clutchLable.place(x=63,y=stearingOffset)


def test():
    print("test")


# Button(ws, text='Start', command=step).place(x=40, y=50)

# Button(ws, text='Test', command=test()).place(x=80, y=50)


def map( x,  in_min,  in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""

        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        while True:
            ws.update()
            pygame.event.get()


              # Insert your code on what you would like to happen for each event here!
            # In the current setup, I have the state simply printing out to the screen.
            #3 clutch
            #2 gas
            #1 brake
            #0 wheel


            wheelGraph['value'] = map(pygame.joystick.Joystick(0).get_axis(0), -1, 1,0, 100)
            throttleGraph['value'] = map(pygame.joystick.Joystick(0).get_axis(2), -1, 1,100, 0)
            brakeGraph['value'] = map(pygame.joystick.Joystick(0).get_axis(1), -1, 1,100, 0)
            clutchGraph['value'] = map(pygame.joystick.Joystick(0).get_axis(3), -1, 1,100, 0)
            ws.update()

             

            os.system('cls')
            print(map(pygame.joystick.Joystick(0).get_axis(0), -1, 1,100, 0))
            print(map(pygame.joystick.Joystick(0).get_axis(1), -1, 1,100, 0))
            print(map(pygame.joystick.Joystick(0).get_axis(2), -1, 1,100, 0))
            print(map(pygame.joystick.Joystick(0).get_axis(3), -1, 1,100, 0))
            pprint.pprint(self.button_data)
            pprint.pprint(self.axis_data)
            pprint.pprint(self.hat_data)


def controller_main():
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()


controller_main()
