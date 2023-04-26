import streamlit as st
from accounts import *

st.set_page_config(page_title="My Streamlit App", page_icon=":bank:",layout='wide', initial_sidebar_state='collapsed')


st.title("welcome To CDAC Central Bank")
st.sidebar.title("Menu")
col1, col2 = st.columns([1,3])
choice = col1.radio("", ("Create account", "Withdraw", "Deposit", "Check balance","Test Database Connection"))

if choice == "Create account":
        first_name = col2.text_input("Enter account first name: ")
        last_name = col2.text_input("Enter account Last Name ")
        age = col2.text_input("Enter age")
        dob =col2.date_input(label="Select Date of Birth")
        initial_deposit = col2.text_input("Enter initial deposit amount: ")
        if col2.button("Create account"):
            pass

# withdraw
elif choice == "Withdraw":
    account_number = col2.text_input("Enter account number: ")
    if col2.button("Submit"):
        account_number = int(account_number)
        pass

# deposit
elif choice == "Deposit":
    account_number = col2.text_input("Enter account number: ")
    if col2.button('Submit'):
        account_number = int(account_number)
        pass

# check balance
elif choice == "Check balance":
    account_number = col2.text_input("Enter account number: ")
    if col2.button("Submit"):
       account_number = int(account_number)
       pass

elif choice=="Test Database Connection":
    if col2.button("check status"):
        obj = BankAccount()
        col2.write(obj)