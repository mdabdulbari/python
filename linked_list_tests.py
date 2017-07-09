from linked_list import LinkedList

def test_element_at_beginning():
    p = LinkedList()
    p.insert(0, 1)
    assert p.element_at(0) == 1

def test_element_at():
    p = LinkedList()
    p.insert(0,1)
    p.insert(1,2)
    assert p.element_at(1) == 2

def test_insert_at_beginning():
    p = LinkedList()
    p.insert(0,3)
    assert p.element_at(0) == 3

def test_length():
    p = LinkedList()
    p.insert(0,1)
    p.insert(1,2)
    assert len(p) == 2

def test_contains_when_it_exists():
    p = LinkedList()
    p.insert(0,1)
    assert (1 in p) == True

def test_contains_when_element_does_not_exist():
    p = LinkedList()
    p.insert(0,1)
    assert (3 in p) == False

def test_insert():
    p = LinkedList()
    p.insert(0,3)
    p.insert(1,2)
    p.insert(2,3)
    p.insert(1,4)
    assert p.element_at(1) == 4
    assert p.element_at(2) == 2

def test_iter():
    p = LinkedList()
    p.insert(0,1)
    p.insert(1,2)
    p.insert(2,3)
    l = []
    for e in p:
        l.append(e)
    assert l == [1,2,3]