//JavaScript implementation of a Trie
define(['jquery'], function($) {

	//Trie node class used by the Trie data structure
	function TrieNode() {
		var self = this;

		self.values = [];
		self.table = {};
	}

	//Trie class
	function Trie() {
		var self = this;

		self._rootNode = new TrieNode();

		//create a branch
		self._createBranch = function(key, node) {
			if (key == "") {
				return node;
			}
			var nextNode = node.table[key.charAt(0)];
			if (nextNode == null) {
				nextNode = new TrieNode();
				node.table[key.charAt(0)] = nextNode;
			}
			return self._createBranch(key.substring(1), nextNode);
		};

		self._getNode = function(key, startNode) {
			if (key == "") {
				return startNode;
			}
			var nextNode = startNode.table[key.charAt(0)];
			if (nextNode == null) {
				return null;
			}
			return self._getNode(key.substring(1), nextNode);
		};

		//traverse this node and return all descendant values of this node
		//values will be unique (this returns a Set)
		self._traverseNodes = function(node) {
			var values = node.values.slice(0);
			var valuesObj = {};
			//use this for later to avoid adding duplicate values
			for (var value in values) {
				valuesObj[value] = true;
			}
			var keys = node.table.keys();
			for (var key in keys) {
				var childItemList = self._traverseNodes(node.table[key]);
				for (var child in childItemList) {
					//only add unique items
					if (valuesObj[child] == null) {
						valuesObj[child] = true;
						values.push(child);
					} 
				}
			}
			return values;
		};
		
		self._cleanBranch = function(key, node) {
			if(node == null || key == "") {
				return;
			}
			self._cleanBranch(key.substring(1), node.table[key.charAt(0)]);
			var childKeys = node.table.keys();
			var childless = false;
			for(var key in childKeys) {
				if(!$.isEmptyObject(node.table[key]) || !(node.values.length == 0)) {
					childless = true;
				}
			}
			if (childless == true) {
				node.table = {};
			}
		};

		self.put = function(key, value) {
			var targetNode = createBranch(key, self._rootNode);
			targetNode.values.push(value);
		};

		self.get = function(key) {
			var node = self._getNode(key, self._rootNode);
			if (node == null) {
				return [];
			}
			return node.values;
		};

		self.getAllWithPrefix = function(prefix) {
			var prefixNode = self._getNode(prefix, self._rootNode);
			if (prefixNode == null) {
				return [];
			}
			//following result should not have duplicates
			return self._traverseNodes(prefixNode);
		};
		
		self.remove = function(key) {
			if(key == "") {
				return [];
			} 
			var targetNodeParent = getNode(key.substring(0, key.length - 1), self._rootNode);
			var keyVal = key.charAt(key.length - 1);
			var targetNode = targetNodeParent.table[keyVal];
			delete targetNodeParent.table[keyVal];
			var targetValues = targetNode.values;
			self._cleanBranch(key, self._rootNode);
			return targetValues;
		};
		
		self.removeAll = function() {
			self._rootNode = new TrieNode();
		};
	}
});
