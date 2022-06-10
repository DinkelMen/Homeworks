from FizzBuzz import fizzbuzz
import unittest


class TestFizzBuzz(unittest.TestCase):

    def test_input1(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_input2(self):
        self.assertEqual(fizzbuzz(0), 'FizzBuzz')

    def test_input3(self):
        self.assertEqual(fizzbuzz(-0), 'FizzBuzz')

    def test_input4(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')

    def test_input5(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')

    def test_input6(self):
        self.assertEqual(fizzbuzz(1028), 1028)

    def test_input7(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')

    def test_input8(self):
        self.assertEqual(fizzbuzz(9.0), 'Fizz')

    def test_input9(self):
        self.assertEqual(fizzbuzz(-15.0), 'FizzBuzz')

    def test_input10(self):
        self.assertEqual(fizzbuzz(100000000000000000000000000), 'Buzz')

    def test_input11(self):
        self.assertEqual(fizzbuzz(30 + 21), 'Fizz')


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_negative_input1(self):
        self.assertEqual(fizzbuzz([3]), 'Fizz')

    @unittest.expectedFailure
    def test_negative_input2(self):
        self.assertEqual(fizzbuzz('24'), 'Fizz')

    @unittest.expectedFailure
    def test_negative_input3(self):
        self.assertEqual(fizzbuzz([';']), 'Exception')

    @unittest.expectedFailure
    def test_negative_input4(self):
        self.assertEqual(fizzbuzz(), 'Exception')

    @unittest.expectedFailure
    def test_negative_input5(self):
        self.assertEqual(fizzbuzz({30: 30}), 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
