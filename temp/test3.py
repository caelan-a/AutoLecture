class Grid():
	def __init__(self):
		self.rows = []
		self.row = []

		num_subject = 10
		subjects_per_row = 3

		for i in range(1, num_subject+1):
			self.row.append(i-1)
			if i % subjects_per_row == 0:
				self.rows.append(self.row)
				self.row = []
		if num_subject % subjects_per_row != 0:
			self.rows.append(self.row)

	def print(self):
		print(self.rows)

grid = Grid()
grid.print()


