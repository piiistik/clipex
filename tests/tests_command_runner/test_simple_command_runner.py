from clipex.core.command_runner.simple_runner import SimpleRunner
from pytest import approx


# def test_simple_runner_result():
#     runner = SimpleRunner(iterations=5, timeout=5)

#     commands = ["timeout /t 1 /nobreak >nul"]
#     try:
#         result = runner.run(commands)
#     except Exception as e:
#         assert False, f"Runner raised an exception: {e}"

#     assert result == approx([1], rel=0.1)


def test_simple_runner_dispersion():
    runner = SimpleRunner(iterations=5, timeout=5)

    commands = ["ls ."] * 10

    try:
        result = runner.run(commands)
    except Exception as e:
        assert False, f"Runner raised an exception: {e}"

    assert abs(min(result) - max(result)) < 0.05
