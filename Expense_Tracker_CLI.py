import mysql.connector
import argparse
from datetime import datetime

# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",       # Change if needed
        user="root",            # Your MySQL username
        password="Bhavesh@2006", # Your MySQL password
        database="expense_tracker_cli"
    )

# ---------- Initialize DB ----------
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE NOT NULL,
            description VARCHAR(255),
            category VARCHAR(100),
            amount DECIMAL(10,2) NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ---------- Add Expense ----------
def add_expense(amount, description, category):
    conn = get_connection()
    cursor = conn.cursor()
    today = datetime.now().date()
    cursor.execute("INSERT INTO expenses (date, description, category, amount) VALUES (%s, %s, %s, %s)",
                   (today, description, category, amount))
    conn.commit()
    conn.close()
    print(f"✅ Added: {amount} for {description} [{category}] on {today}")

# ---------- View Expenses ----------
def view_expenses(month=None):
    conn = get_connection()
    cursor = conn.cursor()
    if month:
        cursor.execute("SELECT * FROM expenses WHERE DATE_FORMAT(date, '%%Y-%%m') = %s", (month,))
    else:
        cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No expenses found.")
        return

    print("\nID | Date       | Amount   | Category   | Description")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<3}| {row[1]} | {row[4]:<8} | {row[3]:<10} | {row[2]}")

# ---------- Delete Expense ----------
def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
    conn.commit()
    conn.close()
    print(f"🗑️ Deleted expense with ID {expense_id}")

# ---------- Monthly Total ----------
def monthly_total(month):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE DATE_FORMAT(date, '%%Y-%%m') = %s", (month,))
    total = cursor.fetchone()[0]
    conn.close()
    if total:
        print(f"💰 Total for {month}: {total}")
    else:
        print(f"No expenses found for {month}")

# ---------- Main CLI ----------
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI (MySQL Version)")
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # Add
    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("amount", type=float)
    add_parser.add_argument("description", type=str)
    add_parser.add_argument("--category", default="General")

    # View
    view_parser = subparsers.add_parser("view", help="View expenses")
    view_parser.add_argument("--month", type=str, help="Filter by month (YYYY-MM)")

    # Delete
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("id", type=int)

    # Total
    total_parser = subparsers.add_parser("total", help="Show total expenses for a month")
    total_parser.add_argument("month", type=str)

    args = parser.parse_args()

    if args.cmd == "add":
        add_expense(args.amount, args.description, args.category)
    elif args.cmd == "view":
        view_expenses(args.month)
    elif args.cmd == "delete":
        delete_expense(args.id)
    elif args.cmd == "total":
        monthly_total(args.month)

if __name__ == "__main__":
    init_db()
    main()
