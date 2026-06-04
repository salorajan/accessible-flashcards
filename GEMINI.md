# Accessible Flashcards for the Blind - Project Plan

This document outlines the architecture, conventions, and roadmap for developing an accessible flashcard application using Python.

## Project Overview
The goal is to create a flashcard application that is fully accessible to blind or visually impaired users. This requires a focus on audio feedback, keyboard-driven navigation, and potentially voice interaction.

## Strategic Technical Choices

### 1. User Interface (UI)
*   **Command Line Interface (CLI):** 
    *   **Decision:** Selected as the primary interface.
    *   **Reasoning:** Naturally compatible with screen readers; allows for fast, keyboard-driven interaction without visual distractions.

### 2. Audio & Feedback
*   **Text-to-Speech (TTS):** 
    *   **Decision:** Using `pyttsx3`.
    *   **Reasoning:** Works 100% offline, cross-platform, and utilizes native OS voices for low latency.

### 3. Data Storage
*   **Format:** JSON.
*   **Decision:** `flashcards.json` will store the question/answer pairs.

### 4. Distribution
*   **Target:** Single Standalone Executable.
*   **Tool:** PyInstaller (to be implemented in Phase 4).

---

## Roadmap

### Phase 1: Research & Setup (Completed)
- [x] Finalize technology stack (CLI, pyttsx3, JSON).
- [x] Verify environment dependencies.

### Phase 2: Core Logic (MVP) (Completed)
- [x] Create `flashcards.json` schema and sample data.
- [x] Implement `app.py` with the following:
    - Card loading and shuffling.
    - `pyttsx3` initialization and speech helper.
    - Keyboard-driven CLI loop (using `msvcrt` for single-key presses).

### Phase 3: Accessibility & UX Refinement (Completed)
- [x] Add "Repeat Question" functionality.
- [x] Implement simple progress tracking (correct/incorrect).
- [x] Add startup instructions read aloud via TTS.

### Phase 4: Packaging
- [ ] Install PyInstaller (if not present).
- [ ] Create a build script or command to bundle `app.py`, `flashcards.json`, and the voice engine dependencies into a single `.exe`.
- [ ] Test the executable on a clean environment if possible.

---

## Conventions
- **Accessibility First:** Every feature must be testable without a monitor.
- **Python Version:** 3.10+
- **Code Style:** PEP 8 compliance.
- **Documentation:** Use docstrings for all functions; maintain this `GEMINI.md` as the source of truth for the project direction.
