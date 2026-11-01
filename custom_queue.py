import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        return self.items[0]

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            return removed
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        rand = random.randint(0, len(self.items) - 1)
        for r in range(rand):
            winner = self.items[r]
            if winner == self.dequeue():
                return winner