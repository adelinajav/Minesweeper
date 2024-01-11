from tkinter import *
import settings
import utils
from cell import Cell



root =Tk()
root.configure(bg = 'black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg = 'black',
    width = settings.WIDTH,
    height = utils.height_perc(25)
)

left_frame = Frame(
    root,
    bg = 'black',
    width = utils.width_perc(25),
    height = utils.height_perc(75)
)

centre_frame = Frame(
    root,
    bg = 'black',
    width = utils.width_perc(75),
    height = utils.height_perc(75)
)


left_frame.place(x=0,y=utils.height_perc(25))
top_frame.place(x = 0, y=0)

game_title = Label(
    top_frame,
    bg = 'black',
    fg = 'white',
    text = 'Minsweeper Game',
    font = ('', 48)
)

game_title.place(
    x = utils.width_perc(35),
    y = 0
)

centre_frame.place(x = utils.width_perc(25), y = utils.height_perc(25))


for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn(centre_frame)
        c.cell_obj.grid(
            column = y,
            row = x
        )

Cell.label(left_frame)
Cell.count_label.place(
    x=0,
    y=0)
Cell.randmines()
for c in Cell.all:
    print(c.ismine)

root.mainloop()
