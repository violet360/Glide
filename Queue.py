class queue():
    def __init__(self, sz):
        self.q = []
        self.sz = sz

    def push(self, point):
        if len(self.q) == self.sz:
            (self.q).pop(0)

        self.q.append(point)

    def access(self, idx):
        return (self.q)[idx]

    def display(self):
    	print(self.q, "------")

    def get(self):
    	return (self.q)