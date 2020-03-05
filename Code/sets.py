from hashtable import HashTable


class Set:
	def __init__(self, elements=None):
		self.hash = HashTable()
		self.size = 0
		if elements is not None:
			for element in elements:
				self.add(element)
		
	def size(self):
		"""
		Time Complexity --> O(1)
		"""
		return self.size
	
	def contains(self, element):
		"""Return a boolean if the element is in the Set"""
		"""
		Time Complexity --> O(1)
		"""
		return self.hash.contains(element)
		
	def add(self, element):
		"""Add an element to the set"""
		"""
		Time Complexity --> O(1) Except when resize is called. Then O(n)
		"""
		self.size += 1
		if not self.hash.contains(element):
			return self.hash.set(element, element)
		raise KeyError("Can not add again")

	def intersection(self, other_set):
		"""Return the set of elements that are common in both sets"""
		"""
		Time Complexity --> O(n)
		"""
		new_set = Set()
		for each_element in self.hash.values():
			if other_set.contains(each_element):
				new_set.add(each_element)
		return new_set
	
	def union(self, other_set):
		"""
		Time Complexity --> O(n+m) since we traverse both sets
		"""
		new_set = Set()
		for element in self.hash.values():
			new_set.add(element)
		for element in other_set.hash.values():
			if not new_set.contains(element):
				new_set.add(element)
		return new_set
	
	def remove(self, element):
		"""
		Time Complexity --> O(1). & O(n) if we need to resize
		"""
		if not self.hash.contains(element):
			raise KeyError("Can not delete element that doesn't exist")
		self.hash.delete(element)
		self.size -= 1
	
	def difference(self, other_set):
		"""Return a new set that is the difference of this set and other_set."""
		"""
		Time Complexity --> O(n+m)  Traversing the self set & the other set to find common
		"""
		new_set = Set()
		for element in self.hash.values():
			new_set.add(element)
		# Removes intersected elements
		for element in other_set.hash.values():
			if new_set.contains(element):
				new_set.remove(element)
		
		return new_set
	
	def is_subset(self, other_set):
		"""Return a boolean indicating whether other_set is a subset of this set."""
		"""
		Time Complexity --> O(n) traverse the whole set to see if it contains all the elements
		"""

		return bool([element for element in other_set.hash.values() if self.contains(element)])


def test_set():
	elements = ['A', 'B', 'D', 'F']
	other_elements = ['A', 'B', 'D', 'F', 'G', 'H']
	set = Set(elements)
	other_set = Set(other_elements)
	print(other_set.is_subset(set))


if __name__ == '__main__':
	test_set()
