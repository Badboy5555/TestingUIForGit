import csv
import allure
import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def driver():
    """ Start Firefox engine """
    with allure.step('Start Firefox engine'):
        option_load = Options()
        option_load.page_load_strategy = 'eager'
        driver_path = Service(r'C:\geckodriver.exe')
        driver = webdriver.Firefox(service=driver_path, options=option_load)
        driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def screenshot_on_failure(request, driver):
    """ Take a screenshot when test fails """
    yield
    item = request.node
    if item.rep_call.failed or item.rep_call.skipped:
        function_name = str(item).split(' ')[1].replace('>', '')
        function_datetime = str(datetime.datetime.now()).replace(':', '-').replace(' ', '-')
        screenshot_name = function_name + '-' + str(function_datetime)
        allure.attach(driver.get_full_page_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)


def pytest_addoption(parser):
    parser.addoption('--add_person_data', action='store', help='Path to a csv data file')


def data_for_web_table_add_person(path_to_file):
    """ Load data for testing Web Tables "Add" func """
    if path_to_file:
        input_data = []
        with open(path_to_file, 'r', encoding='utf-8') as R:
            for i in csv.reader(R):
                input_data.append(i)
        return input_data
    return 'No data file'


def pytest_generate_tests(metafunc):
    if 'input_data' in metafunc.fixturenames:
        loaded_data = data_for_web_table_add_person(metafunc.config.getoption('add_person_data'))
        test_cases = []
        for par in loaded_data:
            test_cases.append(pytest.param(par, marks=pytest.mark.xfail(
                ('26aaaaaaaaaaaaaaaaaaafirst' in (par[0], par[5]))
                or ('26aaaaaaaaaaaaaaaaaaaalast' in (par[1]))
                or (par[2] in ('@B_9.ru', 'A-9@.ru', 'a@b.c', 'ab.com', 'ццr@mail.ru'))
                or (par[3] in ('-1', '100', 'age'))
                or (par[4] in ('-1', '10000000000', 'salary'))
                or ('26aaaaaaaaaaaaaadepartment' in (par[5])),
                reason='Negative data tests',
                run=True)))
        metafunc.parametrize("input_data", test_cases)
