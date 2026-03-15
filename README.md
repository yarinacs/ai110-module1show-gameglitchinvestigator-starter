# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose: The game is a number guessing app where players try to guess a secret number within a range based on difficulty (Easy: 1-20, Normal: 1-100, Hard: 1-50). It provides hints ("Too High" or "Too Low") and tracks attempts and score.
- [x] Detail which bugs you found: 1. Hints were reversed (said "Go Higher" when guess > secret). 2. Attempt limits were swapped (Easy had fewer attempts than Normal). 3. Attempts counter started at 1, causing premature game over. 4. Secret number used wrong range on "New Game". 5. Scoring penalized wins too much.
- [x] Explain what fixes you applied: Refactored logic functions to logic_utils.py. Fixed check_guess to use numeric comparisons. Corrected attempt limits and initialization. Updated scoring formula. Added imports and calls in app.py. Added pytest test for scoring.

## 📸 Demo

- [x] [Insert a screenshot of your fixed, winning game here]
- [x] Challenge 1 Completed: [Insert a screenshot of pytest results showing all tests passing here]

Pytest Results Summary:
============================= test session starts ==============================
platform darwin -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
collected 4 items

tests/test_game_logic.py::test_winning_guess PASSED
tests/test_game_logic.py::test_guess_too_high PASSED
tests/test_game_logic.py::test_guess_too_low PASSED
tests/test_game_logic.py::test_update_score_win_early PASSED

============================== 4 passed in 0.04s ==============================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
