# 10828

from sys import stdin
"14",
"push 1",
"push 2",
"top",
"size",
"empty",
"pop",
"pop",
"pop",
"size",
"empty",
"pop",
"push 3",
"empty",
"top",
class Test():
	s = ["14",
		"push 1",
		"push 2",
		"top",
		"size",
		"empty",
		"pop",
		"pop",
		"pop",
		"size",
		"empty",
		"pop",
		"push 3",
		"empty",
		"top"]
	c = -1

	def readline():
		Test.c += 1
		return Test.s[Test.c]

class Stack():
	def __init__(self):
		self.stack = list()

	def push(self, value: int)-> None:
		self.stack.append(value)


	def pop(self)-> int:
		if self.empty() :
			return -1
		else:
			value = self.stack[-1]
			self.stack = self.stack[:-1]
			return value

	def size(self)-> int:
		return len(self.stack)

	def empty(self)-> int:
		return 0 if self.size() > 0 else 1

	def top(self)-> int:
		return -1 if self.empty() else self.stack[-1]



def main(inputInterface):

	stack = Stack()

	N = int(inputInterface.readline())
	for i in range(N):
		m = list(inputInterface.readline().split())

		if m[0] == "push":
			stack.push(m[1])
		elif m[0] == "pop":
			print(stack.pop())
		elif m[0] == "size":
			print(stack.size())
		elif m[0] == "empty":
			print(stack.empty())
		elif m[0] == "top":
			print(stack.top())

main(Test)