import tkinter
from game_field import GameField

game = GameField()
window = tkinter.Tk()

def draw():
    for row_num, row in enumerate(game.game_field):
        for col_num, element in enumerate(row):
            label = tkinter.Label(
                text=str(element),
            )
            label.grid(row=row_num, column=col_num)

def handle(event):
    if event.keysym == "Up":
        game.up()
    if event.keysym == "Down":
        game.down()
    if event.keysym == "Left":
        game.left()
    if event.keysym == "Right":
        game.right()
    draw()

def down(event):
    game.down()
    draw()

# Bind keypress event to handle_keypress()
window.bind("<Up>", handle)
window.bind("<Down>", handle)
window.bind("<Right>", handle)
window.bind("<Left>", handle)

draw()
window.mainloop()

