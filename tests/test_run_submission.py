from run_submission import run_submission_simulation


class TestTestSubmission:

    def test_run_submission(self):
        player = 'run_right'
        opponent = 'run_right'

        result = run_submission_simulation(player, opponent)
        assert isinstance(result, list)
        assert all([isinstance(score, int) for score in result])
        # Scores can't be negative.
        assert all([score >= 0 for score in result])
        assert len(result) == 2
