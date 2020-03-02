from hashtable import HashTable


class Set:
	def __init__(self, elements=None):
		self.hash = HashTable()
		self.size = 0
		if elements is not None:
			for element in elements:
				self.add(element)
		
	def size(self):
		return self.size
	
	def contains(self, element):
		"""Return a boolean if the element is in the Set"""
		return self.hash.contains(element)
		
	def add(self, element):
		"""Add an element to the set"""
		self.size += 1
		if not self.hash.contains(element):
			return self.hash.set(element, element)
		raise KeyError("Can not add again")

	def intersection(self, other_set):
		"""Return the set of elements that are common in both sets"""
		new_set = Set()
		for each_element in self.hash.values():
			if other_set.contains(each_element):
				new_set.add(each_element)
		return new_set
	
	def union(self, other_set):
		new_set = Set()
		for element in self.hash.values():
			new_set.add(element)
		for element in other_set.hash.values():
			if not new_set.contains(element):
				new_set.add(element)
		return new_set
	
	def remove(self, element):
		if not self.hash.contains(element):
			raise KeyError("Can not delete element that doesn't exist")
		self.hash.delete(element)
		self.size -= 1
	
	def difference(self, other_set):
		"""Return a new set that is the difference of this set and other_set."""
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
		return bool([element for element in other_set.hash.values() if self.contains(element)])


def test_set():
	elements = ['A', 'B', 'D', 'F']
	other_elements = ['A', 'B', 'D', 'F', 'G', 'H']
	set = Set(elements)
	other_set = Set(other_elements)
	print(other_set.is_subset(set))


if __name__ == '__main__':
	test_set()
