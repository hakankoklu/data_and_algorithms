"""Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);"""


class PhoneDirectory:

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.size = maxNumbers
        self.free_nums = set()
        self.used_nums = set()
        self.last_used = -1

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.free_nums:
            id = self.free_nums.pop()
            self.used_nums.add(id)
            return id
        if self.last_used + 1 < self.size and self.last_used + 1 not in self.used_nums:
            self.last_used += 1
            id = self.last_used
            self.used_nums.add(id)
            return id
        return -1

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number in self.used_nums:
            self.used_nums.remove(number)
            self.free_nums.add(number)

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number not in self.used_nums

