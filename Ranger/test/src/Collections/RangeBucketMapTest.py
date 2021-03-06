import unittest
from Ranger.src.Collections.RangeBucketMap import RangeBucketMap
from Ranger.src.Range.Range import Range

debug = False


class RangeBucketMapTest(unittest.TestCase):
    """ Unit Tests for RangeBucketMap.py """

    def test_put(self):
        if debug: print("Testing put")
        buckets = RangeBucketMap()
        buckets.put(Range.closed(3, 5), 'a')
        self.assertEqual(buckets.ranges[0], Range.closed(3, 5))
        self.assertEquals(buckets.items[0], set(['a']))
        buckets.put(Range.closed(7, 10), 'b')
        self.assertEqual(len(buckets), 2)
        self.assertEqual(buckets.ranges[0], Range.closed(3, 5))
        self.assertEqual(buckets.ranges[1], Range.closed(7, 10))
        self.assertEqual(buckets.items[0], set(['a']))
        self.assertEqual(buckets.items[1], set(['b']))
        buckets.put(Range.closed(4, 8), 'c')
        self.assertEqual(len(buckets), 5)
        self.assertEqual(buckets.ranges[0], Range.closed_open(3, 4))
        self.assertEqual(buckets.ranges[1], Range.closed(4, 5))
        self.assertEqual(buckets.ranges[2], Range.open(5, 7))
        self.assertEqual(buckets.ranges[3], Range.closed(7, 8))
        self.assertEqual(buckets.ranges[4], Range.open_closed(8, 10))
        self.assertEqual(buckets.items[0], set(['a']))
        self.assertEqual(buckets.items[1], set(['a', 'c']))
        self.assertEqual(buckets.items[2], set(['c']))
        self.assertEqual(buckets.items[3], set(['b', 'c']))
        self.assertEqual(buckets.items[4], set(['b']))

    def test_get(self):
        if debug: print("Testing get")
        buckets = RangeBucketMap()
        buckets.put(Range.closed(3, 5), 'a')
        buckets.put(Range.closed(7, 10), 'b')
        buckets.put(Range.closed(4, 8), 'c')
        self.assertEqual(buckets.get(6), set(['c']))
        self.assertEqual(buckets.get(4), set(['a', 'c']))
        self.assertEquals(buckets.get(Range.closed(0, 20)), set(['a', 'b', 'c']))
        self.assertEquals(buckets.get(Range.open_closed(5, 8)), set(['b', 'c']))

    def test_get_bugfix1(self):
        if debug: print("Testing get under first bugfix")
        buckets = RangeBucketMap()
        buckets.put(Range.closed(67432367, 67434244), 'G')
        buckets.put(Range.closed(67432367, 67434244), 'T1')
        buckets.put(Range.closed(67432375, 67434015), 'T2')
        buckets_dict = dict((v, k) for k, v in buckets.iteritems())
        self.assertEqual(buckets_dict['T2'], Range.closed(67432375, 67434015))

    def test_remove(self):
        if debug: print("Testing remove")
        buckets = RangeBucketMap()
        buckets.put(Range.closed(3, 5), 'a')
        buckets.put(Range.closed(7, 10), 'b')
        buckets.put(Range.closed(4, 8), 'c')
        buckets.remove(Range.closed(3, 3))
        self.assertEqual(len(buckets), 5)
        self.assertEqual(buckets.ranges[0], Range.open(3, 4))
        self.assertEqual(buckets.ranges[1], Range.closed(4, 5))
        self.assertEqual(buckets.ranges[2], Range.open(5, 7))
        self.assertEqual(buckets.ranges[3], Range.closed(7, 8))
        self.assertEqual(buckets.ranges[4], Range.open_closed(8, 10))
        self.assertEqual(buckets.items[0], set(['a']))
        self.assertEqual(buckets.items[1], set(['a', 'c']))
        self.assertEqual(buckets.items[2], set(['c']))
        self.assertEqual(buckets.items[3], set(['b', 'c']))
        self.assertEqual(buckets.items[4], set(['b']))
        buckets.remove(Range.closed(9, 20))
        self.assertEqual(len(buckets), 5)
        self.assertEqual(buckets.ranges[0], Range.open(3, 4))
        self.assertEqual(buckets.ranges[1], Range.closed(4, 5))
        self.assertEqual(buckets.ranges[2], Range.open(5, 7))
        self.assertEqual(buckets.ranges[3], Range.closed(7, 8))
        self.assertEqual(buckets.ranges[4], Range.open(8, 9))
        self.assertEqual(buckets.items[0], set(['a']))
        self.assertEqual(buckets.items[1], set(['a', 'c']))
        self.assertEqual(buckets.items[2], set(['c']))
        self.assertEqual(buckets.items[3], set(['b', 'c']))
        self.assertEqual(buckets.items[4], set(['b']))
        buckets.remove(Range.closed(5, 7))
        self.assertEqual(len(buckets), 4)
        self.assertEqual(buckets.ranges[0], Range.open(3, 4))
        self.assertEqual(buckets.ranges[1], Range.closed_open(4, 5))
        self.assertEqual(buckets.ranges[2], Range.open_closed(7, 8))
        self.assertEqual(buckets.ranges[3], Range.open(8, 9))
        self.assertEqual(buckets.items[0], set(['a']))
        self.assertEqual(buckets.items[1], set(['a', 'c']))
        self.assertEqual(buckets.items[2], set(['b', 'c']))
        self.assertEqual(buckets.items[3], set(['b']))

    def test_iteritems(self):
        if debug: print("Testing iteritems")
        buckets = RangeBucketMap()
        buckets.put(Range.closed(3, 5), 'a')
        buckets.put(Range.closed(7, 10), 'b')
        buckets.put(Range.closed(4, 8), 'c')
        iterator = buckets.iteritems(2, 10)
        self.assertEquals(next(iterator), (Range.closed(3, 5), 'a'))
        self.assertEquals(next(iterator), (Range.closed(4, 8), 'c'))
        self.assertEquals(next(iterator), (Range.closed(7, 10), 'b'))
        with self.assertRaises(StopIteration):
            next(iterator)
        iterator = buckets.iteritems(3, 8)
        self.assertEquals(next(iterator), (Range.closed(3, 5), 'a'))
        self.assertEquals(next(iterator), (Range.closed(4, 8), 'c'))
        self.assertEquals(next(iterator), (Range.closed(7, 8), 'b'))
        with self.assertRaises(StopIteration):
            next(iterator)


if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
