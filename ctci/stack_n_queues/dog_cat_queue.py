"""An animal shelter holds dogs and cats and operated on a FIFO basis. You can either adopt the animal that has been
there the longest or you can specify if you want a dog or a cat and get the animal of your preferred type that has been
there the longest. Implement enqueue, dequeueAny, dequeueDog and dequeueCat.
You can use a built in LinkedList from your language."""

class Node:

    def __init__(self, name, animal, prev, next):
        self.name = name
        self.animal = animal
        self.prev = prev
        self.next = next


class DogCatQueue:

    def __init__(self):
        self.dogs = []
        self.dog_turn = None
        self.cats = []
        self.cat_turn = None
        self.head = None
        self.tail = None

    def push(self, name, is_dog):
        """type True, False for dog, cat respectively"""
        if is_dog:
            self.push_dog(name)
        else:
            self.push_cat(name)

    def push_dog(self, name):
        n = Node(name, 'dog', None, None)
        self.dogs.append(n)
        if not self.head and not self.tail:
            self.head = self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        if self.dog_turn is None:
            self.dog_turn = 0

    def push_cat(self, name):
        n = Node(name, 'cat', None, self.head)
        self.cats.append(n)
        if not self.head and not self.tail:
            self.head = self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        if self.cat_turn is None:
            self.cat_turn = 0

    def dequeue_any(self):
        n = self.head
        if not n:
            ValueError("Shelter empty")
        result = n.name
        self.head = n.next
        if self.head:
            self.head.prev = None
        if n.animal == 'dog':
            self.dog_turn += 1
        else:
            self.cat_turn += 1
        return result

    def dequeue_dog(self):
        if self.dog_turn is None or self.dog_turn >= len(self.dogs):
            ValueError("No dogs available")
        if self.head.animal == 'dog':
            return self.dequeue_any()
        n = self.dogs[self.dog_turn]
        n.prev.next = n.next
        if n.next:
            n.next.prev = n.prev
        return n.name

    def dequeue_cat(self):
        if self.cat_turn is None or self.cat_turn >= len(self.cats):
            ValueError("No cats available")
        if self.head.animal == 'cat':
            return self.dequeue_any()
        n = self.cats[self.cat_turn]
        n.prev.next = n.next
        if n.next:
            n.next.prev = n.prev
        return n.name
