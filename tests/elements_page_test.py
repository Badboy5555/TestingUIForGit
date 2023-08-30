import random
import allure

import pytest
from pages.element_page import TextBoxesPage, RadioButtonsPage, WebTablesPage, ClickButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:
    @allure.sub_suite('Tex Box')
    @allure.feature('Text Box page has a registration form fields and output fields')
    class TestTextBoxes:
        @allure.story('Check fields filling')
        def test_text_box(self, driver, screenshot_on_failure):
            """ Check fields filling """
            url = 'https://demoqa.com/text-box'
            tbox_page = TextBoxesPage(driver, url)
            tbox_page.open()
            input_full_name, input_email, input_current_address, input_permanent_address = tbox_page.fill_input_form()
            output_full_name, output_email, output_current_address, output_permanent_address = \
                tbox_page.get_output_form()
            with allure.step('Check fields for equality'):
                assert input_full_name == output_full_name, 'There is a missing in a full_name'
                assert input_email == output_email, 'There is a missing in a email'
                assert input_current_address == output_current_address, 'There is a missing in a current_address'
                assert input_permanent_address == output_permanent_address, 'There is a missing in a permanent_address'

    @allure.sub_suite('Radio Button')
    @allure.feature('Radio Button page has a feedback question with 3 variants of answers')
    @pytest.mark.usefixtures('radio_button_setup')
    class TestRadioButtons:
        @pytest.fixture
        def radio_button_setup(self, driver, screenshot_on_failure):
            """ Creates a RadioButtonsPage object and open its url """
            with allure.step('Setup RadioButtonsPage object and open its url'):
                url = 'https://demoqa.com/radio-button'
                self.radio_button_page = RadioButtonsPage(driver, url)
                self.radio_button_page.open()

        @allure.story('Check radio button "Yes"')
        def test_radio_button_yes(self):
            """ Check if it's possible to select button 'Yes'"""
            self.radio_button_page.yes_button_click()
            result_text = self.radio_button_page.get_result_text()
            with allure.step('Check result text'):
                assert 'Yes' in result_text, 'There is a missing in Yes-radiobutton functon'

        @allure.story('Check radio button "No"')
        @pytest.mark.xfail(reason='tag "radio" is disabled', run=False)
        def test_radio_button_no(self):
            """ Check if it's possible to select button 'No'"""
            self.radio_button_page.no_button_click()
            result_text = self.radio_button_page.get_result_text()
            with allure.step('Check result text'):
                assert 'No' in result_text, 'There is a missing in No-radiobutton functon'

        @allure.story('Check radio button "impressive"')
        def test_radio_button_impressive(self):
            """ Check if it's possible to select button 'No'"""
            self.radio_button_page.impressive_button_click()
            result_text = self.radio_button_page.get_result_text()
            with allure.step('Check result text'):
                assert 'Impressive' in result_text, 'There is a missing in Impressive-radiobutton functon'

    @allure.sub_suite('Web Tables')
    @allure.feature("Web Tables page has a person's data list and functions add/edit/delete for it")
    @pytest.mark.usefixtures('web_table_setup')
    class TestWebTables:
        @pytest.fixture
        def web_table_setup(self, driver, screenshot_on_failure):
            """ Creates a WabTablePage object and open its url """
            with allure.step('Setup WebTablesPage object and open its url'):
                url = 'https://demoqa.com/webtables'
                self.web_table_page = WebTablesPage(driver, url)
                self.web_table_page.open()

        # parametrized by pytest_generate_tests hook

        def test_web_table_add_person(self, input_data):
            """ Check if one new person could be added in the list """
            expected_person = self.web_table_page.create_specified_person(input_data)

            with allure.step('Check if form is closed'):
                assert self.web_table_page.get_form_status_is_closed() == 1, \
                    'Registration Form is not closed after submitting!'

            actual_person = self.web_table_page.get_last_person()

            with allure.step('Check data equality'):
                assert actual_person == expected_person, 'New person is not equal to the old person.'

        @pytest.mark.parametrize('how_much', [2])
        def test_web_table_add_random_valid_persons(self, how_much):
            """ Check if 'how_much' new random persons could be added in the list """
            input_persons = self.web_table_page.create_random_valid_persons(how_much)
            output_persons = self.web_table_page.get_all_persons()

            with allure.step('Check if persons in the list'):
                assert all(item in input_persons for item in output_persons), 'Persons are not in the list.'

        def test_web_table_search_one_random_result(self):
            """ Check if search result matches to the random query """
            intput_persons = self.web_table_page.create_random_valid_persons(1)
            person_attribute = intput_persons[0][random.randint(0, 5)]

            self.web_table_page.search_by_any_key(person_attribute)
            search_result = self.web_table_page.get_last_person()

            with allure.step('Check search result'):
                assert person_attribute in search_result, 'Search result does not match of the search query'

        specified_search_list = [('Cierra', 1), ('Vega', 1), ('cierra@example.com', 1), ('39', 1), ('10000', 1),
                                 ('Insurance', 1),
                                 ('Cier', 2), ('Ve', 2), ('cierra@exam', 2), ('20', 2), ('1000', 2), ('Insur', 1),
                                 ('rr', 3), ('nt', 3), ('a@', 3), ('9', 3), ('2000', 3), ('ce', 3)]

        @pytest.mark.parametrize('query,query_count', specified_search_list)
        def test_web_table_search_specified_results(self, query, query_count):
            """ Check if search result matches to the query """
            self.web_table_page.search_by_any_key(query)
            result_count, result_mapping = self.web_table_page.get_search_specified_results(query)

            with allure.step('Check search result'):
                assert query_count == result_count, f'Query search count {query_count} is not equal to result search count {result_count}'
                assert result_mapping == 1, f"Search result {result_count} does't match to the search query {query}"

        special_symbols_search_list = [(r'/\w/', 3), (r'/*/', 3)]

        @pytest.mark.parametrize('query,query_count', special_symbols_search_list)
        def test_web_table_search_special_symbols(self, query, query_count):
            """ Check if search result matches to the query """
            self.web_table_page.search_by_any_key(query)
            result_count = self.web_table_page.get_search_special_symbols()

            with allure.step('Check search result'):
                assert query_count == result_count, \
                    f'Query search count {query_count} is not equal to result search count {result_count}'

        def test_web_table_edit_new_random_person_first_name(self):
            """ Check if first name of a new random person could be edited """
            query = 'GGGG'
            self.web_table_page.create_random_valid_persons(1)
            first_name_before_edit = self.web_table_page.get_last_person()[0]

            self.web_table_page.edit_last_person_first_name(query)
            first_name_after_edit = self.web_table_page.get_last_person()[0]

            assert first_name_after_edit == query and \
                   first_name_after_edit != first_name_before_edit, f'New first name != {query}'

        @pytest.mark.parametrize('old_first_name,new_first_name',
                                [('Alden', 'AAlden'), ('Cierra', 'Cierr'), ('Kierra', 'KierrA')])
        def test_web_table_edit_person_first_name(self, old_first_name, new_first_name):
            """ Check if first_name could be edited """
            self.web_table_page.edit_specified_person_first_name(old_first_name, new_first_name)

            with allure.step('Check if form is closed'):
                assert self.web_table_page.get_form_status_is_closed() == 1, \
                    'Registration Form is not closed after submitting!'

            edited_name = self.web_table_page.get_specified_person(new_first_name)[0][0]
            with allure.step('Check first name'):
                assert new_first_name == edited_name, \
                    f"The {new_first_name} not in the list after {old_first_name} was changed!"

        def test_web_table_delete_new_random_person(self):
            """ Check if a new random person could be deleted """
            self.web_table_page.create_random_valid_persons(1)
            person_before_delete = self.web_table_page.get_last_person()

            self.web_table_page.delete_last_person()
            person_after_delete = self.web_table_page.get_last_person()

            with allure.step('Check the list'):
                assert person_before_delete != person_after_delete, 'The person has not been deleted!'

        @pytest.mark.parametrize('first_name', ['Cierra', 'Kierra', 'Alden'])
        def test_web_table_delete_specified_person_by_first_name(self, first_name):
            """ Check if a person could be deleted """
            self.web_table_page.delete_specified_person_by_first_name(first_name)
            actual_data = self.web_table_page.get_specified_person(first_name)

            with allure.step('Check the list'):
                assert f"Specified name {first_name} doesn't exist." == actual_data, \
                    f"The person {first_name}' has not been deleted!"

        @pytest.mark.parametrize('rows_amount', ['5', '10', '20', '25', '50', '100'])
        def test_web_table_switch_rows(self, rows_amount):
            """ Check if page switches to the selected rows number """
            number_of_rows = self.web_table_page.switch_rows(rows_amount)

            with allure.step('Check rows amount'):
                assert number_of_rows == int(rows_amount),\
                    'The number of rows has not been changed or changed incorrectly'

    @allure.sub_suite('ClickButtons')
    @allure.feature("ClickButtons page has 3 buttons for interact in the different ways")
    @pytest.mark.usefixtures('click_buttons_page_setup')
    class TestClickButtons:
        @pytest.fixture
        def click_buttons_page_setup(self, driver, screenshot_on_failure):
            """ Creates a ClickButtonsPage object and open its url """
            with allure.step('Setup ClickButtonsPage object and open its url'):
                url = 'https://demoqa.com/buttons'
                self.click_buttons_page = ClickButtonsPage(driver, url)
                self.click_buttons_page.open()

        def test_click_buttons_page_double_click(self):
            """ Check if it's possible to double-click button """
            self.click_buttons_page.click_double_click_butt()
            result_mess = self.click_buttons_page.get_click_result('double')

            with allure.step('Check double-click button'):
                assert 'You have done a double click' == result_mess, "Button double_click wasn't clicked."

        def test_click_buttons_page_right_click(self):
            """ Check if it's possible to right-click button """
            self.click_buttons_page.click_right_click_butt()
            result_mess = self.click_buttons_page.get_click_result('right')

            with allure.step('Check right-click button'):
                assert 'You have done a right click' == result_mess, "Button right_click wasn't clicked."

        def test_click_buttons_page_single_click(self):
            """ Check if it's possible to single-click button """
            self.click_buttons_page.click_single_click_butt()
            result_mess = self.click_buttons_page.get_click_result('single')

            with allure.step('Check single-click button'):
                assert 'You have done a dynamic click' == result_mess, "Button single_click wasn't clicked."

    @allure.sub_suite('Links')
    @allure.feature("Links page has many links for interact in the different ways")
    @pytest.mark.usefixtures('test_links_page_setup')
    class TestLinks:
        @pytest.fixture
        def test_links_page_setup(self, driver, screenshot_on_failure):
            """ Creates a LinksPage object and open its url """
            with allure.step('Setup LinksPage object and open its url'):
                url = 'https://demoqa.com/links'
                self.test_links_page = LinksPage(driver, url)
                self.test_links_page.open()

        def test_open_new_tab(self):
            """ Check if new page opens in the new tab """
            current_url = self.test_links_page.get_tab_url()
            self.test_links_page.click_simple_link()
            new_tab_url = self.test_links_page.get_tab_url()

            with allure.step('Check new tab is opened'):
                assert current_url == new_tab_url, 'New tab has different url'

        @pytest.mark.parametrize('api_link', ['Created', 'Moved', 'Unauthorized'])
        def test_satus_mess_and_code(self, api_link):
            """ Check if status codes and messages are correct """
            self.test_links_page.click_api_link(api_link)
            status_code, status_mess = self.test_links_page.get_satus_mess_and_code(api_link)

            with allure.step('Check API link status_code and message_code'):
                match api_link:
                    case 'Created':
                        assert status_code in 'Link has responded with status 201 and status text Created' and \
                               status_mess in 'Link has responded with status 201 and status text Created', \
                            'Wrong status message or status code'
                    case 'Moved':
                        assert status_code in 'Link has responded with status 301 and status text Moved Permanently' and \
                               status_mess in 'Link has responded with status 301 and status text Moved Permanently', \
                            'Wrong status message or status code'
                    case 'Unauthorized':
                        assert status_code in 'Link has responded with status 401 and status text Unauthorized' and \
                               status_mess in 'Link has responded with status 401 and status text Unauthorized', \
                            'Wrong status message or status code'

    @allure.sub_suite('Upload and Download')
    @allure.feature("Upload and Download page has buttons for moving a file")
    @pytest.mark.usefixtures('test_upload_download_page_setup')
    class TestUploadDownload:
        @pytest.fixture
        def test_upload_download_page_setup(self, driver, screenshot_on_failure):
            """ Creates a UploadDownloadPage object and open its url """
            with allure.step('Setup UploadDownload object and open its url'):
                url = 'https://demoqa.com/upload-download'
                self.upload_download_page = UploadDownloadPage(driver, url)
                self.upload_download_page.open()

        @pytest.mark.parametrize('file_path', [r'C:\sdi.cfg'])
        def test_upload_file(self, file_path):
            """ Check if local and server files are equal """
            self.upload_download_page.upload_file(file_path)
            local_file_name = file_path.split('\\')[-1]
            server_file_name = self.upload_download_page.get_file_name()

            with allure.step('Check files equality'):
                assert local_file_name == server_file_name, 'Filenames are not equal'

        def test_download_file(self):
            """ Check if server and local files are equal """
            server_file = self.upload_download_page.download_file()
            with allure.step('Check files equality'):
                assert self.upload_download_page.check_files_equality(r'F:\sampleFile.jpeg', server_file), \
                    'Filenames are not equal'

    @allure.sub_suite('Dynamic Properties')
    @allure.feature("Dynamic Properties page has 3 buttons that have dynamic behaviour")
    @pytest.mark.usefixtures('test_dynamic_properties_page_setup')
    class TestDynamicProperties:
        @pytest.fixture
        def test_dynamic_properties_page_setup(self, driver, screenshot_on_failure):
            """ Creates a DynamicPropertiesPage object and open its url """
            with allure.step('Setup DynamicPropertiesPage object and open its url'):
                url = 'https://demoqa.com/dynamic-properties'
                self.dynamic_properties_page = DynamicPropertiesPage(driver, url)
                self.dynamic_properties_page.open()

        def test_will_enable(self):
            """ Check if the button is enabled in 5 seconds """
            with allure.step('Check the button'):
                assert self.dynamic_properties_page.check_will_enable(), 'Button "Will enable 5 seconds" is not enable'

        def test_change_color(self):
            """ Check if the button changes color after 5 seconds"""
            color_before, color_after = self.dynamic_properties_page.get_colors()
            with allure.step("Check the button's colors"):
                assert color_before != color_after, 'Colors are equal'

        def test_visible_after(self):
            """ Check if the button is visible after 5 seconds"""
            with allure.step('Check the button'):
                assert self.dynamic_properties_page.check_visible_after(), 'Button "Visible After 5 Seconds" is not visible'
