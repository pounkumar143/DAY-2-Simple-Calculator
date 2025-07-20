AI Math Learning Platform
A modular, user-friendly Streamlit app for collaborative math learning with real-time calculator, AI-powered practice, quizzes, and PDF/Excel export for results tracking.

📂 Project Structure
your-math-app/
├── app.py                  # Main application file
├── requirements.txt        # Python package dependencies
├── .env                    # Secret keys (e.g., GROQ_API_KEY)
├── groq_utils.py           # AI model integration
├── components/
│   ├── __init__.py
│   ├── calculator.py       # Calculator UI and logic
│   └── pdf_report.py       # PDF result/report generator
├── modes/
│   ├── __init__.py
│   ├── practice.py         # Practice mode logic
│   ├── learn.py            # Learn mode (AI explanations)
│   ├── quiz.py             # Quiz challenge
│   └── collaboration.py    # (Optional/teamwork mode)
├── user_pdfs/              # Folder for saved user reports (PDF)
├── admin_data.xlsx         # Master Excel record for admin (auto-managed)
├── DejaVuSans.ttf          # Font for Unicode/Math PDF output
├── DejaVuSans-Bold.ttf     # Bold version, for PDF output
└── README.md               # This file


🚀 Getting Started

1) Install requirements
   pip install -r requirements.txt

2) Set up .env file
    GROQ_API_KEY=your_groq_api_key_here

3) Make sure fonts for PDF export are present

     Download DejaVuSans.ttf and DejaVuSans-Bold.ttf and place them in your project root.

4) Run the app
 streamlit run app.py

💡 Features
Always-on Calculator: Standard & scientific, supports negative numbers and live computation.

Practice Mode: Random math tasks, instant feedback, per-session PDF report with scores and AI step explanations.

Learn Mode: Ask any math question; get a detailed, step-by-step AI explanation in both the app and downloadable PDF.

Quiz Challenge: User-selected number of diverse, AI-generated questions; score and step-by-step solutions; export as PDF.

Collaboration Mode: (Stub/sample) for future real-time/group learning.

Export: Every mode provides a user-facing PDF report (includes all questions, answers, scores/feedback).

Admin Data: All results and answers are automatically logged to admin_data.xlsx (in the project folder, never exposed to users).

PDFs for Admin: All user result PDFs are backed up in user_pdfs/ for your admin use.

🛡️ Security and Privacy
User registration is local and session-based (no external account needed).

Admin-only data (admin_data.xlsx and internal PDF backups) is not accessible to users from UI.

🧩 Extending the App
Add more scientific calculator features in calculator.py.

Expand practice/quiz generation logic or improve scoring with better LLM prompts.

Add user authentication, persistent cloud storage, or analytics as needed.

For real-time collaboration, implement backend with sockets or state sharing.

🗃️ Developer Notes
Modular: Each mode or feature is its own file for easy maintenance.

To deploy, ensure that all required files (including fonts) are present in the app directory.

For robust Unicode and math symbol PDF export, never rename or remove DejaVuSans.ttf or DejaVuSans-Bold.ttf.

📜 License
MIT License (or insert your own license here).

❓ FAQ
Q: Why do I see a PermissionError on admin_data.xlsx?
A: Make sure the file is not open in Excel or another program when using the app.

Q: PDF download fails with a font error.
A: Confirm that both required font files are present in your project root directory.

Q: Can users download their data as Excel?
A: No, PDF export is user-facing; Excel is for admin/teacher tracking only.

🤝 Credits
Powered by Streamlit, NumPy, Pandas, FPDF, and Groq/OpenAI APIs.

Unicode-safe PDF thanks to DejaVu Fonts.

For setup guides, help, and customization tips, see comments in each file or open an issue.
