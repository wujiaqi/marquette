#Node class which defines the state of the game
class Node:
	def __init__(self, state, parent = None):
		self.state = state
		self.parent = parent

	def __makeChildNode(self, swap_index, empty_index):
		#returns a child node
		child_state = list(self.state)
		child_state[empty_index], child_state[empty_index + swap_index] = child_state[empty_index + swap_index], child_state[empty_index]
		child_node = Node(child_state, self)
		return child_node

	def print_node(self):
		print "===Game State==="
		for y in xrange(0,3):
			print self.state[3 * y] if self.state[3 * y] != 0 else " ",
			print self.state[3 * y + 1] if self.state[3 * y + 1] != 0 else " ",
			print self.state[3 * y + 2] if self.state[3 * y + 2] != 0 else " "
		print ""

	def expand(self):
		expansion = []
		empty_slot = self.state.index(0)
		if empty_slot > 3:
			expansion.append(self.__makeChildNode(-3, empty_slot))
		if empty_slot < 6:
			expansion.append(self.__makeChildNode(3, empty_slot))
		if empty_slot != 0 and empty_slot != 3 and empty_slot != 6:
			expansion.append(self.__makeChildNode(-1, empty_slot))
		if empty_slot != 2 and empty_slot != 5 and empty_slot != 8:
			expansion.append(self.__makeChildNode(1, empty_slot))
		return expansion

	def get_path():
		return None

def tree_search(initial_node, goal):
	fringe = initial_node.expand()
	while True:
		if len(fringe) == 0:
			return -1
		node = fringe.pop()
		node.print_node()
		if node == goal:
			return node
		fringe.extend(node.expand())

start = [8,7,6,5,4,3,2,1,0]
goal = [1,2,3,4,5,6,7,8,0]

start_node = Node(start)
for x in start_node.expand():
	x.print_node()

#goal = tree_search(Node(start), Node(goal))

"""if goal == -1:
	print "no solution"
else:
	goal.print_node();"""


