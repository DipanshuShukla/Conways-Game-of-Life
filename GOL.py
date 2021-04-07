from copy import deepcopy
import tkinter as tk
import random

class cell:
	def __init__(self):
		pass

class gameofLife(tk.Canvas):
	def __init__(self,width,height):

		self.Height = height
		self.Width = width
		self.GRID = None

		self.speed = 100
		
		
		self.border = 20
		self.scale = 38

		self.shape_Grid = [[None for i in range(self.scale)] for j in range(self.scale)]

		self.draw_space_width = self.Height-2*(self.Height/self.border)

		self.cell_width = self.draw_space_width/self.scale

		super().__init__(width=self.Width, height=self.Height, background="white", highlightthickness=0)
		
		self.Create_New_Grid(self.Height, self.Width)


		self.after(self.speed, self.update_next)

	def Create_New_Grid(self, height, width):
		print("Creating Grid...")

		self.GRID = [[(random.randint(0,1)) for i in range(self.scale)] for j in range(self.scale)]
		
		print("Done.")
		
		for line in self.GRID:
			print(line)

	def draw_Grid(self):
		for i in range(self.scale):
			for j in range(self.scale):
				self.shape_Grid[i][j] = self.create_rectangle(self.Width/self.border + i*self.cell_width, self.Height/self.border + j*self.cell_width, self.Width/self.border + (i+1)*self.cell_width, self.Height/self.border + (j+1)*self.cell_width, fill="black" if self.GRID[i][j] else "white",outline="white" if self.GRID[i][j] else "black", tag="cells")
		self.create_rectangle(self.Width/self.border, self.Height/self.border, self.Width/self.border + self.draw_space_width, self.Height/self.border + self.draw_space_width, width=3)

	def get_next_state(self,i,j):
		live_neighbours = 0

		for a in range(-1,2):
			for b in range(-1,2):
				if i+a >= 0 and i+a < self.scale and j+b >= 0 and j+b < self.scale and not (a==0 and b==0):
					live_neighbours = live_neighbours + self.GRID[a+i][b+j]

		if self.GRID[i][j]:

			return 1 if live_neighbours == 2 or live_neighbours == 3 else 0

		else:

			return 1 if live_neighbours == 3 else 0


	def next_instance(self):

		next_state = [[0 for i in range(self.scale)] for j in range(self.scale)]

		for i in range(self.scale):
			for j in range(self.scale):
				next_state[i][j] = self.get_next_state(i,j)

		self.GRID = next_state

		if True:

			print("/nNext State:")

			for i in self.GRID:
				print(i)

	def update_screen(self):
		for i in range(self.scale):
			for j in range(self.scale):
				self.itemconfig(self.shape_Grid[i][j], fill="black" if self.GRID[i][j] else "white",outline="white" if self.GRID[i][j] else "black")
				#self.itemconfig(self.shape_Grid[i][j], outline="white" if self.GRID[i][j] else "black")

	def update_next(self):
		self.next_instance()
		self.update_screen()
		self.after(self.speed, self.update_next)



class instance:
	def __init__(self,width,height):


		self.root = tk.Tk()
		self.root.title("Game of life")
		self.root.resizable(False,False)

		self.Height = height
		self.Width = width

		
		self.Game = gameofLife(width,height)
		self.Game.pack()
		#self.Game.create_rectangle(50, 50, self.Width-50, self.Height-50, fill="grey")
		self.Game.draw_Grid()


	def run(self):
		self.root.mainloop()