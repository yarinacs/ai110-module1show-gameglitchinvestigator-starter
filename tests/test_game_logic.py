from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_update_score_win_early():
    # Test that winning on fewer attempts gives higher score
    # Win on attempt 1: should be 90 points (100 - 10*1)
    score1 = update_score(0, "Win", 1)
    assert score1 == 90
    
    # Win on attempt 2: should be 80 points (100 - 10*2)
    score2 = update_score(0, "Win", 2)
    assert score2 == 80
    
    # Ensure early win is better
    assert score1 > score2
