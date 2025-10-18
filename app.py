import streamlit as st
import datetime
from database import create_tables, add_habit, get_habits, log_habit, get_logs
from openai_agent import generate_weekly_summary

st.set_page_config(page_title="Habit Tracker Agent", page_icon="🔥", layout="centered")

create_tables()

st.title("🔥 Habit Tracker Agent")
st.caption("Track your daily habits and get AI-powered weekly insights!")

# --- Add New Habit ---
st.header("➕ Add a New Habit")
with st.form("add_habit_form"):
    habit_name = st.text_input("Habit Name")
    frequency = st.selectbox("Frequency", ["daily", "weekly"])
    submitted = st.form_submit_button("Add Habit")
    if submitted and habit_name:
        add_habit(habit_name, frequency)
        st.success(f"Habit '{habit_name}' added successfully!")

# --- Log Habit Completion ---
st.header("✅ Log Habit Progress")
habits = get_habits()
if habits:
    habit_choices = {name: _id for _id, name, _ in habits}
    selected_habit = st.selectbox("Select Habit", list(habit_choices.keys()))
    status = st.radio("Status", ["completed", "missed"])
    date = st.date_input("Date", datetime.date.today())
    if st.button("Log Habit"):
        log_habit(habit_choices[selected_habit], date.strftime("%Y-%m-%d"), status)
        st.success(f"Logged '{selected_habit}' as {status} for {date}.")
else:
    st.warning("No habits found. Add one above!")

# --- View Logs ---
st.header("📅 Habit Logs")
logs = get_logs()
if logs:
    st.table(logs)
else:
    st.info("No logs yet. Start logging your habits!")

# --- Weekly Summary ---
st.header("🧠 Weekly AI Summary")
if st.button("Generate Weekly Summary"):
    with st.spinner("Generating insights..."):
        summary = generate_weekly_summary()
        st.success("Here’s your weekly summary:")
        st.write(summary)
