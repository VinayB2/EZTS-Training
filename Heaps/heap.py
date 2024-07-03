class Heap:
    def __init__(self):
        self.heap = []
    def parent(self, idx):
        return idx // 2
    def leftChild(self, idx):
        return idx * 2
    def rightChild(self,idx):
        return idx * 2 + 1
    
    