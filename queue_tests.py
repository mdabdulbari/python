from queue import Queue

def test_queue():
    p = Queue()
    p.enqueue(1)
    p.enqueue(2)
    assert p.dequeue() == 1
    assert p.dequeue() == 2

def test_peek():
    p = Queue()
    p.enqueue(1)
    p.enqueue(2)
    assert p.peek() == 1