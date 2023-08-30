from selenium.webdriver.common.by import By


class TextBoxesPageLocators:
    # Input form
    INPUT_FULL_NAME = (By.CSS_SELECTOR, '#userName')
    INPUT_EMAIL = (By.CSS_SELECTOR, '#userEmail')
    INPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    INPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')

    SUBMIT_BUTT = (By.CSS_SELECTOR, '#submit')

    # Output form
    OUTPUT_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    OUTPUT_EMAIL = (By.CSS_SELECTOR, '#output #email')
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class RadioButtonsPageLocators:
    YES = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    NO = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    IMPRESSIVE = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    TEXT_SUCCESS = (By.CSS_SELECTOR, '.text-success')


class WebTablesPageLocators:
    # Add
    ADD_BUTT = (By.CSS_SELECTOR, '#addNewRecordButton')

    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    AGE = (By.CSS_SELECTOR, '#age')
    SALARY = (By.CSS_SELECTOR, '#salary')
    DEPARTMENT = (By.CSS_SELECTOR, '#department')
    SUBMIT_BUTT = (By.CSS_SELECTOR, '#submit')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#registration-form-modal')

    # Result table
    # Magic time =)
    PERSONS = (By.XPATH, '//div[starts-with(@class, "rt-tr -") and not(starts-with(@class, "rt-tr -padRow"))]')
    ALL_DATA_OF_CURRENT_PERSON = (By.CSS_SELECTOR, '[role="gridcell"]')

    # Search
    SEARCH_INPUT = (By.CSS_SELECTOR, '#searchBox')

    # Edit
    EDIT_BUTT = (By.CSS_SELECTOR, 'span[title="Edit"]')
    DELETE_BUTT = (By.CSS_SELECTOR, 'span[title="Delete"]')

    # Pagination rows
    ROWS_ON_PAGE = (By.CSS_SELECTOR, 'div[role="rowgroup"]')
    ROWS_SELECTOR = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')


class ClickButtonsPageLocators:
    # ClickButtons
    DOUBLE_CLICK_BUTT = (By.CSS_SELECTOR, '#doubleClickBtn')
    RIGHT_CLICK_BUTT = (By.CSS_SELECTOR, '#rightClickBtn')
    SINGLE_CLICK_BUTT = (By.CSS_SELECTOR, 'div[class="mt-4"]:nth-child(3)>button')

    # ClickButtons messages
    DOUBLE_CLICK_MESS = (By.CSS_SELECTOR, '#doubleClickMessage')
    RIGHT_CLICK_MESS = (By.CSS_SELECTOR, '#rightClickMessage')
    SINGLE_CLICK_MESS = (By.CSS_SELECTOR, '#dynamicClickMessage')


class LinksPageLocators:
    #New tab liks
    SIMPLE_LINK = (By.CSS_SELECTOR, '#simpleLink')
    DYNAMIC_LINK = (By.CSS_SELECTOR, '#dynamicLink')

    # API call links
    API_CREATED_LINK = (By.CSS_SELECTOR, '#created')
    API_MOVED_LINK = (By.CSS_SELECTOR, '#moved')
    API_UNAUTHORIZED_LINK = (By.CSS_SELECTOR, '#unauthorized')


class UploadDownloadPageLocators:
    UPLOAD_BUTT = (By.CSS_SELECTOR, '#uploadFile')
    UPLOAD_FILE_PATH = (By.CSS_SELECTOR, '#uploadedFilePath')
    DOWNLOAD_BUTT = (By.CSS_SELECTOR, '#downloadButton')


class DynamicPropertiesPageLocators:
    WILL_ENABLE = (By.CSS_SELECTOR, '#enableAfter')
    CHANGE_COLOR = (By.CSS_SELECTOR, '#colorChange')
    VISIBLE_AFTER = (By.CSS_SELECTOR, '#visibleAfter')

