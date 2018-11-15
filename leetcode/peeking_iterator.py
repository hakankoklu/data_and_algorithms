

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peek_buffer = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peek_buffer:
            self.peek_buffer = self.iterator.next()
        return self.peek_buffer

    def next(self):
        """
        :rtype: int
        """
        if self.peek_buffer:
            result = self.peek_buffer
            self.peek_buffer = None
        else:
            result = self.iterator.next()
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peek_buffer is not None or self.iterator.hasNext()
