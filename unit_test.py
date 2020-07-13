import unittest


class Testing(unittest.TestCase):
    def test_overlapping(self):
        a = 'some'
        b = 'some'
        self.assertTrue(a, b)

    def test_non_overlapping(self):
        a = True
        b = True
        self.assertTrue(a, b)

    def test_equal(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_notequal(self):
        a = True
        b = False
        self.assertNotEqual(a, b)

    def test_negative(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_positive(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_unsorted(self):
        a = True
        b = True
        self.assertEqual(a, b)  

    def test_sorted(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_zero(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_nonzero(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_empty_element(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_non_empty_elements(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()