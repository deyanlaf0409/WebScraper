import unittest
from Filter import Filter


class TestFilter(unittest.TestCase):
    def setUp(self):
        pass

    def test_search_by_words_in_desc(self):
        test_description = "apple,banana,orange"
        test_filter = Filter.Filter(words_in_description=test_description)


        returns_true = "apple,banana,orange"
        returns_false = "carrot,cabbage,mule"
        actual = test_filter._Filter__search_by_words_in_desc
        self.assertTrue(actual(returns_true))
        self.assertFalse(actual(returns_false))


class TestHelperFilter(unittest.TestCase):
    def test_helper_filter(self):

        test_filter_2 = Filter.Filter()

        # Test case 1: Filter should return True
        self.assertTrue(Filter.helper_filter(5, "random_attr < 7"))

        # Test case 2: Filter should return False
        self.assertFalse(Filter.helper_filter(8, "random_attr < 4"))

        # Test case 3: Filter should return True
        self.assertTrue(Filter.helper_filter(3.14, "random_attr < 3.141592"))

        # Test case 4: Filter should return False
        self.assertFalse(Filter.helper_filter(1.23, "random_attr < 1.12"))

