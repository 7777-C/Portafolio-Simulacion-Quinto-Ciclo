class LCGModel:
    def __init__(self, a=1664525, c=1013904223, m=2**32, seed=12345):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed
        self.state = seed

    def reset(self, new_seed=None):
        if new_seed is not None:
            self.seed = new_seed
        self.state = self.seed

    def generate_sequence(self, n=10000):
        self.reset()
        raw_values = []
        normalized_values = []

        for _ in range(n):
            self.state = (self.a * self.state + self.c) % self.m
            raw_values.append(self.state)
            normalized_values.append(self.state / self.m)

        return raw_values, normalized_values
