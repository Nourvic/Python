import curses
import random

# Initialisierung
screen = curses.initscr()
curses.curs_set(0)  # Maus verstecken
screen_height, screen_width = screen.getmaxyx()

# Neues Fenster
window = curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1) # window erhaelt ein Input von der Tastatur
window.timeout(100) #delay in ms -> 1000ms = 1 s
#x und y Koordinate fuer den Kopf des Snakes
snk-x = screen_width /4 #500 //4 --> 125
snk-y = screen_height /2 #600 //2 -->300

#defenieren des Snakes
snake = [
    [snk-y,snk-x],
    [snk-y,snk-x-1]
    [snk-y,snk-x-2]
]

# defenieren eines Kerns
kern =[screen_height//2,screen_width//2]
#      [600//2,          400//2] ---> kern[300,200]

# 
window.addch(kern[0],kern[1],curses.ACS_DIAMOND)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key= key if next_key == -1 else next_key
   """"
    if next_key == -1:
        key =key
    else:
        key = next_key
   """"
   if snake[0][0] in [0,screen_height]
   

window.refresh()  # Bildschirm aktualisieren
window.addstr(5, 10, "Hallo, das Fenster funktioniert!")  # Text anzeigen

# Auf Tastendruck warten, damit das Programm nicht sofort schliesst
window.getch()

# Beenden
curses.endwin()
