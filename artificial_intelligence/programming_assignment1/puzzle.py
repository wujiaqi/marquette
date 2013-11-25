import math

#Node class which defines the state of the game
class Node:
	#ctor
	def __init__(self, state, parent = None, cost = 0):
		self.state = state
		self.parent = parent
		self.cost = cost

	#produces a child node from this node. Provided the arguments for which element to swap with relative to this node and which node is empty,
	#the return value is a child node with these two indexes swapped and the parent node defined as self and an increased cost
	def __makeChildNode(self, swap_index, empty_index):
		#returns a child node
		child_state = list(self.state)
		child_state[empty_index], child_state[empty_index + swap_index] = child_state[empty_index + swap_index], child_state[empty_index]
		child_node = Node(child_state, self, self.cost + 1)
		return child_node

	#print the current node on the console
	def print_node(self):
		print "===Game State==="
		for y in xrange(0,3):
			print self.state[3 * y] if self.state[3 * y] != 0 else " ",
			print self.state[3 * y + 1] if self.state[3 * y + 1] != 0 else " ",
			print self.state[3 * y + 2] if self.state[3 * y + 2] != 0 else " "
		print ""

	#Returns an expansion of nodes. Checks the path for duplicates and removes them
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

		nodes_to_delete = []
		for x in expansion:
			prev = self
			while prev is not None:
				if prev.state == x.state:
					nodes_to_delete.append(x)
					break
				prev = prev.parent

		for x in nodes_to_delete:
			expansion.remove(x)
		return expansion

	#prints the series of states which leads to the solution
	def get_path(self):
		path = []
		node = self
		while node is not None:
			path.append(node)
			node = node.parent
		return reversed(path)

start = [8,6,7,2,5,4,3,0,1]
#start = [0,1,3,4,2,5,7,8,6]
#start = [1,2,3,4,5,6,7,0,8]
goal = [1,2,3,4,5,6,7,8,0]

start_node = Node(start)
goal_node = Node(goal)


def tree_search(initial_node, goal):
	lowest = 20
	fringe = initial_node.expand()
	node_dict = {}	#dictionary to keep track of nodes
	for x in fringe:
		node_dict[tuple(x.state)] = x	

	while True:
		if len(fringe) == 0:
			return -1
		node = fringe.pop(0)
		del node_dict[tuple(node.state)]
		#node.print_node()
		if node.state == goal.state:
			return node
		expansion = node.expand()
		for x in expansion:
			x_tuple = tuple(x.state)
			if x_tuple in node_dict:
				if node_dict[x_tuple].cost > x.cost:
					node_dict[x_tuple] = x
					fringe.remove(node_dict[x_tuple])
					fringe.append(x)
			else:
				node_dict[x_tuple] = x
				fringe.append(x)

for x in start_node.expand():
	x.print_node()

goal = tree_search(Node(start), Node(goal))

if goal == -1:
	print "no solution"
else:
	print "solution found in :"
	for x in goal.get_path():
		x.print_node()


