#import tkinter as tk
from classes.layout import Layout as ly

sizeH = 600
sizeW = 750
sizeS = 150
window = ly.Window("DCID Keypress Bot", f"{sizeW}x{sizeH}")

sidebar = ly.Div(window, {
    "width": sizeS, 
    "height": sizeH, 
    "background": "#d5d5d5"
}, 'left')

container = ly.Div(window, {
    "width": sizeW - sizeS,
    "height": sizeH,
    "background": "#efefef"
}, 'right')

links = ly.Links(ly, sidebar, container, sizeW, [
    {"title": "Home", "method": "home"},
    {"title": "Configurações", "method": "configs"}
])

ly.Router( container, "home")

window.mainloop()