from FizzBuzz import fizzbuzz
import pytest


class Test_FizzBuzz():
    @pytest.fixture()
    def its_a_fixture(self):
        print('I AM FIXTURE!!!')
        a = 15 * 3
        return a

    @pytest.fixture()
    def its_not_a_fixture(self):
        print('I AM NOT FIXTURE!!!')
        b = 15 / 3
        return b

    def test_input0(self, its_a_fixture):
        assert True

    @pytest.mark.smoke
    def test_input1(self, its_a_fixture):
        assert fizzbuzz(1) == 1

    @pytest.mark.smoke
    def test_input2(self, its_a_fixture):
        assert fizzbuzz(0) == 'FizzBuzz'

    @pytest.mark.parametrize('number', [-1, -2, -7])
    def test_input3(self, its_a_fixture, number):
        assert fizzbuzz(number) == number

    def test_input4(self, its_a_fixture):
        assert fizzbuzz(3) == 'Fizz'

    def test_input5(self, its_a_fixture):
        assert fizzbuzz(5) == 'Buzz'

    def test_input6(self, its_a_fixture):
        assert fizzbuzz(1028) == 1028

    def test_input7(self, its_a_fixture):
        assert fizzbuzz(15) == 'FizzBuzz'

    def test_input8(self, its_a_fixture):
        assert fizzbuzz(9.0) == 'Fizz'

    @pytest.mark.smoke
    def test_input9(self, its_a_fixture):
        assert fizzbuzz(-15.0) == 'FizzBuzz'

    def test_input10(self, its_a_fixture):
        assert fizzbuzz(100000000000000000000000000) == 'Buzz'

    def test_input11(self, its_a_fixture):
        assert fizzbuzz(30 + 21) == 'Fizz'

# Negative tests

    @pytest.mark.xfail
    def test_negative_input1(self, its_not_a_fixture):
        assert fizzbuzz([3]) == 'Fizz'

    @pytest.mark.xfail
    def test_negative_input2(self, its_not_a_fixture):
        assert fizzbuzz('24') == 'Fizz'

    @pytest.mark.xfail
    def test_negative_input3(self, its_not_a_fixture):
        assert fizzbuzz([';']) == 'Exception'

    @pytest.mark.xfail
    def test_negative_input4(self, its_not_a_fixture):
        assert fizzbuzz('') == 'Exception'

    @pytest.mark.xfail
    def test_negative_input5(self, its_not_a_fixture):
        assert fizzbuzz({30: 30}) == 'FizzBuzz'
