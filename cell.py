import tkinter as tk
from tkinter import messagebox
from tkinter import Button, Label
import random
import settings
import ctypes
import sys



class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    count_label = None
    def __init__(self,x,y, ismine = False):
        self.ismine = ismine
        self.isopened = False
        self.candidate = False
        self.cell_obj = None
        self.x = x
        self.y = y

        ##############################################
        Cell.all.append(self)

    def create_btn(self, location):
        btn = Button(
            location,
            width = 12,
            height = 4,
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-2>', self.right_click)
        self.cell_obj = btn

    @staticmethod
    def label(location):
        lbl = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f'Cells Left: {Cell.cell_count}',
            width = 12,
            height = 4,
            font = ("", 25)
        )
        Cell.count_label = lbl

    def left_click(self, event):
        if self.ismine:
            self.showmine()
        else:
            if self.surr_len==0:
                for obj in self.surr:
                    obj.showcell()
            self.showcell()
            if Cell.cell_count == settings.MINES_COUNT:
                messagebox.showinfo('Congratulations you won !')
        self.cell_obj.unbind('<Button-1>')
        self.cell_obj.unbind('<Button-2>')


    def showmine(self):
        self.cell_obj.configure(highlightbackground='red', text='')
        messagebox.showinfo('Game Over', 'Game Over')

    def getcell(self, x, y):
        for cell in Cell.all:
            if cell.x ==x and cell.y==y:
                return cell
    @property
    def surr(self):
        cells = [
            self.getcell(self.x - 1, self.y - 1),
            self.getcell(self.x - 1, self.y),
            self.getcell(self.x - 1, self.y + 1),
            self.getcell(self.x, self.y - 1),
            self.getcell(self.x + 1, self.y - 1),
            self.getcell(self.x + 1, self.y),
            self.getcell(self.x + 1, self.y + 1),
            self.getcell(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells


    @property
    def surr_len(self):
        counter = 0
        for cell in self.surr:
            if cell.ismine:
                counter+=1
        return counter

    def showcell(self):
        if not self.isopened:
            Cell.cell_count = Cell.cell_count-1
            self.cell_obj.configure(text = self.surr_len)
            if Cell.count_label:
                Cell.count_label.configure(
                    text = f'Cells Left: {Cell.cell_count}')
            self.cell_obj.configure(
                bg = 'SystemButtonFace'
            )
        self.isopened = True

    def right_click(self, event):
        if not self.candidate:
            self.cell_obj.configure(highlightbackground='orange', text='')
            self.candidate = True
        else:
            self.cell_obj.configure(
                bg = 'SystemButtonFace'
            )
            self.candidate = False

    @staticmethod
    def randmines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.ismine = True


    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
