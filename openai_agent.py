from openai import OpenAI
import sqlite3
from datetime import datetime, timedelta

client = OpenAI(api_key="your_opemai_key")

def generate_weekly_summary():
    conn = sqlite3.connect("habits.db")
    c = conn.cursor()
    last_week = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    c.execute("""
        SELECT h.name, l.date, l.status
        FROM logs l
        JOIN habits h ON h.id = l.habit_id
        WHERE l.date >= ?
    """, (last_week,))
    
    data = c.fetchall()
    conn.close()

    if not data:
        return "No logs found this week. Start tracking your habits today!"

    text_data = "\n".join([f"{row[0]} - {row[1]} - {row[2]}" for row in data])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a motivational habit coach."},
            {"role": "user", "content": f"Here are my last week's habit logs:\n{text_data}\nCreate a motivational summary and insights."}
        ]
    )

    return response.choices[0].message.content
