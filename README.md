# 🏦 Banking Simulator with Excel Integration

## 📋 Overview
This is a command-line based Banking Simulator written in Python that performs core banking operations such as **deposit**, **withdrawal**, and **balance check**. The data is fetched from an Excel file using `pandas`, and the system ensures user authentication via **account number**, **holder name**, and **PIN** verification.

## 🚀 Features

- 🔐 **Secure Access**: Each account is protected with a PIN. Users get 3 attempts to enter the correct PIN.
- 🧑‍💼 **Multi-Factor Authentication**: Account access requires both the correct account number and the associated holder's name.
- 💰 **Banking Operations**:
  - Deposit funds
  - Withdraw funds
  - Check account balance
- 🔁 **Repeatable Sessions**: The simulator runs in a loop allowing multiple banking sessions until the user decides to exit.
- 📂 **Excel Integration**:
  - Account details are loaded from an Excel file.
  - Operates on the loaded data during the session.
  - *(Known Flaw)*: Changes made during the session do not persist to the Excel file after execution.

## 🛠️ Technologies Used
- `numpy`
- `pandas`

## 📂 File Structure

```plaintext
.
├── main.py                    # Main Python file
├── banking data sim.xlsx      # Excel file with account data
└── README.md                  # Project documentation
