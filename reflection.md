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


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
