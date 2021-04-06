from copy import deepcopy
import tkinter as tk

class cell:
	def __init__(self):
		pass

class gameofLife(tk.Canvas):
	def __init__(self,width,height):

		self.Height = height
		self.Width = width
		self.GRID = None

		super().__init__(width=self.Width, height=self.Height, background="white", highlightthickness=0)
		
		self.Create_New_Grid(self.Height, self.Width)

	def Create_New_Grid(self, height, width):
		print("Creating Grid...")
		self.GRID = [[0 for i in range(width)] for j in range(height)]
		print("Done.")
		for line in self.GRID:
			print(line)

class instance:
	def __init__(self,width,height):


		self.root = tk.Tk()
		self.root.title("Game of life")
		self.root.resizable(False,False)

		self.Height = height
		self.Width = width

		
		self.Game = gameofLife(width,height)
		self.Game.pack()

	def run(self):
		self.root.mainloop()