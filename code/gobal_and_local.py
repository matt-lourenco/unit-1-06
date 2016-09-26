# Created by: Matthew Lourenco
# Created on: 23 Sept 2016
# This program is a program that shows the difference between local and global variables

import ui

variableX = 25

def local_touch_up_inside(sender):
    #shows how local variables work
    
    variableX = 10
    variableY = 30
    variableZ = variableX + variableY
    
    view['local_label'].text = str(variableZ)

def global_touch_up_inside(sender):
    #shows how global variables work
    
    global variableX
    variableX = variableX + 1
    variableY = 30
    variableZ = variableX + variableY
    
    view['global_label'].text = str(variableZ)

view = ui.load_view()
view.present('full_screen')
