class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.size += 1
        self.rear = (self.rear + 1) % self.capacity
        return True

      
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        actual_idx = (self.rear - 1) % self.capacity
        print(f"self.queue = {self.queue}")
        return self.queue[actual_idx]
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False


    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        else:
            return False
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()




# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.queue = [0] * k # 存元素的数组
#         self.capacity = k # 容量（数组大小）
#         self.size = 0 # 当前数组存了多少元素
#         self.front = 0 # 队首在哪？
#         self.rear = 0 # 下一个插入位置在哪里，不是队尾元素

#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         else:
#             self.queue[self.rear] = value
#             self.rear = (self.rear + 1) % self.capacity #用取模让指针绕回开头，防越位
#             self.size += 1
#             return True
        

#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         else:
#             self.queue[self.front] = 0
#             self.front = (self.front + 1) % self.capacity #用取模让指针绕回开头，防越位
#             self.size -= 1
#             return True
            
#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.front]
        

#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1

#         return self.queue[(self.rear-1) % self.capacity]
        

#     def isEmpty(self) -> bool:
#         if self.size == 0:
#             return True
#         else: 
#             return False
        
#     def isFull(self) -> bool:
#         if self.size == self.capacity:
#             return True
#         else:
#             return False

# # Your MyCircularQueue object will be instantiated and called as such:
# # obj = MyCircularQueue(k)
# # param_1 = obj.enQueue(value)
# # param_2 = obj.deQueue()
# # param_3 = obj.Front()
# # param_4 = obj.Rear()
# # param_5 = obj.isEmpty()
# # param_6 = obj.isFull()