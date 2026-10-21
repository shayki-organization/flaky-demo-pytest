# flaky-demo-pytest

Demo repository for exercising a flaky-test detector against GitHub Actions logs (pytest).

- `tests/test_calc.py` contains stable tests plus three intentionally flaky tests
  (`test_flaky_*`) that fail with ~40% probability per run.
- `.github/workflows/tests.yml` (`Tests` → `unit-tests`) runs `pytest tests -rf` on
  every push so the standard `FAILED tests/test_x.py::Class::test - AssertionError`
  summary lines appear in the log.
- `.github/workflows/broken.yml` (`Broken suite` → `broken-suite`) runs
  `broken_tests/test_broken.py`, which always fails, to verify the detector
  classifies consistently failing jobs as broken rather than flaky.
