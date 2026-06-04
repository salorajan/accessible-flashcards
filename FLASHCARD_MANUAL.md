# How to Create Your Own Flashcards

The app reads flashcards from a file named `flashcards.json`. You can easily add your own questions and answers using any text editor (like Notepad) or by using an AI.

## 1. Using AI to Create Flashcards (Recommended)
You can copy and paste the prompt below into ChatGPT, Gemini, or Claude to generate a perfect flashcard file for any topic.

**Copy this prompt:**
> "Act as an educational content creator. I need a flashcard set in JSON format for the topic: [INSERT TOPIC HERE]. 
> Please provide exactly 10 cards. 
> The format MUST be a list of objects where each object has a 'question' and an 'answer' key. 
> IMPORTANT: For math or complex terms, write the text exactly how it should be SPOKEN by a screen reader (e.g., use 'squared' instead of '^2'). 
> Return ONLY the raw JSON code block."

---

## 2. Bypassing Windows "SmartScreen" / Blocked App
Because this is a custom-made app and not signed by a large company like Microsoft, Windows might show a blue "Windows protected your PC" screen.

**How to run it:**
1.  Click **"More info"** on the blue screen.
2.  Click **"Run anyway"**.
*Alternatively:* Right-click `app.exe`, select **Properties**, check the box that says **"Unblock"** at the bottom, and click OK.

---

## 3. Manual Step-by-Step Guide
If you want to edit the file yourself:

1.  **Open the file:** Find `flashcards.json` in the same folder as the app and right-click to "Open with Notepad".
2.  **Follow the Format:** Each card must be inside curly braces `{ }`.
3.  **Use Quotes:** Always put text inside double quotes `"`.

### Example Format:
```json
[
    {
        "question": "What is the square root of 64?",
        "answer": "8"
    }
]
```

## Tips for Better Accessibility
*   **Keep it Simple:** Write questions exactly as you want them to be spoken.
*   **Phonetic Spelling:** If a name is hard for the computer to pronounce, you can spell it phonetically (e.g., "Eye-zak Newton").
