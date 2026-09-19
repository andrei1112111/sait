from sait.main import main


def test_greet_success(runner):
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Hey! You are using the Simple AI Tools!" in result.output
