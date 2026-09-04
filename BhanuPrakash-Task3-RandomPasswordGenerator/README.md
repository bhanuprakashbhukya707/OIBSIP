# 🔐 Random Password Generator

## 📌 Project Overview

The Random Password Generator is a Python-based application that generates strong and secure random passwords based on user-selected requirements.

This project is developed as *Task 3* and provides an easy-to-use GUI interface where users can select the password length and character types. The application uses Python's secrets module for secure password generation.

## ✨ Features

- 🔢 Choose password length (minimum 8 characters)
- 🔠 Include uppercase letters
- 🔡 Include lowercase letters
- 🔢 Include numbers
- 🔣 Include symbols
- 🛡️ Uses the secrets module for secure password generation
- 💪 Password strength indicator
- 📋 Copy generated password to clipboard
- 🚫 Option to exclude ambiguous characters such as 0, O, 1, l, and I
- 🔄 Generate multiple passwords without restarting the application
- 🕘 Displays the last 5 generated passwords during the current session
- ✅ Ensures at least one character from every selected character type

## 🛠️ Technologies Used

- Python
- Tkinter
- Secrets
- String
- Pyperclip

## 📂 Project Structure

```text
BhanuPrakash-Task3-RandomPasswordGenerator/
│
├── password_generator.py
└── README.md