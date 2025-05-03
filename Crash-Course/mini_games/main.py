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
snk_x = screen_width //4 #500 //4 --> 125
snk_y = screen_height //2 #600 //2 -->300

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
    # Eingabe vom Benutzer holen
    next_key = window.getch()
    # Wenn keine Taste gedrückt -> gleiche Richtung behalten
    # Wenn Taste gedrückt -> neue Richtung nehmen
    key = key if next_key == -1 else next_key

    # Überprüfen, ob die Schlange an die Wand stößt oder sich selbst berührt
    if snake[0][0] == 0 or snake[0][0] == screen_height - 1 or snake[0][1] == 0 or snake[0][1] == screen_width - 1 or snake[0] in snake[1:]:       
        curses.endwin()  # Curses-Fenster schließen
        quit()           # Programm beenden

    # Neue Position des Kopfes erzeugen (alte Kopfposition kopieren)
    new_head = [snake[0][0], snake[0][1]]

    # Richtung ändern je nach gedrückter Taste
    if key == curses.KEY_DOWN:
        new_head[0] += 1   # Y-Koordinate größer → nach unten
    if key == curses.KEY_UP:
        new_head[0] -= 1   # Y-Koordinate kleiner → nach oben
    if key == curses.KEY_RIGHT:
        new_head[1] += 1   # X-Koordinate größer → nach rechts
    if key == curses.KEY_LEFT:
        new_head[1] -= 1   # X-Koordinate kleiner → nach links

    # Neues Kopfstück der Schlange vorne einfügen
    snake.insert(0, new_head)

    # Prüfen, ob die Schlange das Futter gefressen hat
    if snake[0] == kern:
        kern = None  # Das alte Futter wird gelöscht

        # Neues Futter erzeugen, das nicht auf dem Körper liegt
        while kern is None:
            new_kern = [
                random.randint(1, screen_height - 1),  # Zufällige Y-Position
                random.randint(1, screen_width - 1)    # Zufällige X-Position
            ]
            # Nur akzeptieren, wenn das neue Futter nicht auf der Schlange ist
            kern = new_kern if new_kern not in snake else None

        # Neues Futter zeichnen
        window.addch(kern[0], kern[1], curses.ACS_DIAMOND)

    else:
        # Wenn kein Futter gegessen wurde: Schwanz der Schlange löschen
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    # Neuen Kopf der Schlange zeichnen
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
