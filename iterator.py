nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator(list):

    def __iter__(self):
        self.cursor = 0
        self.inner_cursor = -1
        return self

    def __next__(self):
        self.inner_cursor += 1
        if len(self)-1 == self.cursor and len(self[self.cursor]) == self.inner_cursor:
            raise StopIteration
        if len(self[self.cursor]) == self.inner_cursor:
            self.cursor += 1
            self.inner_cursor = 0
        return self[self.cursor][self.inner_cursor]


for item in FlatIterator(nested_list):
    print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)