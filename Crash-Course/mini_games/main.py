import curses
import random

# Initialisierung
screen = curses.initscr()
curses.curs_set(0)  # Maus verstecken

#getmaxyx() sie frage die Hoehe und Breite vom Fenster(Terminal) ab. z.B. 40ze, 600sp
screen_height, screen_width = screen.getmaxyx()

# Neues Fenster
window = curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1) # window erhaelt ein Input von der Tastatur
window.timeout(100) #delay in ms -> 1000ms = 1 s
#x und y Koordinate fuer den Kopf des Snakes
snk_x = screen_width /4 #500 //4 --> 125
snk_y = screen_height /2 #600 //2 -->300

#defenieren des Snakes
snake = [
    [snk_y,snk_x], #Kopf
    [snk_y,snk_x-1], #Koerperteil-1 (Bauch)
    [snk_y,snk_x-2] #Koerperteil-2 (Schweif)
]

# defenieren eines Kerns
kern =[screen_height//2,screen_width//2] #Position vom Futter !!
#      [600//2,          400//2] ---> kern[300,200] es wird in der Mitte platziert

# addch(y,x,zeichen)-> zeichnet etwas an eine Stelle 
window.addch(kern[0],kern[1],curses.ACS_DIAMOND) 

# Am Anfang bewegt sich die Schlange nach rechts
key = curses.KEY_RIGHT


while True:
    #getch() -> liest vom benutzer die naechste gedrueckte Taste
    next_key = window.getch()
    #wenn keine Taste gedrueckt wurde dann bleibe in derselben Richtung
    #wenn eine Taste  gedrueckt wurde, benutze die neue Taste
    key = key if next_key == -1 else next_key
 #  if next_key == -1: # -1 -> heisst wenn keine Input-angabe erfolgt, dann bleibt key unveraendert
 #      key =key # key bleibt unveraendert
 #  else:
 #     key = next_key
 
 if snake[0][0] in [0,screen_height] or snake[0][1] in [0][screen_width] or 
 snake[0] in sanke[1:]:
     curses.endwin() # Fenster schliessen
     quit() #Programm schliessen
    
 new_head = [snake[0][0],snake[0][1]]
if key == curses.KEY_DOWN:
    new_head[0] +=1
if key == curses.KEY_UP:
    new_head[0] -=1
   

window.refresh()  # Bildschirm aktualisieren
window.addstr(5, 10, "Hallo, das Fenster funktioniert!")  # Text anzeigen

# Auf Tastendruck warten, damit das Programm nicht sofort schliesst
window.getch()

# Beenden
curses.endwin()
