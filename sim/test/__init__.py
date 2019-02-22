import unittest


def get_tests():
    return full_suite()


def full_suite():
    from test import TechnicalTest

    technicaltestsuite = unittest.TestLoader().loadTestsFromTestCase(TechnicalTest)

    return unittest.TestSuite([technicaltestsuite])
