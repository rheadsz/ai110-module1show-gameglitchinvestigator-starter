# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran the game, it launched successfully in the browser using Streamlit, but the behavior of the game was incorrect and confusing. The interface worked, but the game logic seemed broken.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
One bug I noticed was that the hints were incorrect. No matter what number I entered, even very low numbers like 0, the game always responded with "Go lower." I expected the game to tell me to go higher when my guess was too low.

Another issue was that the game allowed invalid inputs such as negative numbers. Even when I entered a number outside the given range (1–100), the game still processed it and gave a misleading hint instead of rejecting the input.

A third bug was with the attempt counter. The game stated that I had 8 attempts, but it ended early after around 5 guesses and said I was out of attempts, which did not match the expected behavior.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used GitHub Copilot as AI tools for this project. I used Copilot inside VS Code to analyze the codebase and explain the bugs, and ChatGPT to better understand how to fix the issues step by step.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One correct suggestion from AI was identifying that the hint logic in the check_guess function was flipped. The AI pointed out that when the guess was greater than the secret, the game incorrectly told the user to go higher. I verified this by testing the game manually and confirming that the hints were incorrect, then fixed the logic and saw the correct behavior.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One misleading suggestion from AI was not clearly identifying the issue with the secret value being converted into a string on alternating attempts. This caused inconsistent comparisons and unexpected behavior. I identified this issue by reading the code and noticing the type mismatch, then fixed it by keeping the secret value as an integer throughout.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed by both manually testing the game and observing the behavior in the Streamlit app. I checked whether the hints were correct and whether the number of attempts matched what was expected.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  One test I ran was manually guessing numbers above and below the secret value to confirm that the hints were correct. For example, when I guessed a number higher than the secret, the game correctly told me to go lower. I also used pytest to create automated tests for the check_guess function to ensure it returned the correct outcomes.
- Did AI help you design or understand any tests? How?
AI helped me design the pytest tests by suggesting how to structure simple test cases. This made it easier to verify the correctness of the logic without relying only on manual testing.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the entire script every time the user interacts with the app, such as clicking a button or entering input. Because of this, variables would normally reset each time unless we store them in session state.

Session state allows us to keep track of values like the secret number, attempts, and score across reruns. Without session state, the game would not function correctly because it would forget previous guesses and progress.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I want to reuse is carefully testing code step by step instead of immediately trusting AI-generated solutions. This helped me catch issues that were not obvious at first.

Next time, I would be more critical of AI suggestions and verify each change more systematically instead of assuming it is correct. I would also break problems into smaller parts when asking AI for help.

This project changed the way I think about AI-generated code by showing me that AI can be helpful but is not always reliable. It is important to review, test, and understand the code rather than blindly trusting it.
