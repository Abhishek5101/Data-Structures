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
		set_to_use.add(7)
		set_to_use.add(8)
		with self.assertRaises(KeyError):
			set_to_use.add(3)
		assert set_to_use.contains(6) is True
		assert set_to_use.contains(7) is True
		assert set_to_use.contains(8) is True
		
	def test_remove(self):
		elements = [1, 2, 3, 4, 5]
		set_to_use = Set(elements)
		set_to_use.remove(1)
		set_to_use.remove(2)
		set_to_use.remove(3)
		set_to_use.remove(4)
		with self.assertRaises(KeyError):
			set_to_use.remove(79)
		assert set_to_use.contains(1) is False
		assert set_to_use.contains(2) is False
		assert set_to_use.contains(3) is False
		assert set_to_use.contains(4) is False
		
	def test_union(self):
		elements1 = [1, 2, 3, 4, 5]
		other_elements1 = [4, 5, 6, 7]
		set_to_use1 = Set(elements1)
		other_set_to_use1 = Set(other_elements1)
		self.assertEqual(set_to_use1.union(other_set_to_use1).hash.values(), [1, 2, 3, 4, 5, 6, 7])
		
		elements2 = [7, 8, 9, 10, 11]
		other_elements2 = [12, 13]
		set_to_use2 = Set(elements2)
		other_set_to_use2 = Set(other_elements2)
		self.assertEqual(set_to_use2.union(other_set_to_use2).hash.values(), [7, 8, 9, 10, 11, 12, 13])

		elements3 = [75, 76]
		other_elements3 = [12, 13]
		set_to_use3 = Set(elements3)
		other_set_to_use3 = Set(other_elements3)
		self.assertEqual(set_to_use3.union(other_set_to_use3).hash.values(), [75, 76, 12, 13])

	def test_intersection(self):
		elements = [1, 2, 3, 4, 5]
		other_elements = [4, 5, 6, 7]
		set_to_use = Set(elements)
		other_set_to_use = Set(other_elements)
		self.assertEqual(set_to_use.intersection(other_set_to_use).hash.values(), [4, 5])
		
		elements2 = [9, 0]
		other_elements2 = [0]
		set_to_use2 = Set(elements2)
		other_set_to_use2 = Set(other_elements2)
		self.assertEqual(set_to_use2.intersection(other_set_to_use2).hash.values(), [0])

		elements3 = [66, 666, 6666]
		other_elements3 = [66, 6666]
		set_to_use3 = Set(elements3)
		other_set_to_use3 = Set(other_elements3)
		self.assertEqual(set_to_use3.intersection(other_set_to_use3).hash.values(), [66, 6666])

	def test_difference(self):
		elements = [1, 2, 3, 4, 5]
		other_elements = [4, 5, 6, 7]
		set_to_use = Set(elements)
		other_set_to_use = Set(other_elements)
		self.assertEqual(set_to_use.difference(other_set_to_use).hash.values(), [1, 2, 3])

		elements2 = [1, 2, 3, 4, 5]
		other_elements2 = [4, 5, 6, 7]
		set_to_use2 = Set(elements2)
		other_set_to_use2 = Set(other_elements2)
		self.assertEqual(other_set_to_use2.difference(set_to_use2).hash.values(), [6, 7])
		
		elements3 = [1, 2, 3, 4, 5, 8, 9]
		other_elements3 = [4, 5, 6, 7]
		set_to_use3 = Set(elements3)
		other_set_to_use3 = Set(other_elements3)
		self.assertEqual(set_to_use3.difference(other_set_to_use3).hash.values(), [1, 2, 3, 8, 9])

	def test_is_subset(self):
		elements = [1, 2, 3, 4, 5]
		other_elements = [1, 2]
		set_to_use = Set(elements)
		other_set_to_use = Set(other_elements)
		assert other_set_to_use.is_subset(set_to_use) is True
		
		elements = [6, 7, 8, 9]
		other_elements = [6, 7]
		set_to_use = Set(elements)
		other_set_to_use = Set(other_elements)
		assert other_set_to_use.is_subset(set_to_use) is True
		
		elements = [1, 2, 3, 4, 5]
		other_elements = [6, 7]
		set_to_use = Set(elements)
		other_set_to_use = Set(other_elements)
		assert other_set_to_use.is_subset(set_to_use) is False



	
	

		





