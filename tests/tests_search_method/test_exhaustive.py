from clipex.core.search_method.exhaustive import Exhaustive


def test_exhaustive_single_variable():
    variable_ranges = [(0, 2)]
    exhaustive = Exhaustive(variable_ranges)

    search_space = exhaustive.step([])

    expected_combinations = [
        ((0,), None),
        ((1,), None),
        ((2,), None),
    ]

    assert len(search_space) == len(expected_combinations)
    for combo in expected_combinations:
        assert combo in search_space


def test_exhaustive_two_variables():
    variable_ranges = [(0, 1), (0, 2)]
    exhaustive = Exhaustive(variable_ranges)

    search_space = exhaustive.step([])

    expected_combinations = [
        ((0, 0), None),
        ((0, 1), None),
        ((0, 2), None),
        ((1, 0), None),
        ((1, 1), None),
        ((1, 2), None),
    ]

    assert len(search_space) == len(expected_combinations)
    for combo in expected_combinations:
        assert combo in search_space


def test_exhaustive_three_variables():
    variable_ranges = [(0, 1), (0, 1), (0, 1)]
    exhaustive = Exhaustive(variable_ranges)

    search_space = exhaustive.step([])

    expected_combinations = [
        ((0, 0, 0), None),
        ((0, 0, 1), None),
        ((0, 1, 0), None),
        ((0, 1, 1), None),
        ((1, 0, 0), None),
        ((1, 0, 1), None),
        ((1, 1, 0), None),
        ((1, 1, 1), None),
    ]

    assert len(search_space) == len(expected_combinations)
    for combo in expected_combinations:
        assert combo in search_space


def test_exhaustive_empty_ranges():
    variable_ranges = []
    exhaustive = Exhaustive(variable_ranges)

    search_space = exhaustive.step([])

    expected_combinations = [
        ((), None),
    ]

    assert len(search_space) == len(expected_combinations)
    for combo in expected_combinations:
        assert combo in search_space


def test_exhaustive_incorrect_ranges():
    variable_ranges = [(5, 3)]  # Invalid range where low > high
    exhaustive = Exhaustive(variable_ranges)

    search_space = exhaustive.step([])

    # Expecting no combinations since the range is invalid
    assert len(search_space) == 0
