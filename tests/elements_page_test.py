from pages.element_page import TextBoxPage


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
