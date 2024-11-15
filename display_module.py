"""
Project: EV-DataLogger
Author: Walker Poyner, Alex Burns
"""

import tkinter as tk
from tkinter import ttk
import math
import sys
root = tk.Tk()

"""
What needs to be put on the screen:
 - MPH
    - keep this simple, just mph
 - Current Battery percentage
    - not just basic progressbar, include markers and labels
    - change color depending on deviation from norm?
    - decide if progressbar should be vertical or horizontal
 - Recharge potential (get clairification from Taylor)
    - just figure out what this is even supposed to be
    - how much breaking for X seconds could recharge?
 - Rear tire temps
    - vertical progress bars (if we have nothing else to do we could make them tire shaped)
"""

class Gauge (tk.Canvas):
    _current_value = 0
    _commanded_value = 0
    _needle_width = 10
    _needle_color = "red"
    _angle = 0
    _needle_length = 10
    _bounds = [0, 80]
    _dial_origin_coords = [0,0]
    _dial_target_coords = [0,0]
    _animation_speed = 30 # Lower number is faster
    _dialmovement_start = False
    _value_reporter_method = lambda : True

    def __init__(self,tk_parent, value_range = _bounds, needle_width=_needle_width, needle_color=_needle_color, needle_length=_needle_length, **kwargs):
        super().__init__(tk_parent,width=needle_length * 3, height=needle_length*1.5 ,**kwargs)
        self._dial_origin_coords = (self.winfo_reqwidth()/2, self.winfo_reqheight() * 0.95)
        self._needle_length = needle_length
        self._needle_width = needle_width
        self._needle_color = needle_color
        self._bounds = value_range
        self._needle_ref = 0
        #self.setValue(0)
        #self.drawNeedle()

        # not needed
        self._arc_ref = self.create_arc(
            self._dial_origin_coords[0]-self._needle_length,
            self._dial_origin_coords[1]-self._needle_length,
            self._dial_origin_coords[0]+self._needle_length,
            self._dial_origin_coords[1]+self._needle_length,
            width = self._needle_width, 
            outline = self._needle_color,
            style = "arc",
            dash=(20,10,3,10),
            extent = 180,
            )

    # not needed
    def drawNeedle(self,value):
        self._current_value = value
        self._angle = math.pi - ((math.pi/self._bounds[1]) * self._current_value)
        self._target_coords = [(math.cos(self._angle))*(self._needle_length)+self._dial_origin_coords[0],self._dial_origin_coords[1]-(math.sin(self._angle))*(self._needle_length)]
        self.delete(self._needle_ref)
        self._needle_ref = self.create_line(
            self._dial_origin_coords[0],
            self._dial_origin_coords[1],
            self._target_coords[0],
            self._target_coords[1],
            width = self._needle_width, 
            fill = self._needle_color)

    # TODO: make widely applicable for all data
    def autoUpdate(self):
        self._commanded_value = self._value_reporter_method()
        self.drawNeedle_animate()
        self.after(100, self.autoUpdate)

    # not needed
    def drawNeedle_animate(self):
        if self._current_value == self._commanded_value:
            self._dialmovement_start = False
            return
        self.drawNeedle(self._current_value + (1 if self._commanded_value > self._current_value else (-1)))
        self._animation_speed = 12//(((self._commanded_value+1)//(self._current_value+1)) if (self._commanded_value > self._current_value) else ((self._current_value +1)//(self._commanded_value+1)))
        super().after(self._animation_speed, self.drawNeedle_animate)

# will have to restructure to not have gauge     
def update_mph(gauge, label, mph):
    gauge.after(0,)

# will need major reworks when we can connect to the SEVCON
def get_mph():
    mph = int(input("Enter mph: "))
    mph_variable.set(mph)
    return mph

# THIS IS ALL FORMATING FOR TKINTER NOT CUSTOM TKINTER
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(root.winfo_screenwidth(),root.winfo_screenheight())
s= ttk.Style()
s.configure("TFrame",background="black")
main_frame = ttk.Frame(root, padding="4 4 10 10")
main_frame.grid(row=0,column=0)
main_frame.configure()

# MPH variable
mph_variable = tk.IntVar(root)

label1 = ttk.Label(main_frame, text="54 MPH", textvariable=mph_variable) # why 54????
label1.configure(font=("Helvetica",72,),foreground='red',background='black', padding="8 0 8 8")
label1.grid(row=1, column=1,)

# why is this hardcoded
label2 = ttk.Label(main_frame, text = "(x,y)")
label2.configure(font=("Helvetica",72,),foreground='red',background='black', padding="8 4 8 4")
label2.grid(row=3, column=1)
label2 = ttk.Label(main_frame, text = "140 V")
label2.configure(font=("Helvetica",72,),foreground='red',background='black', padding="0 0 0 0")
label2.grid(row=2, column=1)

# create gauge
# not needed
gauge1 = Gauge(main_frame, needle_length=200, background="black",value_range =[0,100])
gauge1.grid(column=0, row=2)

# create battery progressbar
# absolutely not.
progressbar = ttk.Progressbar(orient=tk.VERTICAL)
progressbar.place(x=30, y=30, height=160)

# update needle values
# yes but dude no gauge
gauge1.drawNeedle(0)
gauge1._value_reporter_method = get_mph

# Update all info
gauge1.autoUpdate() # TODO: make autoUpdate global and applicable for all data

# loop and destroy window if there are 80 seconds without updates
tk.mainloop()
root.after(80000, lambda: root.destroy()) # why