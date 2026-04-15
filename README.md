🎭 Playwright Automation Framework — Python + POM
An end-to-end test automation framework built with Python, Playwright, and the Page Object Model (POM) design pattern. This project automates real-world user flows on SauceDemo — a standard e-commerce demo site used in QA testing.

🚀 Features

✅ End-to-end test coverage: Login → Add to Cart → Checkout → Logout
✅ Page Object Model (POM) for clean, maintainable, and reusable code
✅ Pytest-based test runner with fixtures and configuration
✅ Chromium browser support via Playwright
✅ Configurable slow motion for visual debugging
✅ Modular project structure — easy to scale and extend


🧪 Test Scenarios Covered
TestDescriptiontest_login.pyValidates successful login with valid credentialstest_add_to_cart.pyAdds a product to cart and verifies cart statetest_logout.pyFull E2E flow: Login → Add to Cart → Checkout → Logout

🗂️ Project Structure
Playwright_with_POM/
│
├── pages/                  # Page Object classes
│   ├── __init__.py
│   ├── login_page.py       # Login page actions & locators
│   ├── add_to_cart.py      # Cart, checkout actions & locators
│   └── logout_page.py      # Logout actions & locators
│
├── Test/                   # Test files
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   └── test_logout.py
│
├── conftest.py             # Pytest fixtures (browser setup)
├── pytest.ini              # Pytest configuration
└── requirements.txt        # Project dependencies

⚙️ Tech Stack
ToolPurposePython 3.14Programming languagePlaywrightBrowser automation libraryPytestTest frameworkPOM Design PatternCode structure & maintainabilityChromiumBrowser engine

🛠️ Setup & Installation
1. Clone the repository
bashgit clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create and activate virtual environment
bashpython -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
3. Install dependencies
bashpip install -r requirements.txt
playwright install

▶️ Running Tests
Run all tests
bashpytest
Run a specific test file
bashpytest Test/test_logout.py
Run with visible browser + slow motion
bashpytest --headed --slowmo 1000

📄 Configuration
pytest.ini controls global settings:
ini[pytest]
addopts = --headed --slowmo 1000
Browser setup is handled in conftest.py using Playwright's fixture hooks.

📌 Application Under Test
SauceDemo — https://www.saucedemo.com
CredentialValueUsernamestandard_userPasswordsecret_sauce

👨‍💻 Author
Akash Jaiswar
Automation Test Engineer
🔗 GitHub • LinkedIn

📚 What I Learned

Implementing Page Object Model for scalable test architecture
Writing Playwright locators using IDs, CSS selectors, and data-test attributes
Debugging TimeoutErrors and TypeError issues in Playwright
Structuring a professional pytest project with fixtures and config files
Managing a project with Git & GitHub
