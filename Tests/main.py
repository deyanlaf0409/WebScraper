import unittest
from linkbuilder_test import TestGetCategory, TestGetBook
from scraper_test import TestBookScrapper, TestFillBook
from sorter_test import TestSortBooks
from filter_test import TestFilter, TestHelperFilter

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGetCategory))
    suite.addTest(unittest.makeSuite(TestGetBook))
    suite.addTest(unittest.makeSuite(TestBookScrapper))
    suite.addTest(unittest.makeSuite(TestFillBook))
    suite.addTest(unittest.makeSuite(TestSortBooks))
    suite.addTest(unittest.makeSuite(TestFilter))
    suite.addTest(unittest.makeSuite(TestHelperFilter))
    unittest.TextTestRunner().run(suite)
