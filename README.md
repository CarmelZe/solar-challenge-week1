# Solar Data Challenge - Week 0
**MoonLight Energy Solutions - Solar Farm Analysis**  
*10 Academy Training Program - Data Engineering, Financial Analytics & Machine Learning Engineering*

---

## 🌱 Environment Setup

### Prerequisites
- Python 3.10+ ([Download](https://www.python.org/downloads/))
- Git ([Download](https://git-scm.com/))
- GitHub account
- (Optional) VS Code or PyCharm IDE

### Installation
```bash
# 1. Clone repository
git clone https://github.com/CarmelZe/solar-challenge-week1.git
cd solar-challenge-week1

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

Verify Setup
bash
python --version  # Should show Python 3.10+
pip list  # Should show streamlit, pandas, etc.

📂 Project Structure
solar-challenge-week1/
├── app/                  # Streamlit dashboard
│   ├── main.py           # Dashboard entry point
│   └── utils.py          # Data loading utilities
├── data/                 # Cleaned datasets (.gitignore'd)
├── notebooks/            # Jupyter notebooks for EDA
│   ├── benin_eda.ipynb
│   ├── compare_countries.ipynb
│   └── ...
├── .github/workflows/    # CI/CD pipelines
├── dashboard_screenshots/ # Dashboard previews
├── .gitignore
├── requirements.txt
└── README.md

🚀 Running the Dashboard
bash
streamlit run app/main.py
Features:

Country comparison (Benin/Sierra Leone/Togo)

Interactive metric selection (GHI/DNI/DHI)

Data validation and error handling

Dashboard Preview

📊 Key Findings
Solar Potential Ranking
Benin > Sierra Leone > Togo (by median GHI)

Weather Impact
Sierra Leone shows highest diffuse radiation (DHI) due to cloud cover

Optimal Locations
Benin's northern regions had most consistent irradiance

🔍 Tasks Completed
Task	Description	Files
1	Git & CI Setup	.github/workflows/ci.yml
2	EDA & Cleaning	notebooks/*_eda.ipynb
3	Country Comparison	notebooks/compare_countries.ipynb
Bonus	Streamlit Dashboard	app/main.py
📅 Submission
Requirements:

GitHub repo link

Final report (PDF/Markdown)

Dashboard screenshot

Deadline:
Wednesday, May 21 2025 @ 8:00 PM UTC

⁉️ Support
For issues, please:

Check open issues

Create a new issue if unresolved

Facilitators: Yabebal, Mahlet, Kerod, Rediet, Rehmet


### Key Improvements:
1. **Added visual hierarchy** with clear section headers
2. **Included project structure** for better navigation
3. **Enhanced task documentation** with completion table
4. **Added support section** for troubleshooting
5. **Made deadlines/facilitators** more visible
6. **Optimized for mobile viewing** with concise formatting

To implement:
1. Save this as `README.md`
2. Add your dashboard screenshot to `dashboard_screenshots/`
3. Commit changes:
```bash
git add README.md dashboard_screenshots/
git commit -m "docs: update README with complete project details"
git push origin main
