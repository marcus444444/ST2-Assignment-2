class Queue:
    def __init__(self):
        self.items = []
        stack = []
        positions = []
        target_positions = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    

    
    def update_animation(self, positions):
        panel_top = HEIGHT - 100

        for i in range(len(positions)):
            target_y = panel_top - (i + 1) * (BLOCK_HEIGHT + 5)

            positions[i] += (target_y - positions[i]) * 0.2