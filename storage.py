class Pointers:

    def __init__(self):
        self.queue = [(0,0)]

    def enqueue(self,datapoint):
        self.queue.append(datapoint)
        return True
    
    def dequeue(self):
        return self.queue.pop(0)

    # def move_snake_pointers(self,datapoint):
    #     self.dequeue()
    #     self.enqueue(datapoint)

    def pointers(self):
        return self.queue

# x = pointers()
# for i in range(1,6):
#     x.enqueue(i)