import pytest
from pages.element_page import TextBoxPage, RadioButtonPage


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

    @pytest.mark.usefixtures('setup')
    class TestRadioButton:
        @pytest.fixture
        def setup(self, driver2):
            url = 'https://demoqa.com/radio-button'
            self.rb = RadioButtonPage(driver2, url)
            self.rb.open()

        def test_radio_button_yes(self):
            self.rb.yes_button_click()
            result_text = self.rb.get_result_text()
            assert 'Yes' in result_text, 'There is a missing in Yes-radiobutton functon'

        @pytest.mark.xfail(reason='tag "radio" is disabled', run=False)
        def test_radio_button_no(self):
            self.rb.no_button_click()
            result_text = self.rb.get_result_text()
            assert 'No' in result_text, 'There is a missing in Yes-radiobutton functon'

        def test_radio_button_impressive(self):
            self.rb.impressinve_button_click()
            result_text = self.rb.get_result_text()
            assert 'Impressive' in result_text, 'There is a missing in Yes-radiobutton functon'
