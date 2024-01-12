import PySimpleGUI as sg

sg.theme('Dark Grey 13')

layout = [[sg.Text('Please upload your file here')],

          [sg.Input(), sg.FileBrowse()],

          [sg.OK(), sg.Cancel()]]

window = sg.Window('Hello Softwarica', layout)

event, values = window.read()

window.close()