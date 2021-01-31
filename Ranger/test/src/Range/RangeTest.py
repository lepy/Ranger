import unittest
from Ranger.src.Range.Range import Range

debug = False

class RangeTest(unittest.TestCase):
    """ Unit Tests for Range.py """
    def test_closed(self):
        if debug: print("Testing closed")
        # Floats
        floatRange = Range.closed(2.,5.)
        self.assertFalse(floatRange.contains(1.99))
        self.assertTrue(floatRange.contains(2.))
        self.assertTrue(floatRange.contains(3.))
        self.assertTrue(floatRange.contains(5.))
        self.assertFalse(floatRange.contains(5.01))
        # Integers
        intRange = Range.closed(2,5)
        self.assertTrue(intRange.contains(2))
        self.assertFalse(intRange.contains(1))
        # Letters
        letterRange = Range.closed('b','e')
        self.assertFalse(letterRange.contains('a'))
        self.assertTrue(letterRange.contains('b'))
        self.assertTrue(letterRange.contains('c'))
        self.assertTrue(letterRange.contains('e'))
        self.assertFalse(letterRange.contains('f'))
    def test_closedOpen(self):
        if debug: print("Testing closed_open")
        # Floats
        floatRange = Range.closed_open(2., 5.)
        self.assertFalse(floatRange.contains(1.99))
        self.assertTrue(floatRange.contains(2.))
        self.assertTrue(floatRange.contains(3.))
        self.assertFalse(floatRange.contains(5.))
        self.assertFalse(floatRange.contains(5.01))
        # Letters
        letterRange = Range.closed_open('b', 'e')
        self.assertFalse(letterRange.contains('a'))
        self.assertTrue(letterRange.contains('b'))
        self.assertTrue(letterRange.contains('c'))
        self.assertFalse(letterRange.contains('e'))
        self.assertFalse(letterRange.contains('f'))
    def test_openClosed(self):
        if debug: print("Testing open_closed")
        # Floats
        floatRange = Range.open_closed(2., 5.)
        self.assertFalse(floatRange.contains(1.99))
        self.assertFalse(floatRange.contains(2.))
        self.assertTrue(floatRange.contains(3.))
        self.assertTrue(floatRange.contains(5.))
        self.assertFalse(floatRange.contains(5.01))
        # Letters
        letterRange = Range.open_closed('b', 'e')
        self.assertFalse(letterRange.contains('a'))
        self.assertFalse(letterRange.contains('b'))
        self.assertTrue(letterRange.contains('c'))
        self.assertTrue(letterRange.contains('e'))
        self.assertFalse(letterRange.contains('f'))
    def test_open(self):
        if debug: print("Testing open")
        # Floats
        floatRange = Range.open(2.,5.)
        self.assertFalse(floatRange.contains(1.99))
        self.assertFalse(floatRange.contains(2.))
        self.assertTrue(floatRange.contains(3.))
        self.assertFalse(floatRange.contains(5.))
        self.assertFalse(floatRange.contains(5.01))
        with self.assertRaises(TypeError):
            Range.open(3.,3.)
        # Letters
        letterRange = Range.open('b','e')
        self.assertFalse(letterRange.contains('a'))
        self.assertFalse(letterRange.contains('b'))
        self.assertTrue(letterRange.contains('c'))
        self.assertFalse(letterRange.contains('e'))
        self.assertFalse(letterRange.contains('f'))
        with self.assertRaises(TypeError):
            Range.open('b','b')
    def test_lessThan(self):
        if debug: print("Testing less_than")
        # Floats
        floatRange = Range.less_than(5.)
        self.assertTrue(floatRange.contains(1.99))
        self.assertTrue(floatRange.contains(2.))
        self.assertTrue(floatRange.contains(3.))
        self.assertFalse(floatRange.contains(5.))
        self.assertFalse(floatRange.contains(5.01))
        # Letters
        letterRange = Range.less_than('e')
        self.assertTrue(letterRange.contains('a'))
        self.assertTrue(letterRange.contains('b'))
        self.assertTrue(letterRange.contains('c'))
        self.assertFalse(letterRange.contains('e'))
        self.assertFalse(letterRange.contains('f'))
    def test_atMost(self):
        if debug: print("Testing at_most")
        # Floats
        floatRange = Range.at_most(5.)
        self.assertTrue(floatRange.contains(1.99))
        self.assertTrue(floatRange.contains(2.))
        self.assertTrue(floatRange.contains(3.))
        self.assertTrue(floatRange.contains(5.))
        self.assertFalse(floatRange.contains(5.01))
        # Letters
        letterRange = Range.at_most('e')
        self.assertTrue(letterRange.contains('a'))
        self.assertTrue(letterRange.contains('b'))
        self.assertTrue(letterRange.contains('c'))
        self.assertTrue(letterRange.contains('e'))
        self.assertFalse(letterRange.contains('f'))
    def test_greaterThan(self):
        if debug: print("Testing greater_than")
        # Floats
        floatRange = Range.greater_than(5.)
        self.assertFalse(floatRange.contains(1.99))
        self.assertFalse(floatRange.contains(2.))
        self.assertFalse(floatRange.contains(3.))
        self.assertFalse(floatRange.contains(5.))
        self.assertTrue(floatRange.contains(5.01))
        # Letters
        letterRange = Range.greater_than('e')
        self.assertFalse(letterRange.contains('a'))
        self.assertFalse(letterRange.contains('b'))
        self.assertFalse(letterRange.contains('c'))
        self.assertFalse(letterRange.contains('e'))
        self.assertTrue(letterRange.contains('f'))
    def test_atLeast(self):
        if debug: print("Testing at_least")
        # Floats
        floatRange = Range.at_least(5.)
        self.assertFalse(floatRange.contains(1.99))
        self.assertFalse(floatRange.contains(2.))
        self.assertFalse(floatRange.contains(3.))
        self.assertTrue(floatRange.contains(5.))
        self.assertTrue(floatRange.contains(5.01))
        # Letters
        letterRange = Range.at_least('e')
        self.assertFalse(letterRange.contains('a'))
        self.assertFalse(letterRange.contains('b'))
        self.assertFalse(letterRange.contains('c'))
        self.assertTrue(letterRange.contains('e'))
        self.assertTrue(letterRange.contains('f'))
    def test_hasLowerBound(self):
        if debug: print("Testing has_lower_bound")
        self.assertTrue(Range.at_least(5.).has_lower_bound())
        self.assertFalse(Range.at_most(5.).has_lower_bound())
        self.assertTrue(Range.closed(2.,5.).has_lower_bound())
    def test_hasUpperBound(self):
        if debug: print("Testing has_upper_bound")
        self.assertFalse(Range.at_least(5.).has_upper_bound())
        self.assertTrue(Range.at_most(5.).has_upper_bound())
        self.assertTrue(Range.closed(2.,5.).has_upper_bound())
    def test_lowerEndpoint(self):
        if debug: print("Testing lower_endpoint")
        with self.assertRaises(TypeError):
            Range.at_most(5.).lower_endpoint()
        self.assertEqual(Range.at_least(5.).lower_endpoint(), 5.)
        self.assertEqual(Range.closed(5.,10.).lower_endpoint(), 5.)
    def test_upperEndpoint(self):
        if debug: print("Testing upper_endpoint")
        with self.assertRaises(TypeError):
            Range.at_least(5.).upper_endpoint()
        self.assertEqual(Range.at_most(5.).upper_endpoint(), 5.)
        self.assertEqual(Range.closed(5.,10.).upper_endpoint(), 10.)
    def test_isLowerBoundClosed(self):
        if debug: print("Testing is_lower_bound_closed")
        with self.assertRaises(TypeError):
            Range.at_most(5.).is_lower_bound_closed()
        self.assertTrue(Range.closed_open(5., 10.).is_lower_bound_closed())
        self.assertFalse(Range.open_closed(5., 10.).is_lower_bound_closed())
    def test_isUpperBoundClosed(self):
        if debug: print("Testing is_upper_bound_closed")
        with self.assertRaises(TypeError):
            Range.at_least(5.).is_upper_bound_closed()
        self.assertFalse(Range.closed_open(5., 10.).is_upper_bound_closed())
        self.assertTrue(Range.open_closed(5., 10.).is_upper_bound_closed())
    def test_isEmpty(self):
        if debug: print("Testing is_empty")
        self.assertTrue(Range.closed_open(3., 3.).is_empty())
        self.assertTrue(Range.open_closed(3., 3.).is_empty())
        self.assertFalse(Range.open_closed(3., 3.001).is_empty())
    def test_containsAll(self):
        if debug: print("Testing contains_all")
        self.assertTrue(Range.open_closed(3., 5.).contains_all([4., 4.5, 5.]))
        self.assertFalse(Range.closed_open(3., 5.).contains_all([4., 4.5, 5.]))
        self.assertFalse(Range.closed_open(3., 5.).contains_all([3., 4., 5.]))
        self.assertFalse(Range.closed_open(3., 5.).contains_all([2., 4., 5.]))
    def test_encloses(self):
        if debug: print("Testing encloses")
        range1 = Range.closed(3.,6.)
        range2 = Range.closed(4.,5.)
        self.assertTrue(range1.encloses(range2))
        range1 = Range.open(3.,6.)
        range2 = Range.open(3.,6.)
        self.assertTrue(range1.encloses(range2))
        range2 = Range.closed(4.,4.)
        self.assertTrue(range1.encloses(range2))
        range1 = Range.open_closed(3., 6.)
        range2 = Range.closed(3.,6.)
        self.assertFalse(range1.encloses(range2))
        self.assertTrue(range2.encloses(range1))
        range1 = Range.closed(4.,5.)
        range2 = Range.open(3.,6.)
        self.assertFalse(range1.encloses(range2))
        self.assertTrue(range2.encloses(range1))
    def test_isConnected(self):
        if debug: print("Testing is_connected")
        range1 = Range.closed(2.,4.)
        range2 = Range.closed(5.,7.)
        self.assertFalse(range1.is_connected(range2))
        range2 = Range.closed(3.,5.)
        self.assertTrue(range1.is_connected(range2))
        range2 = Range.closed(4.,6.)
        self.assertTrue(range1.is_connected(range2))
    def test_intersection(self):
        if debug: print("Testing intersection")
        range1 = Range.closed(1.,5.)
        range2 = Range.closed(3.,7.)
        self.assertEqual(range1.intersection(range2),
                         Range.closed(3.,5.))
        range2 = Range.closed(5.,7.)
        self.assertEqual(range1.intersection(range2),
                         Range.closed(5.,5.))
        range2 = Range.closed(6.,7.)
        with self.assertRaises(ValueError):
            range1.intersection(range2)
    def test_span(self):
        if debug: print("Testing span")
        range1 = Range.closed(1.,3.)
        range2 = Range.closed(5.,7.)
        self.assertEqual(range1.span(range2),
                         Range.closed(1.,7.))
        range2 = Range.closed(2.,5.)
        self.assertEqual(range1.span(range2),
                         Range.closed(1.,5.))
    def test_getDistanceFromPoint(self):
        if debug: print("Testing get_distance_from_point")
        range1 = Range.closed(1.,3.)
        self.assertAlmostEqual(range1.get_distance_from_point(1.), 0.)
        self.assertAlmostEqual(range1.get_distance_from_point(2.), 0.)
        self.assertAlmostEqual(range1.get_distance_from_point(3.), 0.)
        self.assertAlmostEqual(range1.get_distance_from_point(100.), 97.)
        self.assertAlmostEqual(range1.get_distance_from_point(0.99), 0.01)
        range1 = Range.open_closed(1., 3.)
        with self.assertRaises(TypeError):
            range1.get_distance_from_point(0.99)
    def test_getDistanceFromRange(self):
        if debug: print("Testing get_distance_from_range")
        range1 = Range.closed(1.,3.)
        self.assertAlmostEqual(range1.get_distance_from_range(Range.closed(5., 7.)), 2.)
        self.assertAlmostEqual(range1.get_distance_from_range(Range.closed(-1., 0.)), 1.)
        self.assertAlmostEqual(range1.get_distance_from_range(Range.closed(-5., 10.)), 0.)
        self.assertAlmostEqual(range1.get_distance_from_range(Range.closed(-5., 2.)), 0.)
        self.assertAlmostEqual(range1.get_distance_from_range(Range.closed(2., 10.)), 0.)
        self.assertAlmostEqual(range1.get_distance_from_range(Range.closed(1.5, 2.1)), 0.)
        with self.assertRaises(TypeError):
            range1.get_distance_from_range(Range.closed_open(1.5, 2.1))
if __name__ == "__main__":
    debug = True
    unittest.main(exit = False)
