#import tkinter as tk
from classes.layout import Layout as ly

sizeH = 600
sizeW = 750
sizeNH = 50
window = ly.Window("DCID Keypress Bot", f"{sizeW}x{sizeH}")

navbarProd = {
    "width": sizeW, 
    "height": sizeNH, 
    "background": "#dfdfdf"
}
navbar = ly.Div(window, navbarProd, 'top')

containerProp = {
    "width": sizeW,
    "height": sizeH - sizeNH,
    "background": "#e2e2e2"
}
container = ly.Div(window, containerProp, 'top')

linksData = [
    {"title": "Home", "method": "home"},
    {"title": "Configurações", "method": "configs"}
]
links = ly.Links(ly, { 
    "side_in": navbar, 
    "side_out": container, 
    "sizeW": sizeW,
    "links": linksData
})

ly.Router( container, "home")

window.mainloop()