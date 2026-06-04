import json
import pyttsx3
import sys
import random
import msvcrt

class FlashcardApp:
    def __init__(self, data_file='flashcards.json'):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175)  # Slightly faster for efficient review
        self.cards = self.load_cards(data_file)
        self.current_card_index = 0
        self.score = {"correct": 0, "incorrect": 0}

    def load_cards(self, file_path):
        try:
            with open(file_path, 'r') as f:
                cards = json.load(f)
                random.shuffle(cards)
                return cards
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Failed to decode {file_path}.")
            sys.exit(1)

    def speak(self, text, wait=True):
        print(f"{text}")
        self.engine.say(text)
        if wait:
            self.engine.runAndWait()

    def get_key(self):
        """Waits for a single key press and returns it."""
        return msvcrt.getch().decode('utf-8').lower()

    def show_instructions(self):
        msg = (
            "Instructions. "
            "Press Space to hear the question. "
            "Press Space again to hear the answer. "
            "After hearing the answer, press Y if you got it right, or N if you got it wrong. "
            "Press R at any time to repeat. "
            "Press Q to quit."
        )
        self.speak(msg)

    def run(self):
        self.speak("Welcome to Accessible Flashcards.")
        self.show_instructions()
        
        while self.current_card_index < len(self.cards):
            card = self.cards[self.current_card_index]
            
            # 1. Question phase
            self.speak(f"Card {self.current_card_index + 1}. Press Space for the question.")
            while True:
                key = self.get_key()
                if key == ' ':
                    self.speak(card['question'])
                    break
                elif key == 'r':
                    self.speak("Repeating.")
                    self.speak(f"Card {self.current_card_index + 1}.")
                elif key == 'q':
                    self.quit_app()
                    return

            # 2. Answer phase
            self.speak("Press Space for the answer.")
            while True:
                key = self.get_key()
                if key == ' ':
                    self.speak(f"The answer is: {card['answer']}")
                    break
                elif key == 'r':
                    self.speak(card['question'])
                elif key == 'q':
                    self.quit_app()
                    return

            # 3. Scoring phase
            self.speak("Did you get it right? Press Y for Yes or N for No.")
            while True:
                key = self.get_key()
                if key == 'y':
                    self.score["correct"] += 1
                    self.speak("Correct! Moving to next card.")
                    break
                elif key == 'n':
                    self.score["incorrect"] += 1
                    self.speak("Incorrect. Moving to next card.")
                    break
                elif key == 'r':
                    self.speak(f"The answer was: {card['answer']}")
                elif key == 'q':
                    self.quit_app()
                    return

            self.current_card_index += 1

        self.speak("End of session.")
        self.quit_app()

    def quit_app(self):
        total = self.score["correct"] + self.score["incorrect"]
        summary = f"You finished {total} cards. You got {self.score['correct']} right and {self.score['incorrect']} wrong. Goodbye."
        self.speak(summary)
        sys.exit(0)

if __name__ == "__main__":
    app = FlashcardApp()
    app.run()
