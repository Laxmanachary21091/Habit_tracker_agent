🔥 Habit Tracker Agent

🧠 AI-powered habit tracking and motivation system built with Python, Streamlit, SQLite, and OpenAI.
📘 Overview

The Habit Tracker Agent helps you build consistency by tracking your daily habits, reminding you to complete them, and generating AI-powered weekly summaries that motivate you to stay on track.

With an interactive Streamlit dashboard, you can:

Add and manage daily or weekly habits

Log progress easily

View your activity history

Generate motivational weekly summaries using OpenAI GPT

🧩 Features

✅ Add new habits with custom frequency
✅ Log daily or weekly completion status
✅ View all logs in a clean table view
✅ Generate AI-based summaries using OpenAI
✅ (Optional) Daily reminders using schedule
✅ Simple and lightweight (SQLite for storage)
✅ Beautiful Streamlit UI

🏗️ Project Structure
habit_tracker_agent/
│
├── app.py              # Streamlit main app
├── database.py         # Handles SQLite database & CRUD operations
├── openai_agent.py     # Generates AI-based weekly summaries
├── reminder.py         # (Optional) For scheduling reminders
├── requirements.txt    # Dependencies
└── habits.db           # Auto-created SQLite database


▶️ Run the App

Launch the Streamlit dashboard:

streamlit run app.py


It will open automatically in your browser at
👉 http://localhost:8501

💻 Usage
➕ Add a Habit

Enter a habit name (e.g., "Exercise") and choose a frequency ("daily" or "weekly").

✅ Log Habit Progress

Select a habit, mark as completed or missed, and save.

📅 View Habit Logs

See all your logged progress in a structured table.

🧠 Weekly Summary

Click “Generate Weekly Summary” — the AI agent will create a personalized motivational report using your last week’s data.

🧠 Example Weekly Summary (AI Output)

💪 Great job this week! You completed 5 out of 7 exercise sessions and maintained a strong reading streak.
Stay consistent — small habits build big results! 🌱

🧰 Technologies Used
Component	Technology
Frontend/UI	Streamlit
Database	SQLite
AI Summaries	OpenAI GPT (via openai library)
Scheduler	schedule
Language	Python 3.x
🌟 Future Improvements

📊 Add progress charts & streak visualization

📱 Send notifications or email reminders

🏆 Add achievements & badges

☁️ Deploy on Streamlit Cloud or Hugging Face Spaces
