from logic_utils import check_guess

def test_check_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_check_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"