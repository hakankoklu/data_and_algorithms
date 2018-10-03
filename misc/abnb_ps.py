"""Assume that you have location service that tells you all the sub-regions that comprise the
input region. For example, if you give the input as "Earth", it will give you a a list of all the
continents in the world, e.g. ["North America", "Europe", ...]. Or if you put in "United States",
it’ll return the states ["California", "Oregon", ...].

Given two regions, write a method that returns the smallest region that includes both
inputs. For example, "California" and "Mexico" should return "North America". Or "San Francisco"
and "Virginia" should return "United States".

"""

# first column of each row is enclosing region, and following columns
# are all the regions within that row


# values = [['Earth', 'North America', 'South America'],
#           ['North America', 'Mexico', 'United States', 'Canada'],
#           ['South America', 'Argentina', 'Brazil', 'Chile'],
#           ['Mexico', 'Oaxaca', 'Puebla'],
#           ['United States', 'California', 'Wyoming', 'New York'],
#           ['Canada', 'Ontario', 'Quebec', 'Saskatchewan']]


# def make_path_dict(values):
#     result = {}
#     for arr in values:
#         for elm in arr[1:]:
#             result[elm] = arr[0]
#     return result
#
#
# def get_root_path(value, path_dict):
#     current = value
#     path = []
#     while current !=:
#         path.append(current)
#         current = path_dict[current]
#     path.append('Earth')
#     return path
#
#
# def find_smallest_region(inp1, inp2, values):
#     path_dict = make_path_dict(values)
#     path1 = get_root_path(inp1, path_dict)
#     path2 = get_root_path(inp2, path_dict)
#     path1.reverse()
#     path2.reverse()
#     result = 'Earth'
#     for r1, r2 in zip(path1, path2):
#         if r1 == r2:
#             result = r1
#         else:
#             break
#     return result
#
#
# tests = [['California', 'Mexico'], ['Quebec', 'North America'], ['New York', 'Chile']]
# for inp1, inp2 in tests:
#     print(find_smallest_region(inp1, inp2, values))


###### AFTERWARDS #######


class SubRegionFinder:

    def __init__(self, values):
        self.values = values
        self.parent_dict = self.set_path_dict()
        self.root = self.set_root()

    def set_path_dict(self):
        result = {}
        for arr in self.values:
            for elm in arr[1:]:
                result[elm] = arr[0]
        return result

    def set_root(self):
        current = self.values[0][0]
        while self.parent_dict.get(current) is not None:
            current = self.parent_dict[current]
        return current

    def get_root_path(self, value):
        current = value
        path = []
        while current != self.root:
            path.append(current)
            current = self.parent_dict[current]
        path.append(self.root)
        return path

    def find_smallest_region(self, *regions):
        paths = []
        for region in regions:
            path = self.get_root_path(region)
            path.reverse()
            paths.append(path)
        result = self.root
        for subregions in zip(*paths):
            first = subregions[0]
            if all([x == first for x in subregions]):
                result = first
            else:
                break
        return result


if __name__ == '__main__':
    values = [['Earth', 'North America', 'South America'],
              ['North America', 'Mexico', 'United States', 'Canada'],
              ['South America', 'Argentina', 'Brazil', 'Chile'],
              ['Mexico', 'Oaxaca', 'Puebla'],
              ['United States', 'California', 'Wyoming', 'New York'],
              ['Canada', 'Ontario', 'Quebec', 'Saskatchewan']]
    tests = [['California', 'Mexico'], ['Quebec', 'North America', 'United States'], ['New York', 'Chile']]
    sf = SubRegionFinder(values)
    for inps in tests:
        print(sf.find_smallest_region(*inps))
