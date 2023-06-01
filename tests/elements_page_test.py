import random
import time

import pytest
from pages.element_page import TextBoxPage, RadioButtonPage, WebrTablesPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            url = 'https://demoqa.com/text-box'
            tbox_page = TextBoxPage(driver, url)
            tbox_page.open()
            input_full_name, input_email, input_current_address, input_permanent_address = tbox_page.fill_input_form()
            output_full_name, output_email, output_current_address, output_permanent_address = tbox_page.get_output_form()

            assert input_full_name == output_full_name, 'There is a missing in a full_name'
            assert input_email == output_email, 'There is a missing in a email'
            assert input_current_address == output_current_address, 'There is a missing in a current_address'
            assert input_permanent_address == output_permanent_address, 'There is a missing in a permanent_address'

    @pytest.mark.usefixtures('radio_button_setup')
    class TestRadioButton:
        @pytest.fixture
        def radio_button_setup(self, driver2):
            url = 'https://demoqa.com/radio-button'
            self.radio_button_page = RadioButtonPage(driver2, url)
            self.radio_button_page.open()

        def test_radio_button_yes(self):
            self.radio_button_page.yes_button_click()
            result_text = self.radio_button_page.get_result_text()
            assert 'Yes' in result_text, 'There is a missing in Yes-radiobutton functon'

        @pytest.mark.xfail(reason='tag "radio" is disabled', run=False)
        def test_radio_button_no(self):
            self.radio_button_page.no_button_click()
            result_text = self.radio_button_page.get_result_text()
            assert 'No' in result_text, 'There is a missing in Yes-radiobutton functon'

        def test_radio_button_impressive(self):
            self.radio_button_page.impressinve_button_click()
            result_text = self.radio_button_page.get_result_text()
            assert 'Impressive' in result_text, 'There is a missing in Yes-radiobutton functon'

    @pytest.mark.usefixtures('web_table_setup')
    class TestWebTables:
        @pytest.fixture
        def web_table_setup(self, driver2):
            url = 'https://demoqa.com/webtables'
            self.web_table_page = WebrTablesPage(driver2, url)
            self.web_table_page.open()

        @pytest.mark.parametrize('how_much', [2])
        def test_web_table_add_persons(self, how_much):
            input_persons = self.web_table_page.create_random_persons(how_much)
            output_persons = self.web_table_page.get_all_persons()

            assert any(item in input_persons for item in output_persons), 'Persons do not found in the table.'

        @pytest.mark.parametrize('query', ['1'])
        def test_web_table_search_two_results(self, query):
            self.web_table_page.search_by_any_key(query)
            search_result = self.web_table_page.get_all_persons()
            assert len(search_result) == 2, 'Search result != 2'

        def test_web_table_search_one_result(self):
            intput_persons = self.web_table_page.create_random_persons(1)
            person_attibute = intput_persons[0][random.randint(0, 5)]

            self.web_table_page.search_by_any_key(person_attibute)
            search_result = self.web_table_page.get_last_person()

            assert person_attibute in search_result, 'Search result does not match of the search query'

        input_list = [[['John', 'Smith', 'some@gmail.com', '64', '54678', 'policeman'],
                       ['Jason', 'Newman', 'qwe@bing.com', '20', '10000', 'student']]]

        @pytest.mark.parametrize('input_list', input_list)
        def test_web_table_search_specified_results(self, input_list):
            intput_persons = self.web_table_page.create_specified_persons(input_list)
            first_letter_of_the_person_name = intput_persons[0][0][0]

            self.web_table_page.search_by_any_key(first_letter_of_the_person_name)
            search_result = self.web_table_page.get_all_persons()

            assert len(search_result) == len(input_list), 'Search result != search query'

        def test_web_table_edit_new_random_person_first_name(self):
            query = 'GGGG'
            self.web_table_page.create_random_persons(1)
            first_name_before_edit = self.web_table_page.get_last_person()[0]

            self.web_table_page.edit_last_person_first_name(query)
            first_name_after_edit = self.web_table_page.get_last_person()[0]

            assert first_name_after_edit == query and \
                   first_name_after_edit != first_name_before_edit \
                , f'New first name != {query}'

        def test_web_table_delete_new_random_person(self):
            self.web_table_page.create_random_persons(1)
            person_before_delete = self.web_table_page.get_last_person()

            self.web_table_page.delete_last_person()
            person_after_delete = self.web_table_page.get_last_person()

            assert person_before_delete != person_after_delete, 'Person was not deleted'

        @pytest.mark.parametrize('rows_amount', ['5', '10', '20', '25', '50', '100'])
        def test_web_table_switch_rows(self, rows_amount):
            number_of_rows = self.web_table_page.switch_rows(rows_amount)

            assert number_of_rows == int(rows_amount)
