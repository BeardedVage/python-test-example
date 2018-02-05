import allure
import csv
import page
from hamcrest import *
from decimal import *


@allure.feature('Functional testing')
@allure.story('Check convertation of currency')
@allure.step('Check default values in converter.')
def test_check_default_settings(driver):
    calc_page = page.CalcPage(driver)
    assert_that(calc_page.get_data_from_currencyFrom_dropdown().text), equal_to('RUB')
    assert_that(calc_page.get_data_from_currencyTo_dropdown().text), equal_to('USD')
    assert_that((calc_page.get_data_from_currencyValue_input()).get_attribute('value')), equal_to('100')


@allure.step('Check work of calculator with default data.')
def test_converting_with_default_settings(driver):

    calc_page = page.CalcPage(driver)
    # we should use data provider and equivalence classese to set this data
    currency_value = 1
    currency_from = "RUB"  # todo grab default value from calc
    currency_to = "USD"

    # move to setup
    with open('data/rate.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if (row[0] == currency_from and row[1] == currency_to):
                rate = Decimal(row[2])

    with allure.step('Entering the next value to convert: ' + str(currency_value)):
        calc_page.set_currency_value = currency_value
    with allure.step('Convert data by actual rate: ' + str(rate)):
        calc_page.click_convert_button()
        calc_page.is_calculation_finished()

    convertation_result = Decimal(rate) * currency_value
    convertation_result = str(convertation_result).replace('.', ',')
    expected_value_from = str(currency_value) + ',00 ' + currency_from + ' ='
    expected_value_to = convertation_result + ' ' + currency_to
    with allure.step('Verifying result of conversation.'):
        assert_that(calc_page.get_converted_value_from().text), equal_to(expected_value_from)
        assert_that(calc_page.get_converted_value_to().text), equal_to(expected_value_to)


@allure.step('Enter value of currency and choose currency in calculator and assert calculation result')
def test_converting_with_changed_currency(driver):

    calc_page = page.CalcPage(driver)

    currency_value = 1  # todo use data provider and equivalence classes to set this value
    currency_from = "USD"
    currency_to = "RUB"

    with allure.step('Entering the next value to convert: ' + str(currency_value)):
        calc_page.set_currency_value = currency_value

    with open('data/rate.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if (row[0] == currency_from and row[1] == currency_to):
                rate = Decimal(row[2])

    with allure.step('Choose currency from: ' + str(currency_from)):
        calc_page.choose_currency_from(currency_from)
        # todo add one more test with radio buttons

    with allure.step('Convert data by actual rate: ' + str(rate)):
        calc_page.click_convert_button()
        calc_page.is_calculation_finished()

    convertation_result = Decimal(rate) * currency_value
    convertation_result = str(convertation_result).replace('.', ',')
    expected_value_from = str(currency_value) + ',00 ' + currency_from + ' ='
    expected_value_to = str(convertation_result) + ' ' + currency_to

    with allure.step('Verifying result of conversation.'):
        assert_that(calc_page.get_converted_value_from().text), equal_to(expected_value_from)
        assert_that(calc_page.get_converted_value_to().text), equal_to(expected_value_to)

