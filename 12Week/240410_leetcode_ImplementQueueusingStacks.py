from collections import deque

class MyQueue:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        return self.que.popleft()

    def peek(self) -> int:
        return self.que[0]
        
    def empty(self) -> bool:
        isEmpty = True
        if len(self.que) > 0:
             isEmpty = False
        return isEmpty
    
