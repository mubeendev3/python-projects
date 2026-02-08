# Python Projects Collection

A collection of practical Python applications demonstrating various programming concepts and real-world utilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies](#technologies)

## 🎯 Overview

This repository contains three standalone Python applications:

1. **Word Counter** - Analyze text statistics (characters, words, sentences)
2. **Currency Converter** - Convert between currencies using live exchange rates
3. **Number Guessing Game** - Interactive number guessing game with hints

Each project is self-contained and can be run independently.

## 📦 Projects

### 1. Word Counter (`word_counter.py`)

A text analysis tool that counts characters, words, and sentences in user-provided text.

**Features:**
- Character count
- Word count
- Sentence count (based on punctuation: `.`, `!`, `?`)

### 2. Currency Converter (`currency_convertor.py`)

A real-time currency conversion tool that fetches live exchange rates from an API.

**Features:**
- Live exchange rate data
- Support for multiple currencies
- Real-time conversion calculations
- Error handling for invalid currencies

### 3. Number Guessing Game (`number_guessing_game.py`)

An interactive game where players guess a randomly generated number within a specified range.

**Features:**
- Configurable number range (default: 1-100)
- Input validation
- Attempt counter
- Helpful hints (too high/too low)

## 📋 Requirements

- Python 3.7 or higher
- `requests` library (for currency converter only)

## 🔧 Installation

1. **Clone or download this repository**

2. **Install required dependencies:**

   ```bash
   pip install requests
   ```

   Or if you're using Python 3 specifically:

   ```bash
   pip3 install requests
   ```

## 🚀 Usage

### Word Counter

Run the word counter application:

```bash
python word_counter.py
```

**Example:**
```
📝 Word Counter Application
Enter your text: Hello world! This is a test.

--- Text Statistics ---
Characters: 28
Words: 5
Sentences: 1
```

### Currency Converter

Run the currency converter:

```bash
python currency_convertor.py
```

**Example:**
```
💱 Currency Converter
Enter amount: 100
From currency (e.g. USD): USD
To currency (e.g. PKR): PKR
100.0 USD = 27850.00 PKR
```

**Note:** Currency codes should be in ISO 4217 format (e.g., USD, EUR, GBP, PKR, etc.)

### Number Guessing Game

Run the number guessing game:

```bash
python number_guessing_game.py
```

**Example:**
```
🎯 Welcome to the Number Guessing Game!
I have selected a number between 1 and 100.
Enter your guess (1–100): 50
Too high! Try again.
Enter your guess (1–100): 25
Too low! Try again.
Enter your guess (1–100): 37
🎉 Correct! You guessed the number in 3 attempts.
```

## 📁 Project Structure

```
Python Projects/
│
├── README.md                 # Project documentation
├── word_counter.py          # Word counting application
├── currency_convertor.py    # Currency conversion tool
└── number_guessing_game.py  # Number guessing game
```

## ✨ Features

- **Clean Code**: Well-structured, readable Python code with type hints
- **Error Handling**: Robust error handling for user inputs and API calls
- **User-Friendly**: Interactive command-line interfaces with clear prompts
- **Modular Design**: Each script is self-contained and can be run independently
- **Documentation**: Comprehensive docstrings for all functions

## 🛠 Technologies

- **Python 3.7+** - Programming language
- **requests** - HTTP library for API calls (currency converter)
- **random** - Built-in module for random number generation (guessing game)

## 📝 Notes

- The currency converter uses the [ExchangeRate-API](https://www.exchangerate-api.com/) for live exchange rates
- All applications are command-line based and require user interaction
- The word counter uses simple punctuation-based sentence detection

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features.

## 📄 License

This project is open source and available for educational purposes.

---

**Happy Coding! 🚀**

