### 🚧  Project Status: In Progress 🚧
- This project is still a work in progress. Contributions, issues, and feedback are welcome!
  
# 💻 QA Automation for E-Commerce App
This is a comprehensive QA project for a sample e-commerce site, built using the Page Object Model (POM) design pattern. It covers both **manual and automated testing** using Python, Selenium WebDriver, and PyTest.

🔍 This project demonstrates real-world QA engineering practices including:
- Test case design and implementation
- Automated regression checks
- Test framework setup
- Git-based version control
- Structured test reports



## 🧪 Features Covered
✅ Login Page  <br>
✅ Product Page (including product detail view)<br>
✅ Cart (Planned) <br>
✅ Contact Form (Structure created, test cases in progress)<br>
🧪 More pages to be added as the suite grows<br>


## 🧱 Project Structure
<pre> <code> 📁qa-ecommerce-automation/
│
├── config/ # Test data & configuration
├── pages/ # POM classes (Login, Product, Contact)
├── tests/ # Pytest test files
├── reports/ # HTML test reports
├── docs/ # Test plan/docs
├── conftest.py # Test setup & fixtures
├── requirements.txt
└── pytest.ini </code> </pre>

## 🛠 Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium)
![PyTest](https://img.shields.io/badge/PyTest-3776AB?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions)



## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/melatemarkos/qa-ecommerce-automation.git
cd qa-ecommerce-automation

# Set up environment
pip install -r requirements.txt

# Run tests and generate report
pytest --html=reports/report.html
