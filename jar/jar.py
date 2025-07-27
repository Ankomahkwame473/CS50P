class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self._size = self._size + n
        if self._size > self._capacity:
            raise ValueError("Number of cookies exceeds the capacity of the jar")
        return self._size

    def withdraw(self, n):
        self._size = self._size - n
        if self.size < 0:
            raise ValueError("Not enough cookies")
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(1)
jar.withdraw(1)
print(jar)
