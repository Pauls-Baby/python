import unittest
from overlap_event import Overlapping

class Testing(unittest.TestCase):
    def test_overlapping(self):                                 # is overlapping
        array = [[1,3], [2,6], [8,9], [5,7], [5,10]]                    # overlapped_array holds the overlapping pairs
        n = len(array)
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        overlapped_size = len(overlapped_array)
        result = True if overlapped_size else False
        self.assertTrue(result, True)

    def test_non_overlapping(self):                             # is not overlapping
        array = [[1,3], [4,6], [8,9]]                           # overlapped_array holds the overlapping pairs(here empty)
        n = len(array)
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        self.assertEqual(overlapped_array, [])

    def test_overlapping_in_middle(self):                       # events are present wholy in between another event(middle)
        array = [[1,3], [4,6], [0,9]]
        n = len(array)        
        _, middle, _ = Overlapping.overlap(array, n)
        self.assertEqual(middle, 2)

    def test_overlapping_edges(self):                           #edges overlap
        array = [[1,3], [2,6], [5,9]]
        n = len(array)       
        _, _, adjacent = Overlapping.overlap(array, n)
        self.assertEqual(adjacent, 2)

    def test_full_overlap(self):                                #every elements in list overlap each other
        array = [[1,3], [2,6], [0,9]]
        n = len(array)  
        count = 0
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        overlapped_size = len(overlapped_array)
        self.assertEqual(overlapped_size, n)

    def test_negative(self):                                    #list has negative elements
        array = [[2,6],[-3, -2], [-1, 3], [0, 9], [8,11]]
        n = len(array)         
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        array_length = len(overlapped_array)
        self.assertEqual(array_length, 4)

    def test_positive(self):                                    # only positive elements
        array = [[2,6], [1,3], [0,9], [13,16], [8,10]]
        n = len(array)  
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        array_length = len(overlapped_array)
        self.assertEqual(array_length, 4) 

    def test_unsorted_input(self):                              # unsorted input
        array = [[2,6], [1,3], [0,9], [8,11]]
        n = len(array)  
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        array_length = len(overlapped_array)
        self.assertEqual(array_length, 4) 

    def test_sorted_input(self):                                # sorted input
        array = [[0,9], [1,3], [2,6], [8,11]]
        n = len(array)  
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        array_length = len(overlapped_array)
        self.assertEqual(array_length, 4)

    def test_zero(self):                                        # has event start and end with zero
        array = [[0,0], [1,3], [2,6], [8,11]]
        n = len(array)  
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        array_length = len(overlapped_array)
        self.assertEqual(array_length, 1)

    def test_zero_start(self):                                  # has event start with zero
        array = [[0,5], [1,3], [2,6], [8,11]]
        n = len(array)  
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        array_length = len(overlapped_array)
        self.assertEqual(array_length, 3)

    def test_all_zero(self):                                    # full zero(single minor event)
        array = [[0,0], [0,0], [0,0], [0,0]]
        n = len(array)  
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        array_length = len(overlapped_array)
        self.assertEqual(array_length, 1)

    def test_all_same_elements(self):                           # all event at same time
        array = [[1,3], [1,3], [1,3], [1,3]]
        n = len(array)  
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        array_length = len(overlapped_array)
        self.assertEqual(array_length, 1)

    def test_empty_array(self):                                 # empty array input
        array = []
        n = 1
        overlapped_array, _, _ = Overlapping.overlap(array, n)
        self.assertEqual(overlapped_array, [])

if __name__ == '__main__':
    unittest.main()