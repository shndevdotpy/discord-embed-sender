import PySimpleGUI as gui
from dhooks import Webhook, Embed

'''
Author: github.com/shndevdotpy
This app makes it easy to send embed 
+ Discord style GUI
'''


gui.theme('DarkGrey14')
guiTitle = "Discord Embed Sender"

# Content
layout = [
    [gui.Text("Discord Embed Sender", text_color="#5865F2")],
    [gui.Text("Webhook Link"), gui.In("")],
    [gui.Text("Title               "), gui.In("")],
    [gui.Text("Subtitle          "), gui.In("")],
    [gui.Text("Description     "), gui.In("")],
    [gui.Button("Send", button_color="#5865F2")]

]


# Create window
window = gui.Window(guiTitle, layout)

# Variables
event, values = window.read()
webhookLink = values[0]
title = values[1]
subtitle = values[2]
description = values[3]

#embed style
embed = Embed (
    description=title, #Title
    color=0x5865F2, #Color
    timestamp="now"
)

#Webhook link
hook = Webhook(webhookLink)


embed.add_field(name=subtitle, value=description)



hook.send(embed=embed) #Sends embed via webhook

print("Embed send successful!\nDetails:\nTitle: "+title+"\nSubtitle: "+subtitle+"\nDescription: "+description)



# Exit loop
while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break

window.close()
