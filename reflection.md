# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
the game gave me the hint in the info so i type the hint directly
- List at least two concrete bugs you noticed at the start
1. when the guest is higher than the secret, it said"Go Higher" which should be "Go Lower"
2. The count of the remaining attempt is calculated wrongly. When there is 1 attempt left, it showed game over. It should be shows 1 attempt left.
3. In the settings part, the normal version's attempt times is 8, which is more than easy version, which is 6 now. It should be 8 in the easy version and 6 in the normal version.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

n check_guess at app.py:37-47:


if guess > secret:          # int vs string — TypeError in Python 3
    return "Too High", "📈 Go HIGHER!"
Python 3 can't compare int > str directly — it raises a TypeError, which is caught at line 41. The fallback then does string comparison:


g = str(guess)   # "42"
if g > secret:   # "42" > "7" → False! (string, not numeric comparison)
"42" > "7" is False because "4" < "7" alphabetically, even though 42 > 7 numerically. This flips the hint direction on even attempts.

This is why you see "Go Higher" when you should see "Go Lower" — it's not a simple copy-paste error, it's the result of a type mismatch cascading into broken string comparison logic. The bug was intentionally seeded by that str() conversion on even attempts.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI initially suggested keeping the update_score calculation with the +1 in the points formula, claiming it was correct, but this penalized wins too harshly (e.g., win on attempt 1 got 80 instead of 90).

I verified by running the new test I added, which failed until I removed the +1, and then it passed, confirming the fix.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed by running pytest to ensure all tests passed, and by manually testing the game in the browser to verify behaviors like correct hints, proper attempt counting, and stable secret numbers.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran pytest on tests/test_game_logic.py, which showed all 4 tests passing, including the new test_update_score_win_early that specifically checked the scoring fix. This confirmed the logic was correct and the refactoring didn't break anything.

- Did AI help you design or understand any tests? How?
Yes, the AI suggested adding a test case for the update_score bug, which helped me understand how to write a targeted test that verifies the scoring rewards fewer attempts properly. It guided me to create assertions that check the difference in scores for early vs. late wins.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because Streamlit reruns the entire script every time you interact with the app, like clicking a button. If the secret wasn't stored in session_state, it would get reset to a new random number on each rerun, making the game impossible to win.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns are like refreshing the whole app every time you do something, like clicking a button—it re-executes all the code from top to bottom. Session state is like a persistent storage box that remembers values across these reruns, so things like your score or secret number don't disappear when the app refreshes.

- What change did you make that finally gave the game a stable secret number?
I initialized the secret number in session_state only if it wasn't already set, and ensured it uses the correct range based on the selected difficulty. This way, it persists across reruns instead of changing every time.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Using pytest to test logic functions separately from the UI, which made debugging much easier and ensured the core logic was solid before integrating with Streamlit.

- What is one thing you would do differently next time you work with AI on a coding task?
I would test AI suggestions immediately rather than assuming they're correct, and not hesitate to reject or modify them if they don't work, as happened with the scoring formula.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code can have subtle bugs and isn't always production-ready, so I now approach it with more skepticism and always verify through testing. It also highlighted AI's strength as a collaborative tool for refactoring and debugging, making me more confident in using it as a partner rather than a crutch.
