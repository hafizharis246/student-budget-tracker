import streamlit as st
import sqlite3
from datetime import date
import pandas as pd


# Initialize SQLite database
def init_db():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()


# Save expense to database
def save_expense(amount, category, date):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
              (amount, category, date))
    conn.commit()
    conn.close()


# Get expenses from database
def get_expenses():
    conn = sqlite3.connect("expenses.db")
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df


# Delete expense from database
def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()


# Generate savings tip
def get_savings_tip(expenses):
    if expenses.empty:
        return "No expenses yet. Start tracking to get tips!"
    summary = expenses.groupby("category")["amount"].sum()
    top_category = summary.idxmax()
    tips = {
        "Food": "Cook at home to save on dining out.",
        "Transport": "Use public transport to reduce costs.",
        "Entertainment": "Look for free events or student discounts.",
        "Other": "Review miscellaneous expenses for savings."
    }
    return tips.get(top_category, "Spend wisely!")


# Call init_db at the start
init_db()

# Main app
st.title("AI Budget Tracker for Students")
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Dashboard"])

if page == "Home":
    st.header("Track Your Expenses")
    with st.form("expense_form"):
        amount = st.number_input("Amount ($)", min_value=0.01, step=0.01)
        category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Other"])
        expense_date = st.date_input("Date", value=date.today())
        submit = st.form_submit_button("Submit")
        if submit:
            save_expense(amount, category, str(expense_date))
            st.success("Expense saved!")
    # Footer with badge
    st.markdown("---")
    st.markdown("Built with:")
    st.image("logotext_poweredby_360w.png", width=100)

elif page == "Dashboard":
    st.header("Your Spending")
    expenses = get_expenses()
    if not expenses.empty:
        # Summary by category
        summary = expenses.groupby("category")["amount"].sum().reset_index()
        st.subheader("Total Spending by Category")
        st.dataframe(summary.style.format({"amount": "${:.2f}"}))
        st.markdown("<br>", unsafe_allow_html=True)
        # Expense list with delete buttons
        st.subheader("All Expenses")
        st.markdown("**Date | Category | Amount | Action**")
        for index, row in expenses.iterrows():
            col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
            with col1:
                st.write(row['date'])
            with col2:
                st.write(row['category'])
            with col3:
                st.write(f"${row['amount']:.2f}")
            with col4:
                if st.button("Delete", key=f"delete_{row['id']}"):
                    delete_expense(row['id'])
                    st.success(f"Expense ID {row['id']} deleted!")
                    st.rerun()  # Refresh the page
        st.markdown("<br>", unsafe_allow_html=True)
        # AI savings tip
        st.subheader("Savings Tips")
        st.write(get_savings_tip(expenses))
    else:
        st.write("No expenses recorded yet.")
    # Footer with badge
    st.markdown("---")
    st.markdown("Built with:")
    st.image("logotext_poweredby_360w.png", width=100)