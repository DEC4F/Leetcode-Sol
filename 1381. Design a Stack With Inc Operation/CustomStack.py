"""
Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.
"""


class CustomStackLazy:

    def __init__(self, maxSize: int):
        self.stack = []
        self.n = maxSize
        self.inc = []

    def push(self, x: int) -> None:
        """
        T(n) = O(1)
        """
        if len(self.stack) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        """
        T(n) = O(1)
        ----------
        when popped, propagate the change down the inc array, since only ele before k will be affected
        """
        if not self.inc:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        """
        T(n) = O(1)
        ----------
        increment the val at kth position
        """
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val


class CustomStackVanilla:

    def __init__(self, maxSize: int):
        self.stack = []
        self.n = maxSize

    def push(self, x: int) -> None:
        """
        T(n) = O(1)
        """
        if len(self.stack) < self.n:
            self.stack.append(x)

    def pop(self) -> int:
        """
        T(n) = O(1)
        """
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        """
        T(n) = O(K)
        """
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
