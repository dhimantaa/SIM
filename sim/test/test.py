from unittest import TestCase

import sim


class TestSim(TestCase):
    def test_is_string(self):
        s = sim.Macd()
        self.assertTrue(isinstance(s,sim))