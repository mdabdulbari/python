from stack import Stack

def test_push():
    p = Stack()
    p.push(2)
    if (p.pop() == 2):
        return True
    else:
        return False