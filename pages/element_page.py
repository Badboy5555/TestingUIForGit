from pages.base_page import BasePage
from locators.Locators import TextBoxPageLocators
from generator.generator import generate_data


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
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

        submit = self.element_is_clicable(self.locators.SUBMIT)
        self.go_to_element(submit)
        submit.click()
        return input_full_name, input_email, input_current_address, input_permanent_address

    def get_output_form(self):
        output_full_name = self.element_is_present(self.locators.OUTPUT_FULL_NAME).text.split(':')[-1]
        output_email = self.element_is_present(self.locators.OUTPUT_EMAIL).text.split(':')[-1]
        output_current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[-1]
        output_current_address.replace('\n', ' ')
        output_permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[-1]
        output_permanent_address.replace('\n', ' ')
        return output_full_name, output_email, output_current_address, output_permanent_address




