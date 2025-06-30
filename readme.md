A web application built for students to track their expenses, view spending summaries, and receive AI-generated savings tips. Initially developed using Bolt.new for the hackathon, the project pivoted to Streamlit due to token limits. The app uses SQLite for data storage and includes the "Built with Bolt.new" badge on both the Home and Dashboard pages.

## Features
- **Expense Tracking**: Input expenses with amount, category (Food, Transport, Entertainment, Other), and date via a form on the Home page.
- **Dashboard**: View total spending by category, a list of all expenses, and AI-generated savings tips (e.g., "Cook at home" for high Food spending).
- **AI Savings Tips**: Rule-based AI suggests savings tips based on the highest-spending category.
- **Mobile-Friendly**: Built with Streamlit, ensuring responsiveness on phones and computers.
- **Bolt.new Badge**: Displayed on both pages to acknowledge the hackathon's initial platform.

## Tech Stack
- **Front-End**: Streamlit (Python-based UI)
- **Back-End**: SQLite (database), Python (logic for AI tips)
- **Deployment**: Streamlit Cloud

## Setup Instructions
1. **Prerequisites**:
   - Python 3.8+ installed ([python.org](https://www.python.org/downloads/)).
   - Git installed ([git-scm.com](https://git-scm.com/)).
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/budget-tracker.git
   cd budget-tracker
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the App Locally**:
   ```bash
   streamlit run app.py
   ```
   - Open `http://localhost:8501` in your browser.
5. **Usage**:
   - **Home Page**: Enter expenses (e.g., $10.50, Food, 2025-06-30) and submit.
   - **Dashboard Page**: View spending summaries, expense list, AI tips, and the Bolt.new badge.
6. **Deploy to Streamlit Cloud** (optional):
   - Push the repository to GitHub.
   - Sign in to [streamlit.io/cloud](https://streamlit.io/cloud).
   - Create a new app, select the repository, set `app.py` as the main file, and deploy.

## Files
- `app.py`: Main application code (form, dashboard, AI tips, badge).
- `requirements.txt`: Python dependencies (streamlit, pandas).
- `logotext_poweredby_360w.png`: Bolt.new badge image.
- `expenses.db`: SQLite database (generated automatically, not included in repository).

## Notes
- The app was initially built with Bolt.new but switched to Streamlit due to token limits.
- The SQLite database (`expenses.db`) is recreated on deployment, so add test expenses via the app.
- For the hackathon, the "Built with Bolt.new" badge is included on both pages.

## Hackathon Submission
- **Devpost Description**: A web app to help students manage finances with expense tracking, spending summaries, and AI savings tips.
- **Public URL**: Deployed on Streamlit Cloud (or localhost if deployment issues occur).
- **Video**: 3-minute demo showing the Home page (form, badge), Dashboard (summaries, tips, badge), and Bolt.new acknowledgment.

## License
MIT License