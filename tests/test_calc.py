import os
import random
import random

import pytest

from src.calc import add, divide, is_even


class TestCalc:
    def test_add(self):
        assert add(2, 3) == 5

    def test_divide(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(1, 0)

    def test_is_even(self):
        assert is_even(4)
        assert not is_even(5)


class TestFlakyCalc:
    def test_flaky_adds_under_load(self):
        if random.random() < 0.4:
            raise AssertionError("flaky: simulated timeout while adding")
        assert add(1, 1) == 2

    def test_flaky_divides_under_contention(self):
        if random.random() < 0.4:
            raise AssertionError("flaky: simulated stale divisor cache")
        assert divide(9, 3) == 3

    def test_flaky_fails_on_first_attempt_only(self):
        if os.environ.get("GITHUB_RUN_ATTEMPT") == "1":
            raise AssertionError("flaky: simulated first-attempt failure (GITHUB_RUN_ATTEMPT=1)")
        assert add(1, 1) == 2

    def test_flaky_parity_under_race(self):
        if random.random() < 0.4:
            raise AssertionError("flaky: simulated race in parity check")
        assert is_even(8)
