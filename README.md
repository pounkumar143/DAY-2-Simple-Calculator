📁 Project Structure
your-math-app/
├── app.py
├── requirements.txt
├── .env
├── groq_utils.py
├── components/
│   ├── __init__.py
│   ├── calculator.py
│   └── pdf_report.py
├── modes/
│   ├── __init__.py
│   ├── practice.py
│   ├── learn.py
│   ├── quiz.py
│   └── collaboration.py
├── user_pdfs/           # (PDFs saved by app, auto)
├── admin_data.xlsx      # (Admin Excel export, auto)
├── DejaVuSans.ttf
├── DejaVuSans-Bold.ttf
└── README.md

README.md

components/: reusable interface pieces, calculator, PDF/report code, etc.

modes/: each "mode" of your app (Practice, Learn, Quiz, Collaboration) as its own file.

user_pdfs/: your app saves every user's results PDF here, named by user and mode.

admin_data.xlsx: centralized admin export file, not user-facing.

groq_utils.py: API wrapper for model calls.

Both DejaVuSans font files are needed for robust PDF Unicode support


# AI Math Learning Web App

A modular, Streamlit-based, AI-powered math learning platform with calculator, quiz, practice, and step-by-step AI solutions. Users get PDF results, admin gets full Excel data.

## Project Structure


your-math-app/
├── app.py # Main entry point for Streamlit app
├── requirements.txt # Python dependencies
├── .env # API keys (never share in public repos!)
├── groq_utils.py # AI model (Groq/OpenAI) integration code
├── components/
│ ├── init.py
│ ├── calculator.py # Calculator UI and logic
│ └── pdf_report.py # PDF result/report generator
├── modes/
│ ├── init.py
│ ├── practice.py # Practice mode Q&A
│ ├── learn.py # Learn mode (AI explanations)
│ ├── quiz.py # Quiz challenge logic
│ └── collaboration.py # Placeholder mode
├── user_pdfs/ # Folder for automatic user PDF backups
├── admin_data.xlsx # Local backup of all user activity/results for admin
├── DejaVuSans.ttf # Unicode-safe font for PDF output
├── DejaVuSans-Bold.ttf # Bold font for PDF output
└── README.md


## Install and Run

1. **Clone and install requirements:**

pip install -r requirements.txt


2. **Place your `.env` file with a valid `GROQ_API_KEY`.**

3. **Download `DejaVuSans.ttf` and `DejaVuSans-Bold.ttf`**  
Place them in the project root (required for PDF Unicode/math-safe output).

4. **Start the app:**
streamlit run app.py


5. **Usage:**
- Register a username on first launch.
- Use the sidebar to pick a mode (Practice, Learn, Quiz Challenge, Collaboration).
- Use the always-available calculator.
- At the end of each mode, download your results as PDF.
- All user results are also saved to `user_pdfs/` for admin.
- All user activity and answers are backed up to `admin_data.xlsx` for admin use.

## Features

- **Calculator:** Standard/scientific input, always on dashboard
- **Practice Mode:** Timed or batch Q&A with instant feedback and scoring
- **Learn Mode:** User asks any math question; AI gives step-by-step help
- **Quiz Challenge:** Random AI-generated quiz of user-selected size and difficulty
- **PDF Results:** Every task/mode lets users download a clean PDF report (includes all Qs and As, feedback, scores, and AI explanations)
- **Admin Data:** All user data automatically tracked (not user-downloadable), available as Excel
- **Unicode-Safe:** Handles math symbols, international text in PDFs

## Developer Notes

- Modular files: Add new modes in `modes/`, new components (like analytics or exports) in `components/`.
- All PDFs and admin Excel files are saved server-side; users cannot see admin Excel download.
- For Unicode/math-export issues: ensure both DejaVu font files are present in the root.

## License

MIT License (or specify your license)



