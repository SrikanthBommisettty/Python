

class Stack:
   def __init__(self):
      self.stack = []

   def add(self, dataval):

      if dataval not in self.stack:
         self.stack.append(dataval)
         return True
      else:
         return False

   def peek(self):
	   return self.stack[-1]

  # while(True):


AStack = Stack()
AStack.add("jan")
AStack.add("feb")
AStack.add("mar")
AStack.add("April")
print(AStack.peek())



class Queue:
   def __init__(self):
      self.queue = list()

   def addtoq(self,dataval):

       if dataval not in self.queue:
         self.queue.insert(0,dataval)
         return True
         return False

   def size(self):
      return len(self.queue)


TheQueue = Queue()
TheQueue.addtoq("10")
TheQueue.addtoq("20")
TheQueue.addtoq("30")
TheQueue.addtoq("40")
TheQueue.addtoq("50")
print(TheQueue.size())
