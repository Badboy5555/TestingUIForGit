import base64
import filecmp
import random
import time

import allure
import requests

from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from locators.Locators import TextBoxesPageLocators, RadioButtonsPageLocators, WebTablesPageLocators, \
    ClickButtonsPageLocators, LinksPageLocators, UploadDownloadPageLocators, DynamicPropertiesPageLocators
from generator.generator import generate_data


class TextBoxesPage(BasePage):
    locators = TextBoxesPageLocators()

    @allure.step('Fill input form')
    def fill_input_form(self):
        person_data = next(generate_data())

        input_full_name = person_data.FULL_NAME
        input_email = person_data.EMAIL
        input_current_address = person_data.CURRENT_ADDRESS.replace('\n', ' ')
        input_permanent_address = person_data.PERMANENT_ADDRESS.replace('\n', ' ')

        self.element_is_visible(self.locators.INPUT_FULL_NAME).send_keys(input_full_name)
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(input_email)
        self.element_is_visible(self.locators.INPUT_CURRENT_ADDRESS).send_keys(input_current_address)
        self.element_is_visible(self.locators.INPUT_PERMANENT_ADDRESS).send_keys(input_permanent_address)

        submit = self.element_is_clicable(self.locators.SUBMIT_BUTT)
        self.go_to_element(submit)
        submit.click()
        return input_full_name, input_email, input_current_address, input_permanent_address

    @allure.step('Get output form')
    def get_output_form(self):
        output_full_name = self.element_is_present(self.locators.OUTPUT_FULL_NAME).text.split(':')[-1]
        output_email = self.element_is_present(self.locators.OUTPUT_EMAIL).text.split(':')[-1]
        output_current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[-1]
        output_current_address.replace('\n', ' ')
        output_permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[-1]
        output_permanent_address.replace('\n', ' ')
        return output_full_name, output_email, output_current_address, output_permanent_address


class RadioButtonsPage(BasePage):
    locators = RadioButtonsPageLocators()

    @allure.step('Click Yes-button')
    def yes_button_click(self):
        self.element_is_present(self.locators.YES).click()

    @allure.step('Click No-button')
    def no_button_click(self):
        self.element_is_clicable(self.locators.NO).click()

    @allure.step('Click Impressive-button')
    def impressive_button_click(self):
        self.element_is_clicable(self.locators.IMPRESSIVE).click()

    @allure.step('Get result text')
    def get_result_text(self):
        result_text = self.element_is_present(self.locators.TEXT_SUCCESS).text
        return result_text


class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    @allure.step('Get form status')
    def get_form_status_is_closed(self):
        """ Get status of if 'Registration Form' is closed """
        try:
            self.element_is_not_visible(self.locators.REGISTRATION_FORM)
            return 1
        except TimeoutException:
            return 0

    @allure.step('Get rows count and query mapping')
    def get_search_specified_results(self, query):
        """ Get rows count and query mapping"""
        search_result = self.get_all_persons()

        result_count = len(search_result)
        result_mapping = all([query in i for i in search_result])

        return result_count, result_mapping

    @allure.step('Get rows count')
    def get_search_special_symbols(self):
        """ Check rows count """
        search_result = self.get_all_persons()
        result_count = len(search_result)

        return result_count

    @allure.step('Create random valid user')
    def create_random_valid_persons(self, how_much=2) -> list[list[str]]:
        """ Create 'how_much' number of random persons,
            returns [[...], [...]] of created persons"""
        persons_list = []
        while how_much != 0:
            with allure.step('"Add" click'):
                self.element_is_clicable(self.locators.ADD_BUTT).click()
            with allure.step('Generate data and fill the form'):
                person_data = next(generate_data())

            input_first_name = person_data.FIRST_NAME
            input_last_name = person_data.LAST_NAME
            input_email = person_data.EMAIL
            input_age = person_data.AGE
            input_salary = person_data.SALARY
            input_department = person_data.DEPARTMENT

            self.element_is_visible(self.locators.FIRST_NAME).send_keys(input_first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(input_last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(input_email)
            self.element_is_visible(self.locators.AGE).send_keys(input_age)
            self.element_is_visible(self.locators.SALARY).send_keys(input_salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(input_department)
            
            with allure.step('"Submit" click'):
                submit = self.element_is_clicable(self.locators.SUBMIT_BUTT)
            self.go_to_element(submit)
            submit.click()
            persons_list.append(
                [input_first_name, input_last_name, str(input_age), input_email, str(input_salary), input_department])
            how_much -= 1
        return persons_list

    @allure.step('Create specified person')
    def create_specified_person(self, input_list: list[str]) -> tuple[str, ...]:
        """ Create one specified person """
        with allure.step('"Add" click'):
            self.element_is_clicable(self.locators.ADD_BUTT).click()

        with allure.step('Fill the form'):
            input_first_name, input_last_name, input_email, input_age, input_salary, input_department = input_list
    
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(input_first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(input_last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(input_email)
            self.element_is_visible(self.locators.AGE).send_keys(input_age)
            self.element_is_visible(self.locators.SALARY).send_keys(input_salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(input_department)
        with allure.step('"Submit" click'):
            submit = self.element_is_clicable(self.locators.SUBMIT_BUTT)
            self.go_to_element(submit)
            submit.click()
        return input_first_name, input_last_name, str(input_age), input_email, str(input_salary), input_department

    @allure.step('Get last person')
    def get_last_person(self) -> tuple[str, ...]:
        """ Get the last person from the list """
        last_person_row = self.elements_are_present(self.locators.PERSONS)[-1]
        all_data_of_current_person = last_person_row.find_elements(*self.locators.ALL_DATA_OF_CURRENT_PERSON)[:-1]
        output_first_name, output_last_name, output_age, output_email, output_salary, output_department = \
            [i.text for i in all_data_of_current_person]
        return output_first_name, output_last_name, output_age, output_email, output_salary, output_department

    @allure.step('Get specified person')
    def get_specified_person(self, person_name) -> tuple[list[str], object] | str:
        """ Get specified person's WebDriver class objects and his data """
        persons = self.elements_are_present(self.locators.PERSONS)

        for person in persons:
            all_data_of_current_person_obj = person.find_elements(*self.locators.ALL_DATA_OF_CURRENT_PERSON)
            output_first_name, output_last_name, output_age, output_email, output_salary, output_department, action = \
                all_data_of_current_person = [i.text for i in all_data_of_current_person_obj]
            if person_name in all_data_of_current_person:
                return all_data_of_current_person, all_data_of_current_person_obj
        return f"Specified name {person_name} doesn't exist."

    @allure.step('Get all persons')
    def get_all_persons(self) -> list[list[str]] | list:
        """Get all persons from the list"""
        try:
            all_persons = self.elements_are_present(self.locators.PERSONS)
        except TimeoutException:
            return []
        output_persons = [[i.text for i in person.find_elements(*self.locators.ALL_DATA_OF_CURRENT_PERSON)[:-1]]
                          for person in all_persons]
        return output_persons

    @allure.step('Fill search field by {query}')
    def search_by_any_key(self, query=2):
        """ Makes query search"""
        self.element_is_clicable(self.locators.SEARCH_INPUT).send_keys(query)

    @allure.step("Edit last person first_name={query}")
    def edit_last_person_first_name(self, query):
        """ Edit last person's first name """
        with allure.step('Get person data'):
            last_person_row = self.elements_are_present(self.locators.PERSONS)[-1]
        with allure.step('Click edit-button'):
            last_person_row.find_element(*self.locators.EDIT_BUTT).click()
        first_name_field = self.element_is_visible(self.locators.FIRST_NAME)
        with allure.step('Edit field First_name'):
            first_name_field.clear()
            first_name_field.send_keys(str(query))
            self.element_is_clicable(self.locators.SUBMIT_BUTT).click()

    @allure.step("Edit person's first_name={old_first_name} to {new_first_name}")
    def edit_specified_person_first_name(self, old_first_name, new_first_name):
        """ Edit specified person's first name """
        with allure.step('Get person data'):
            person_obj_action = self.get_specified_person(old_first_name)[1][-1]
        with allure.step('Click edit-button'):
            person_obj_action.find_element(*self.locators.EDIT_BUTT).click()
        with allure.step('Edit field First_name'):
            first_name_field = self.element_is_visible(self.locators.FIRST_NAME)
            first_name_field.clear()
            first_name_field.send_keys(new_first_name)
        self.element_is_clicable(self.locators.SUBMIT_BUTT).click()

    @allure.step('Delete last person')
    def delete_last_person(self):
        """ Delete last person from the list"""
        with allure.step('Get person data'):
            last_person_row = self.elements_are_present(self.locators.PERSONS)[-1]
        with allure.step('Click delete-button'):
            last_person_row.find_element(*self.locators.DELETE_BUTT).click()

    @allure.step('Delete person by first_name={first_name}')
    def delete_specified_person_by_first_name(self, first_name) -> list[str]:
        """ Delete specified person from the list by first name """
        with allure.step('Get person data'):
            person_data, person_obj = self.get_specified_person(first_name)
        with allure.step('Click delete-button'):
            person_obj[-1].find_element(*self.locators.DELETE_BUTT).click()
        return person_data

    @allure.step('Switch rows amount to {rows_amount}')
    def switch_rows(self, rows_amount):
        """ Count number of rows in list """
        elem = self.element_is_clicable(self.locators.ROWS_SELECTOR)
        self.go_to_element(elem)
        select_rows = Select(elem)
        select_rows.select_by_value(rows_amount)
        number_of_rows = len(self.elements_are_present(self.locators.ROWS_ON_PAGE))
        return number_of_rows


class ClickButtonsPage(BasePage):
    locators = ClickButtonsPageLocators()

    @allure.step('Click double-click button')
    def click_double_click_butt(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTT))
    
    @allure.step('Click right-click buttin')
    def click_right_click_butt(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTT))
    
    @allure.step('Click single-click buttin')
    def click_single_click_butt(self):
        self.element_is_visible(self.locators.SINGLE_CLICK_BUTT).click()

    @allure.step('Get result message {butt}')
    def get_click_result(self, butt):
        match butt:
            case 'double':
                butt = self.locators.DOUBLE_CLICK_MESS
            case 'right':
                butt = self.locators.RIGHT_CLICK_MESS
            case 'single':
                butt = self.locators.SINGLE_CLICK_MESS
        return self.element_is_visible(butt).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step('Click the link')
    def click_simple_link(self):
        self.element_is_visible(self.locators.SIMPLE_LINK).click()

    @allure.step('Get tab url')
    def get_tab_url(self):
        return self.driver.current_url

    @allure.step('Click API link {api_link}')
    def click_api_link(self, api_link):
        match api_link:
            case 'Created':
                self.element_is_visible(self.locators.API_CREATED_LINK).click()
            case 'Moved':
                self.element_is_visible(self.locators.API_MOVED_LINK).click()
            case 'Unauthorized':
                self.element_is_visible(self.locators.API_UNAUTHORIZED_LINK).click()

    @allure.step('Get status and message code')
    def get_satus_mess_and_code(self, api_link):
        """ Get status code and message code from response """
        res = requests.get(f'https://demoqa.com/{api_link}')
        status_mess = res.reason
        status_code = res.status_code
        return str(status_code), status_mess


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators()

    @allure.step('Upload')
    def upload_file(self, file_path):
        self.element_is_present(self.locators.UPLOAD_BUTT).send_keys(file_path)

    @allure.step('Get filename')    
    def get_file_name(self):
        return self.element_is_visible(self.locators.UPLOAD_FILE_PATH).text.split('\\')[-1]

    @allure.step('Download')
    def download_file(self):
        """ Decode download link from base64 and download the file  """
        with allure.step('Get download link and decode it from base64'):
            link = self.element_is_present(self.locators.DOWNLOAD_BUTT).get_attribute('href').split(',')[-1]
            file = base64.b64decode(link)
        with allure.step('Download the file'):
            server_file = rf'F:\a{random.randint(1, 99)}b.jpeg'
            with open(server_file, 'wb+') as F:
                F.write(file)
        return server_file

    @allure.step("Check files equality")
    def check_files_equality(self, local_file, server_file):
        """Use filecmp to check if files are equal. Utility's shallow=True mode check files inside."""
        return filecmp.cmp(local_file, server_file, shallow=True)


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step("Button is enable after 5 seconds delay")
    def check_will_enable(self):
        """ Check button after 5 seconds delay """
        try:
            self.element_is_clicable(self.locators.WILL_ENABLE, 6)
            return 1
        except TimeoutException:
            return 0

    @allure.step("Get button's colors before/after 5 seconds delay")
    def get_colors(self):
        """ Get button's property 'color' after 5 seconds delay """
        color_before = self.element_is_present(self.locators.CHANGE_COLOR).value_of_css_property('color')
        time.sleep(6)
        color_after = self.element_is_present(self.locators.CHANGE_COLOR).value_of_css_property('color')
        return color_before, color_after

    @allure.step("Button is visible after 5 seconds delay")
    def check_visible_after(self):
        """ Check button's visibility after 5 seconds delay """
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER, 6)
            return 1
        except TimeoutException:
            return 0
