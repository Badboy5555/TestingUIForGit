# CI/CD config

This CI/CD pipeline base on Python WebUI autotest. 

Config .gitlab-ci.yml: [link](https://gitlab.com/Badboy5555/TestingUIForGit_POM_Gitlab/-/blob/main/.gitlab-ci.yml)

# TestingUIForGitLab
**POM testing. WebUI example**  

This project implemets for Python WebUI autotest for https://demoqa.com/elements.  A tech stack: Python + Selenium + Pytest + Allure  
For Elements-> Web Tables section were made:
- Check-list: functional and non functional checks (Word-doc) — [link](https://github.com/Badboy5555/TestingUIForGit_POM/blob/main/%D0%A7%D0%B5%D0%BA-%D0%BB%D0%B8%D1%81%D1%82.docx)
- Test cases: base functional was covered (Excel-table) — [link](https://github.com/Badboy5555/TestingUIForGit_POM/blob/main/%D0%A2%D0%B5%D1%81%D1%82-%D0%BA%D0%B5%D0%B9%D1%81%D1%8B.xlsx) 
- Test data: data designed for Add-func testing (csv-file) — [link](https://github.com/Badboy5555/TestingUIForGit_POM/blob/main/data/data_for_web_table_add_person.csv)
- Autotests: main coverage is Elements-> Web Tables + some coverage of Elements section — [link](https://github.com/Badboy5555/TestingUIForGit_POM/blob/main/tests/elements_page_test.py)

 
 # Installation
1. Install Python 3.11
2. Clone the project `git clone https://gitlab.com/Badboy5555/TestingUIForGit_POM_Gitlab.git`
3. Install requirements for project:   
   using CLI, navigate to project directory and run command `pip install -r requirements.txt`
   
# Tests runnig
To run all test, using CLI navigate to project directory and run command: `python -m pytest tests --alluredir=allure-results`

# Report 
To generate testrun report, using CLI, navigate to project directory and run command: `allure serve allure-results`

