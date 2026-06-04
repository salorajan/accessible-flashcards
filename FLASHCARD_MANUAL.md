# Accessible Flashcards for the Blind - Manual & Instructions

This application is designed to provide a 100% accessible study experience for blind and visually impaired users. It uses offline Text-to-Speech (TTS) and a simple keyboard-driven interface.

---

## 1. How to Use the App (Keyboard Shortcuts)
The app is designed to be used entirely without a mouse.

*   **Spacebar**:
    *   Press once to hear the **Question**.
    *   Press again to hear the **Answer**.
*   **'Y' Key**: Mark the card as **Correct**.
*   **'N' Key**: Mark the card as **Incorrect**.
*   **'R' Key**: **Repeat** the current audio (Question or Answer).
*   **'Q' Key**: **Quit** the session and hear your final score summary.

---

## 2. Setting Up Your Cards (JSON Format)
The app reads questions from a file named `flashcards.json`. You can create your own topics by editing this file in a simple text editor like Notepad.

### Example Format:
```json
[
    {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
    {
        "question": "What is 10 times 10?",
        "answer": "100"
    }
]
```

### Tips for Better Accessibility:
*   **Math Expressions**: Use words instead of symbols. Write "x squared" instead of "x^2".
*   **Phonetic Spelling**: If the computer mispronounces a word, spell it phonetically (e.g., write "Eye-zak" instead of "Isaac").

---

## 3. Use AI to Create Content
You can use ChatGPT, Gemini, or Claude to generate your `flashcards.json` file instantly. 

**Copy and paste this prompt:**
> "Act as an educational content creator. I need a flashcard set in JSON format for the topic: [INSERT YOUR TOPIC HERE]. 
> Please provide exactly 10 cards. 
> The format MUST be a list of objects where each object has a 'question' and an 'answer' key. 
> IMPORTANT: Write all math and complex terms exactly how they should be SPOKEN (e.g., use 'squared' instead of '^2'). 
> Return ONLY the raw JSON code block."

---

## 4. Troubleshooting: Windows SmartScreen
Since this is a custom tool, Windows may block it initially.
1.  Click **"More info"** on the blue warning screen.
2.  Click **"Run anyway"**.
3.  Alternatively, right-click `app.exe`, go to **Properties**, and check **"Unblock"** at the bottom.

---

## 5. Website Elements (For Sighted Helpers)
The landing page at [salorajan.github.io/accessible-flashcards/](https://salorajan.github.io/accessible-flashcards/) contains:
*   **Header**: "Accessible Flashcards for the Blind".
*   **Description**: Overview of the app's goals and technology.
*   **Download Section**: A green button to download `app.exe` and a link to `flashcards.json`.
*   **Keyboard Guide**: A list of the shortcuts (`Space`, `Y`, `N`, `R`, `Q`).
*   **Family Guide**: Brief instructions on how to customize cards.
*   **Manual Link**: A link to this full manual.
