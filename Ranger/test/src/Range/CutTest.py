import unittest
from Ranger.src.Range.Cut import Cut

debug = False

class CutTest(unittest.TestCase):
    """ Unit Tests for Cut.py """
    # TODO: Write unit tests for __eq__, __lt__, __gt__, __le__, __ge__
    def test_isLessThanInt(self):
        if debug: print("Testing is_less_than with integers")
        ptCut = Cut(int, point=2, below=False)
        belowAllCut = Cut(int, below_all=True)
        aboveAllCut = Cut(int, above_all= True)
        self.assertTrue(ptCut.is_less_than(3))
        self.assertFalse(ptCut.is_less_than(2))
        self.assertFalse(ptCut.is_less_than(1))
        self.assertTrue(belowAllCut.is_less_than(-999))
        self.assertFalse(aboveAllCut.is_less_than(1000))
    def test_isGreaterThanInt(self):
        if debug: print("Testing is_greater_than with integers")
        ptCut = Cut(int, point=2, below=False)
        belowAllCut = Cut(int, below_all=True)
        aboveAllCut = Cut(int, above_all= True)
        self.assertFalse(ptCut.is_greater_than(3))
        self.assertTrue(ptCut.is_greater_than(2))
        self.assertTrue(ptCut.is_greater_than(1))
        self.assertFalse(belowAllCut.is_greater_than(-999))
        self.assertTrue(aboveAllCut.is_greater_than(1000))
    def test_belowValue(self):
        if debug: print("Testing below_value")
        theCut = Cut.below_value(2)
        self.assertFalse(theCut.below_all)
        self.assertFalse(theCut.above_all)
        self.assertEqual(theCut.point, 2)
        self.assertTrue(theCut.below)
    def test_belowAll(self):
        if debug: print("Testing below_all")
        theCut = Cut.below_all(int)
        self.assertTrue(theCut.below_all)
        self.assertFalse(theCut.above_all)
        self.assertIsNone(theCut.point)
    def test_aboveValue(self):
        if debug: print("Testing above_value")
        theCut = Cut.above_value(2)
        self.assertFalse(theCut.below_all)
        self.assertFalse(theCut.above_all)
        self.assertEqual(theCut.point, 2)
        self.assertFalse(theCut.below)
    def test_aboveAll(self):
        if debug: print("Testing above_all")
        theCut = Cut.above_all(int)
        self.assertFalse(theCut.below_all)
        self.assertTrue(theCut.above_all)
        self.assertIsNone(theCut.point)        
if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
