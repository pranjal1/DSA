import ctypes


class MyArray(object):
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 1
        self.data = self._create_arr(self.capacity)

    def _create_arr(self, capacity):
        return (capacity * ctypes.py_object)()

    def list(self):
        return "[" + ", ".join(self.data[i] for i in range(self.length)) + "]"

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.length:
            raise Exception("Incorrect index!")
        return self.data[idx]

    def push(self, item):
        if self.length == self.capacity:
            self._enlarge_array(2 * self.capacity)
        self.data[self.length] = item
        self.length += 1

    def _enlarge_array(self, new_capacity):
        new_arr = self._create_arr(new_capacity)
        for i in range(self.length):
            new_arr[i] = self.data[i]

        self.data = new_arr
        self.capacity = new_capacity

    def delete(self, idx):
        if idx < 0 or idx >= self.length:
            raise Exception("Index error!")
        for i in range(self.length - idx - 1):
            self.data[idx + i] = self.data[idx + 1 + i]
        self.length -= 1


if __name__ == "__main__":
    arr = MyArray()
    print(len(arr))
    arr.push("a")
    print(arr.list())
    arr.push("b")
    print(arr.list())
    arr.delete(1)
    print(arr.list())
    arr.delete(0)
    print(arr.list())
