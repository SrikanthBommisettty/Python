'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None



stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())

print(stack.pop())
print(stack.pop())
print("Is stack empty:", stack.is_empty())



class Node:
  stackData = None
  nextObjAddress = None

class Stack:
 def _init_(self,inputData):
    self.data = inputData

 def is_empty(self,nodeObj):
  return (nodeObj.nextObjAddress == None)

 def push(self, inputData):
  return self.data.append(inputData)

 def pop(self):
  if not self.is_empty():
    return self.data.pop()
  else:
    raise IndexError("stack is empty")

def peek(self):
  if not self.is_empty():
    return self.data[-1]
  else:
    raise IndexError("stack is empty")

stack=Stack()

while(True):

   currObj = Stack(inputData)
   currObj.nextObjAddress = id(nextObj)
   nextObj = Stack(input)
   ObjAvailable = input("Enter Yes to Continue and No to break (Y/N)  :" )
   if(ObjAvailable == "y" or ObjAvailable == "Y") :
      newObj = Stack(inputVal)
      nextObj.nextObjAddress = id(newObj)
   else:
     nextObj.nextObjAddress = None

   nextObj.nextObjAddress = None
'''


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def main():
    details_stack = Stack()

    while True:
        print("1. Enter details")
        print("2. View last entered detail")
        print("3. Exit")
        choice = int(input("Enter your ID number: "))

        if choice == 1:
            detail = input("Enter a Name: ")
            detail = int(input("Enter the employee age"))
            detail = input("Enter the employee role")
            details_stack.push(detail)
            print("Detail entered successfully!")
        elif choice == 2:
            if not details_stack.is_empty():
                print("Last entered detail:", details_stack.peek())
            else:
                print("No details entered yet.")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
