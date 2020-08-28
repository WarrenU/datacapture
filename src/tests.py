import unittest

from src.datacapture import DataCapture


class TestDataCapture(unittest.TestCase):
    def setUp(self):
        self.capture = DataCapture()
        self.capture.add(3)
        self.capture.add(9)
        self.capture.add(3)
        self.capture.add(4)
        self.capture.add(6)
        self.stats = self.capture.build_stats()  # [3, 9, 3, 4, 6]

        self.capture.reset()
        for i in range(1, 1001):
            self.capture.add(i)

        # self.stats_xl contains numbers 1 to 1000 [1,2,3,4...1000]
        self.stats_xl = self.capture.build_stats()

    def test_add(self):
        self.assertEqual(len(self.capture.data), 1000)
        self.assertEqual(self.capture.max_int, 1000)

    def test_less(self):
        """
        Should return 2 for the two values
        that are less than 4 (3 and 3)
        """
        self.assertEqual(self.stats.less(4), 2)

    def test_greater(self):
        """
        Should return 2 (6 and 9 are greater than 4)
        """
        self.assertEqual(self.stats.greater(4), 2)

    def test_between(self):
        """
        Should return 4 (3, 3, 4 and 6 are between 3 and 6)
        """
        self.assertEqual(self.stats.between(3, 6), 4)

    def test_xl_less(self):
        self.assertEqual(self.stats_xl.less(50), 49)

    def test_xl_greater(self):
        self.assertEqual(self.stats_xl.greater(50), 950)

    def test_xl_between(self):
        self.assertEqual(self.stats_xl.between(70, 421), 352)

    def test_adding_four_sixes(self):
        """
        Adding four 6's to a data set from 1 to 1000
        [1,2,3,4,5,6,6,6,6,6,7...1000] In total there are
        5 sixes because there was 1 already present within the set.
        """
        self.capture.add(6)
        self.capture.add(6)
        self.capture.add(6)
        self.capture.add(6)
        stats = self.capture.build_stats()

        # [....6,6,6,6,6,7]
        self.assertEqual(stats.between(6, 7), 6)

        # 1004 elements total
        self.assertEqual(len(self.capture.data), 1004)

        # 1004 Elements - elements: [1,2,3,4,5] 1004-5 = 999
        self.assertEqual(stats.greater(5), 999)


if __name__ == "__main__":
    unittest.main()
