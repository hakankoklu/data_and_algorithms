Implement
a
data
structure
that
affords
the
following
interface.

public


class SpacePanorama {
public SpacePanorama(int numRows, int numCols) {
// initializes the data structure.numRows x numCols is the sector layout.
// numRows, numCols can be as large as 1K each.
}

public void update(int row, int col, Image image) {
// The Hubble will occasionally call this (via some radio wave communication)
// to report new imagery for the sector at a particular row and col
// Images can be up to 1MB in size.
}

public Image fetch(int row, int col) {
// NASA will occasionally call this to check the view of a particular sector.


return null;
}
}
You
can
assume
that
the  # of rows and columns will be at most 1K (i.e. 1K x 1K grid of sectors.)


class Image:

    def __init__(self, path):
        self.path = path

    def write(self, image_bitmap):

    def read(self):


class Node:

    def __init__(self, path, timestamp):
        self.path = path
        self.timestamp = timestamp
        self.prev = None
        self.next = None


class SpacePanorama:

    def __init__(self, num_rows, num_cols):
        self.head = self.tail = None
        self.root_path = "/home/space"
        self.path_matrix = []
        row = [None] * num_cols
        for _ in num_rows:
            self.path_matrix.append(row[:])

    def update(row, col, image):
        if 0 <= row < len(self.path_matrix) and 0 <= col < len(self.path_matrix[0]):
            if not self.path_matrix[row][col]:
                new_name = "image_" + str(row) + "_"
                str(col)
                new_path = os.path.join(self.root_path, new_name)
                ts = datetime.datetime.utcnow()
                node = Node(new_path, ts)
                self.path_matrix[row][col] = node
                if not self.head:
                    self.head = self.tail = node
                else:
                    self.head.next = node
                    node.prev = self.head
                    self.head = node
            else:
                node = self.path_matrix[row][col]
                if node != self.tail and node != self.head:
                    node_prev = node.prev
                    node_next = node.next
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.head.next = node
                    node.prev = self.head
                    node.next = None
                    self.head = node
                elif node == self.tail:
                    self.tail = node.next
                    self.tail.prev = None
                    self.head.next = node
                    node.prev = self.head
                    node.next = None
                    self.head = node
            image_obj = Image(node.path)
            image_obj.write(image)
        else:
            raise ValueError("Out of bounds!")

    def fetch(row, col):
        if 0 <= row < len(self.path_matrix) and 0 <= col < len(self.path_matrix[0]):
            if not self.path_matrix[row][col]:
                raise ValueError("No image for this sector!")
            else:
                node = self.path_matrix[row][col]
                image_obj = Image(node.path)
                return image_obj.read()
        else:
            raise ValueError("Out of bounds!")

    def get_stalest_sector(self):
        if not self.tail:
            ValueError("No image yet")
        image_obj = Image(self.tail.path)
        return image_obj.read()


"""no rows n
cols m

n*m

n, m

m*n-1 + m
path: path to the serialized linked list node

"""