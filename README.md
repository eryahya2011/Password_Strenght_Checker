# Password_Strenght_Checker

# 🔐 Password Strength Checker

## 📌 Overview

A lightweight Python command-line tool that checks the strength of a password based on essential security criteria such as length, uppercase/lowercase letters, digits, and special characters. It provides immediate feedback to help users create stronger passwords.

---

## 🚀 Features

* Validates minimum password length (8 characters)
* Detects numeric characters
* Ensures use of uppercase and lowercase letters
* Checks for special characters using regex
* Continuous input loop until user exits
* Clear feedback messages (Weak / Medium / Strong)

---

## 🛠️ Tech Stack

* Python 3
* Built-in `re` module (Regular Expressions)

---

## ▶️ Usage

Run the script using:

```bash
python password_checker.py
```

---

## 💡 Example

```
Welcome To The Password Strength Checker Tool.
Enter Your Password or (type 'exit' to quit): Hello123
Weak: Password Must Contain a Special Char.

Enter Your Password or (type 'exit' to quit): Hello@123
Congrats! Your Password Is Strong.
```

---

## ⚙️ Validation Rules

A strong password must contain:

* At least 8 characters
* At least 1 digit
* At least 1 uppercase letter
* At least 1 lowercase letter
* At least 1 special character (`!@#$%^&*().?`)

---

## 📈 Future Improvements

* GUI version (Tkinter / PyQt)
* Password strength scoring system
* Suggestion engine for stronger passwords

---

## 📜 License

This project is open-source and available for learning purposes.
