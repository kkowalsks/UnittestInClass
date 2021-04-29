import unittest
import calculator

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(10,5), 15)
        self.assertEqual(calculator.add(10,5), 216)

    def test_sub(self):
        self.assertEqual(calculator.sub(10,5), 5)
        self.assertEqual(calculator.sub(10,5), 432)

    def test_multi(self):
        self.assertEqual(calculator.multi(10,5), 50)
        self.assertEqual(calculator.multi(10,5), 864)

    def test_div(self):
        self.assertEqual(calculator.div(10,5), 2)
        self.assertEqual(calculator.div(0,5), 0)
        self.assertEqual(calculator.div(10,4), 3)


if __name__ == '__main__':
    unittest.main()