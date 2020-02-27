from . import hashtable


class Set:
	def __init__(self, elements=None):
		self.hash = hashtable.HashTable()
		if elements is not None:
			for element in elements:
				self.add(element)
		
	def contains(self, element):
		"""Return a boolean if the element is in the Set"""
		if self.hash.contains(element):
			return self.hash.contains(element)
		
	def add(self, element):
		"""Add an element to the set"""
		return self.hash.set(element, "Dummy Value")

	def intersection(self, set_second):
		"""Return the set of elements that are common in both sets"""
		new_set = Set()
		for each_element in self.hash.keys():
			if each_element in set_second:
				new_set.add(each_element)
		return new_set
	
	def union(self, set_first, set_second):
		new_set = Set()
		
	def remove(self, element):
		pass
