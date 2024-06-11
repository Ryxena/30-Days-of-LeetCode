class Example:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

    def display(self):
        print(f"The value is: {self.value}")

# Membuat instance dari kelas Example
example_instance = Example(5)

# Memanggil metode increment
example_instance.increment()

# Memanggil metode display
example_instance.display()


