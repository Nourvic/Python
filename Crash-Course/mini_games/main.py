import curses
import random

# Initialisierung
screen = curses.initscr()
curses.curs_set(0)  # Maus verstecken
screen_height, screen_width = screen.getmaxyx()

# Neues Fenster
window = curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1) # window erhaelt ein Input von der Tastatur
window.timeout(100) #delay in ms -> 100ms = 1 s
snk-x = screen_width /4
snk-y = screen_height /2 



window.refresh()  # Bildschirm aktualisieren
window.addstr(5, 10, "Hallo, das Fenster funktioniert!")  # Text anzeigen

# Auf Tastendruck warten, damit das Programm nicht sofort schliesst
window.getch()

# Beenden
curses.endwin()
