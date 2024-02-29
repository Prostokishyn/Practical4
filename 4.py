class FibonacciContainer:
    def __init__(self, n):
        self.fib_sequence = self.generate_fibonacci_sequence(n)

    def generate_fibonacci_sequence(self, n):
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    def __len__(self):
        return len(self.fib_sequence)

    def __getitem__(self, index):
        return self.fib_sequence[index]

fib_container = FibonacciContainer(10)

print("Довжина контейнера:", len(fib_container))

print("Перші 5 чисел:", fib_container[:5])