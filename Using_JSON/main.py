import json
import streamlit as st

#import class modules
from Using_JSON.account import *

st.set_page_config(page_title="My Streamlit App", page_icon=":bank:",layout='wide')

# load the account dictionary from file
try:
    with open('accounts.json', 'r') as f:
        accounts = json.load(f)
except FileNotFoundError:
    accounts = {}


st.title("welcome To CDAC Central Bank")
st.sidebar.title("Menu")
choice = st.sidebar.radio("", ("Create account", "Withdraw", "Deposit", "Check balance"))

if choice == "Create account":
        first_name = st.text_input("Enter account holder's name: ")
        initial_deposit = st.number_input("Enter initial deposit amount: ", min_value=0, step=1)
        if st.button("Create account"):
            account_number = BankAccount.create_account(name, initial_deposit)
            st.success(f"Account created successfully. Account number is {account_number}.")

# withdraw
elif choice == "Withdraw":
    account_number = st.number_input("Enter account number: ", min_value=0, step=1)
    if st.button("Submit"):
        if account_number in accounts:
            amount = st.number_input("Enter amount to withdraw: ", min_value=0, step=1)
            name, balance = accounts[account_number]
            account = BankAccount(name, balance)
            if st.button("Withdraw"):
                account.withdraw(amount)
                accounts[account_number] = account.account_info()
        else:
            st.warning("Invalid account number.")

# deposit
elif choice == "Deposit":
    account_number = st.number_input("Enter account number: ", min_value=0, step=1)
    if st.button('Submit'):
        if account_number in accounts:
            amount = st.number_input("Enter amount to deposit: ", min_value=0, step=1)
            name, balance = accounts[account_number]
            account = BankAccount(name, balance)
            if st.button("Deposit"):
                account.deposit(amount)
                accounts[account_number] = account.account_info()
        else:
            st.warning("Invalid account number.")

# check balance
elif choice == "Check balance":
    account_number = st.number_input("Enter account number: ", min_value=0, step=1)
    if st.button("Submit"):
        if account_number in accounts:
            name, balance = accounts[account_number]
            st.success(f"Account holder: {name}")
            st.success(f"Current balance: {balance}")
        else:
            st.warning("Invalid account number.")