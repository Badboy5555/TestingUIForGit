import random
import time


import pytest
from pages.element_page import TextBoxPage, RadioButtonPage, WebTablesPage, ClickButtonsPage, LinksPage, \
    UploadDownloadPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            url = 'https://demoqa.com/text-box'
            tbox_page = TextBoxPage(driver, url)
            tbox_page.open()
            input_full_name, input_email, input_current_address, input_permanent_address = tbox_page.fill_input_form()
            output_full_name, output_email, output_current_address, output_permanent_address = \
                tbox_page.get_output_form()

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
            self.web_table_page = WebTablesPage(driver2, url)
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
                   first_name_after_edit != first_name_before_edit, f'New first name != {query}'

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

    @pytest.mark.usefixtures('click_buttons_page_setup')
    class TestClickButtons:
        @pytest.fixture
        def click_buttons_page_setup(self, driver2):
            url = 'https://demoqa.com/buttons'
            self.click_buttons_page = ClickButtonsPage(driver2, url)
            self.click_buttons_page.open()

        def test_click_buttons_page_double_click(self):
            self.click_buttons_page.click_double_click_butt()
            result_mess = self.click_buttons_page.get_click_result('double')

            assert 'You have done a double click' == result_mess, 'Button double_click wasn\'t clicked.'

        def test_click_buttons_page_right_click(self):
            self.click_buttons_page.click_right_click_butt()
            result_mess = self.click_buttons_page.get_click_result('right')

            assert 'You have done a right click' == result_mess, 'Button right_click wasn\'t clicked.'

        def test_click_buttons_page_single_click(self):
            self.click_buttons_page.click_single_click_butt()
            result_mess = self.click_buttons_page.get_click_result('single')

            assert 'You have done a dynamic click' == result_mess, 'Button single_click wasn\'t clicked.'

    @pytest.mark.usefixtures('test_links_page_setup')
    class TestLinks:
        @pytest.fixture
        def test_links_page_setup(self, driver2):
            url = 'https://demoqa.com/links'
            self.test_links_page = LinksPage(driver2, url)
            self.test_links_page.open()

        def test_open_new_tab(self):
            current_url = self.test_links_page.get_tab_url()
            self.test_links_page.click_simple_link()
            new_tab_url = self.test_links_page.get_tab_url()

            assert current_url == new_tab_url, 'New tab has different url.'

        @pytest.mark.parametrize('api_link', ['Created', 'Moved', 'Unauthorized'])
        def test_satus_mess_and_code(self, api_link):
            self.test_links_page.click_api_link(api_link)
            status_code, status_mess = self.test_links_page.get_satus_mess_and_code(api_link)

            match api_link:
                case 'Created':
                    assert status_code in 'Link has responded with staus 201 and status text Created' and \
                           status_mess in 'Link has responded with staus 201 and status text Created', \
                           'Wrong status message or status code'
                case 'Moved':
                    assert status_code in 'Link has responded with staus 301 and status text Moved Permanently' and \
                           status_mess in 'Link has responded with staus 301 and status text Moved Permanently', \
                           'Wrong status message or status code'
                case 'Unauthorized':
                    assert status_code in 'Link has responded with staus 401 and status text Unauthorized' and \
                           status_mess in 'Link has responded with staus 401 and status text Unauthorized', \
                           'Wrong status message or status code'

    @pytest.mark.usefixtures('test_upload_download_page_setup')
    class TestUploadDownload:
        @pytest.fixture
        def test_upload_download_page_setup(self, driver2):
            url = 'https://demoqa.com/upload-download'
            self.upload_download_page = UploadDownloadPage(driver2, url)
            self.upload_download_page.open()

        @pytest.mark.parametrize('file_path', [r'C:\sdi.cfg'])
        def test_upload_file(self, file_path):
            self.upload_download_page.upload_file(file_path)
            local_file_name = file_path.split('\\')[-1]
            server_file_name = self.upload_download_page.get_file_name()

            assert local_file_name == server_file_name, 'Filenames are not equal'

        def test_download_file(self):
            server_file = self.upload_download_page.download_file()
            assert self.upload_download_page.check_files_equals(r'F:\sampleFile.jpeg', server_file),\
            'Filenames are not equal'
