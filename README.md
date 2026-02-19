# 🇫🇷 French Flash Card Program

A simple flashcard game built with Python and Tkinter to help memorize
French vocabulary.

The app displays a French word, flips the card after a few seconds to
reveal the English translation, and removes correctly answered words
from rotation so you focus only on what you still need to learn.

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 3
-   Tkinter (GUI)
-   Pandas (CSV handling)

------------------------------------------------------------------------

## 📦 Installation

pip install pandas

> Tkinter usually comes pre-installed with Python.

------------------------------------------------------------------------

## ▶️ Run the Program

python main.py

------------------------------------------------------------------------

## 📂 How It Works

-   Loads words from:
    -   data/words_to_learn.csv (if it exists)
    -   Otherwise data/french_words.csv
-   Displays a random French word.
-   Flips the card after 3 seconds.
-   ✅ Right → Word is removed and progress is saved.
-   ❌ Wrong → Word stays in rotation.

Progress is automatically saved in data/words_to_learn.csv.

------------------------------------------------------------------------

## ⚙️ Customization

Change the flip timer inside the script:

timer_secs = 3

Edit data/french_words.csv to add more vocabulary.