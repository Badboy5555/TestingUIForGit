from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Input form
    INPUT_FULL_NAME = (By.CSS_SELECTOR, '#userName')
    INPUT_EMAIL = (By.CSS_SELECTOR, '#userEmail')
    INPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    INPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')

    SUBMIT = (By.CSS_SELECTOR, '#submit')

    # Output form
    OUTPUT_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    OUTPUT_EMAIL = (By.CSS_SELECTOR, '#output #email')
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

class RadioButtonPageLocators:
    YES = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    NO = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    IMPRESSIVE = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    TEXT_SUCCESS = (By.CSS_SELECTOR, '.text-success')
