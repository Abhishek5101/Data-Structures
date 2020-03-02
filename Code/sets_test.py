from sets import Set
import unittest


class SetTests(unittest.TestCase):
	def test_init_and_size(self):
		elements = [1, 2, 3, 4, 5]
		set_to_use = Set(elements)
		assert set_to_use.size is 5
		
	def test_contains(self):
		elements = [1, 2, 3, 4, 5]
		set_to_use = Set(elements)
		assert set_to_use.contains(1) is True
		assert set_to_use.contains(2) is True
		assert set_to_use.contains(3) is True
		assert set_to_use.contains(4) is True
		assert set_to_use.contains(5) is True
		assert set_to_use.contains(109) is False
	
	def test_add(self):
		elements = [1, 2, 3, 4, 5]
		set_to_use = Set(elements)
		set_to_use.add(6)
		with self.assertRaises(KeyError):
			set_to_use.add(3)
		assert set_to_use.contains(6) is True
		
	def test_remove(self):
		elements = [1, 2, 3, 4, 5]
		set_to_use = Set(elements)
		set_to_use.remove(1)
		with self.assertRaises(KeyError):
			set_to_use.remove(79)
		assert set_to_use.contains(1) is False
		
	def test_union(self):
		elements = [1, 2, 3, 4, 5]
		other_elements = [4, 5, 6, 7]
		set_to_use = Set(elements)
		other_set_to_use = Set(other_elements)
		self.assertEqual(set_to_use.union(other_set_to_use).hash.values(), [1, 2, 3, 4, 5, 6, 7])
		
	def test_intersection(self):
		elements = [1, 2, 3, 4, 5]
		other_elements = [4, 5, 6, 7]
		set_to_use = Set(elements)
		other_set_to_use = Set(other_elements)
		self.assertEqual(set_to_use.intersection(other_set_to_use).hash.values(), [4, 5])
	
	def test_difference(self):
		elements = [1, 2, 3, 4, 5]
		other_elements = [4, 5, 6, 7]
		set_to_use = Set(elements)
		other_set_to_use = Set(other_elements)
		self.assertEqual(set_to_use.difference(other_set_to_use).hash.values(), [1, 2, 3])
	
	def test_is_subset(self):
		elements = [1, 2, 3, 4, 5]
		other_elements = [1, 2]
		set_to_use = Set(elements)
		other_set_to_use = Set(other_elements)
		assert other_set_to_use.is_subset(set_to_use) is True


	
	

		





