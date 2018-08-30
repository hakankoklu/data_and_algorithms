"""QUESTION
Prompt: Write a function that takes the input, gives the output, and meets the conditions below.

Input: An N x M matrix of a garden. Each cell contains a positive integer representing the number of carrots in that part of the garden.

Output: The number of carrots Bunny eats before falling asleep.

Conditions: Bunny starts in the center of the garden. If there are more than one center cell, Bunny starts in the cell with the largest number of carrots. There will never be a tie for the highest number of carrots in a center cell. Bunny eats all of the carrots in his cell, then looks left, right, up, and down for more carrots. Bunny always moves to the adjacent cell with the highest carrot count. If there are no adjacent cells with carrots, Bunny falls asleep.

Example test cases:
garden1 = [[5, 7, 8, 6, 3],
[0, 0, 7, 0, 4],
[4, 6, 3, 4, 9],
[3, 1, 0, 5, 8]]

eat(garden1)
27 # starts at garden[1][2] = 7, eats 7 carrots, looks at the 8, 0, 3, and 0 adjacent, moves to the 8, repeat."""





"""I will write a small class to keep things organized a bit. This could be done with a few loose functions as well."""

class BunnyFeast:

    def __init__(self, garden):
        """Initialize with a map of the garden"""
        # Since there should be a valid center cell, I assume the garden cannot be empty
        if not garden:
            raise ValueError("Garden cannot be empty otherwise the bunny will starve!!")
        self.garden = garden

    def find_center_cell(self):
        """Get the center cell"""
        row_count = len(self.garden)
        column_count = len(self.garden[0])
        row_centers = self.get_center_indices(row_count)
        column_centers = self.get_center_indices(column_count)
        carrot_max = 0
        for i in row_centers:
            for j in column_centers:
                if self.garden[i][j] >= carrot_max:
                    carrot_max = self.garden[i][j]
                    garden_center = (i, j)
        return garden_center

    @staticmethod
    def get_center_indices(length):
        """Utility method for finding the center candidates of an array"""
        if length % 2 == 1:
            return [length // 2]
        else:
            return [length // 2 - 1, length // 2]

    def get_max_neighbor(self, current_cell):
        """current_cell is a tuple (row_index, column_index)
        returns a tuple with the next coordinates as a tuple and the number of carrots there
        """
        carrot_max = 0
        r = current_cell[0]
        c = current_cell[1]
        next_cell = None
        # top
        if r > 0 and self.garden[r - 1][c] > carrot_max:
            next_cell = (r - 1, c)
            carrot_max = self.garden[r - 1][c]
        # bottom
        if r < len(self.garden) - 1 and self.garden[r + 1][c] > carrot_max:
            next_cell = (r + 1, c)
            carrot_max = self.garden[r + 1][c]
        # left
        if c > 0 and self.garden[r][c - 1] > carrot_max:
            next_cell = (r, c - 1)
            carrot_max = self.garden[r][c - 1]
        # right
        if c < len(self.garden[0]) - 1 and self.garden[r][c + 1] > carrot_max:
            next_cell = (r, c + 1)
            carrot_max = self.garden[r][c + 1]
        return next_cell, carrot_max

    def eat(self):
        """Starts from the center and travels the garden until it ends up at a cell with no carrots around."""
        start = self.find_center_cell()
        total = self.garden[start[0]][start[1]]  # start by eating the center
        self.garden[start[0]][start[1]] = 0  # set the eaten part to 0
        next_neighbor = self.get_max_neighbor(start)
        while next_neighbor[1] > 0:
            total += next_neighbor[1]
            self.garden[next_neighbor[0][0]][next_neighbor[0][1]] = 0  # set the eaten part to zero
            next_neighbor = self.get_max_neighbor(next_neighbor[0])
        return total


def eat(garden):
    bf = BunnyFeast(garden)
    return bf.eat()

garden1 = [[5, 7, 8, 6, 3],
[0, 0, 7, 0, 4],
[4, 6, 3, 4, 9],
[3, 1, 0, 5, 8]]
print(eat(garden1))