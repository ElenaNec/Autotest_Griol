import time

from selenium.common import NoSuchElementException

from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

class TestSearchLocators:
    LOCATOR_ENTRANCE = (By.XPATH, """//*[@id="headerCartBlock"]/a[2]/div""")
    LOCATOR_REGISTRATION = (By.XPATH, """//*[@id="registration"]/div/div[2]/div/ul/li[2]""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="tabs-2"]/form/div[1]/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="tabs-2"]/form/div[2]/input""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="tabs-2"]/form/div[3]/input""")
    LOCATOR_REGISTRATION_BTN = (By.XPATH, """//*[@id="tabs-2"]/form/button""")
    LOCATOR_ERROR_REGISTRATION_FIELD = (By.XPATH, """//*[@id="tabs-2"]/form/div[4]/div""")

    LOCATOR_ERROR_LOGIN_FIELD = (By.XPATH, """// *[ @ id = "tabs-1"] / form / div[3] / div""")
    LOCATOR_ENTR_CLICK = (By.XPATH, """//*[@id="registration"]/div/div[2]/div/ul/li[1]""")
    LOCATOR_LOGIN_EMAIL_FIELD = (By.XPATH, """//*[@id="email"]""")
    LOCATOR_LOGIN_PASSW_FIELD = (By.XPATH, """//*[@id="password"]""")
    LOCATOR_ENTRANCE_BTN = (By.XPATH, """//*[@id="tabs-1"]/form/button""")
    LOCATOR_LK_TEXT = (By.XPATH, """/html/body/main/div/div[2]/h1""")

    LOCATOR_EXIT_LK = (By.XPATH, """/html/body/main/div/div[1]/ul/li[5]/a""")

    LOCATOR_ICON_SEARCH = (By.XPATH, """//*[@id="title-search-mob"]/form/button/div/span""")
    LOCATOR_SEARCH_FIELD = (By.XPATH, """// *[ @ id = "title-search-mob"] / form / div""")
    LOCATOR_SEARCH_FIELD_1 = (By.XPATH, """/html/body/main/div/div/div/form/input[1]""")

    LOCATOR_CATALOG_CLOTH = (By.XPATH, """/html/body/header/div[3]/div/div/div[2]/div[2]/ul/li[2]""")
    LOCATOR_POZITION_1 = (By.XPATH, """/html/body/main/div/div[2]/div[5]/div[1]/div[2]/a""")
    LOCATOR_POZITION_1_SIZE = (By.XPATH, """/html/body/main/div[1]/div[1]/div[2]/div/div[7]/ul/li[1]""")
    LOCATOR_POZITION_ADD_BASKET = (By.XPATH, """/html/body/main/div[1]/div[1]/div[2]/div/div[9]/a[2]""")

    LOCATOR_POZITION_2 = (By.XPATH, """//*[@id="img-slider-127574"]""")
    LOCATOR_POZITION_2_SISE = (By.XPATH, """/html/body/main/div[1]/div[1]/div[2]/div/div[7]/ul/li[1]""")
    LOCATOR_QUANTITY_IN_BASKET = (By.XPATH, """//*[@id="basket_form"]/div[2]/div[2]/div[1]/span[2]""")

    LOCATOR_PLUS = (By.XPATH, """//*[@id="basket_form"]/div[1]/div[2]/div[3]/div/span[2]""")
    LOCATOR_MINUS = (By.XPATH, """//*[@id="basket_form"]/div[1]/div[2]/div[3]/div/span[1]""")

    LOCATOR_ICON_BASKET = (By.XPATH, """//*[@id="bx_basketFKauiI"]/div""")
    LOCATOR_BASKET_TEXT = (By.XPATH, """/html/body/main/div""")

    LOCATOR_ICON_SEARCH_BTN = (By.XPATH, """//*[@id="title-search-mob"]/form/button""")
    LOCATOR_RESULT_SEARCH = (By.XPATH, """/html/body/main/div/div/div[2]/div[1]/div[2]/a""")

    LOCATOR_PRICE_1 = (By.XPATH, """//*[@id="basket_form"]/div[1]/div[2]/div[2]""")
    LOCATOR_PRICE_2 = (By.XPATH, """//*[@id="basket_form"]/div[1]/div[3]/div[2]""")
    LOCATOR_TOTAL_PRICE = (By.XPATH, """//*[@id="basket_form"]/div[2]/div[2]/div[2]/span[2]""")

    LOCATOR_DELITE = (By.XPATH, """//*[@id="basket_form"]/div[1]/div[2]/div[3]/span[2]""")

    LOCATOR_CHECKOUT = (By.XPATH, """//*[@id="basket_form"]/div[2]/div[2]/div[3]/a[2]""")

    LOCATOR_CHECKOUT_TEXT = (By.XPATH, """/html/body/main/div/h1""")

class OperationsHelper(BasePage):

    # поиск поля регистрация пользователя
    def find_registration_field(self):
         self.find_element(TestSearchLocators.LOCATOR_ENTRANCE).click()
         self.find_element(TestSearchLocators.LOCATOR_REGISTRATION).click()

    # ввод данных в поле email вкладки регистрация
    def enter_email(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    # ввод данных в поле  пароль вкладки регистрация
    def enter_pass(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        passw_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        passw_field.clear()
        passw_field.send_keys(word)

    # ввод данных в поле  ваше имя вкладки регистрация
    def enter_name(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    # клик на кнопку регистрация при авторизации
    def click_login_button(self):
        logging.info("Click loging button")
        self.find_element(TestSearchLocators.LOCATOR_REGISTRATION_BTN).click()

    # получение текста ошибки при регистрации
    def get_error_text(self):
        logging.info("Get_error_text")
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_REGISTRATION_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_REGISTRATION_FIELD[1]}")
        return text


    # поиск иконки лк для авторизации пользователя
    def find_login_field(self):
        logging.info("Click loging button")
        entrance_field = self.find_element(TestSearchLocators.LOCATOR_ENTRANCE).click()

    # клик на кнопку вкладки вход при авторизации
    def entr_click(self):
        logging.info("Click entr button")
        entr_click = self.find_element(TestSearchLocators.LOCATOR_ENTR_CLICK).click()

    # ввод данных в поле email вкладки вход при авторизации
    def enter_email_entr(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_LOGIN_EMAIL_FIELD[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    # ввод данных в поле пароль вкладки вход при авторизации
    def enter_passw_entr(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_LOGIN_PASSW_FIELD[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_PASSW_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    # клик на кнопку войти  при авторизации
    def click_entrance_button(self):
        logging.info("Click entrance button")
        self.find_element(TestSearchLocators.LOCATOR_ENTRANCE_BTN).click()

    # Получение текста лк при успешной авторизации
    def get_lk_text(self):
        logging.info("Get_lk_text")
        lk_field = self.find_element(TestSearchLocators.LOCATOR_LK_TEXT, time=3)
        text = lk_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_LK_TEXT[1]}")
        return text

    # Выходит из личного кабинета пользователя
    def exit_lk(self):
        logging.info("Exit lk")
        self.find_element(TestSearchLocators.LOCATOR_EXIT_LK).click()

    # получение текста ошибки при авторизации
    def get_error_login_text(self):
        logging.info("Get error_login_text")
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_LOGIN_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_LOGIN_FIELD[1]}")
        return text


    # поиск иконки search
    def find_icon_search(self):
        logging.info("Find icon_search")
        icon_field = self.find_element(TestSearchLocators.LOCATOR_ICON_SEARCH)
        time.sleep(1)
        return icon_field

    # поиск иконки корзины
    def find_icon_basket(self):
        logging.info("Get basket text")
        icon_basket = self.find_element(TestSearchLocators.LOCATOR_ICON_BASKET).click()

    # проверка работы иконки корзины
    def get_basket_text(self):
        logging.info("Get basket text")
        self.find_icon_basket()
        time.sleep(2)
        basket_text = self.find_element(TestSearchLocators.LOCATOR_BASKET_TEXT)
        text = basket_text.get_attribute('textContent')
        return text


    # ввод ключевого слова в поле поиска
    def enter_keyword_seach(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_SEARCH_FIELD_1[1]}")
        try:
            search_field = self.find_element(TestSearchLocators.LOCATOR_SEARCH_FIELD_1, time=3)
        except NoSuchElementException:
            search_field = self.find_element(TestSearchLocators.LOCATOR_SEARCH_FIELD, time=3)
        search_field.clear()
        search_field.send_keys(word)
        search_field.send_keys(Keys.ENTER)

    # получение текста результата поиска
    def get_text_result_search(self):
        logging.info("Get search text")
        result_search = self.find_element(TestSearchLocators.LOCATOR_RESULT_SEARCH).text
        # text = result_search.get_attribute('href')
        return result_search

    # поиск кнопки лупы
    def find_icon_search_btn(self):
        logging.info("Find icon_search_btn")
        icon_field = self.find_element(TestSearchLocators.LOCATOR_ICON_SEARCH_BTN)
        return icon_field


    #  поиск каталога товара
    def find_catalog_cloth(self):
        logging.info("Find catalog_cloth")
        catalog_cloth = self.find_element(TestSearchLocators.LOCATOR_CATALOG_CLOTH).click()
        return catalog_cloth

     # выбор товара 1
    def product_selection(self):
        logging.info("Selection pozition 1")
        self.find_element(TestSearchLocators.LOCATOR_POZITION_1).click()

    # выбор товара 2
    def product_selection_2(self):
        logging.info("Selection pozition 2")
        self.find_element(TestSearchLocators.LOCATOR_POZITION_2).click()

    # выбор размера
    def size_selection(self):
        logging.info("Selection size")
        self.find_element(TestSearchLocators.LOCATOR_POZITION_1_SIZE).click()

    # добавление в корзину
    def add_in_basket(self):
        logging.info("Add in basket")
        self.find_element(TestSearchLocators.LOCATOR_POZITION_ADD_BASKET).click()

    # количество товаров в корзине
    def get_text_quantity_basket(self):
        logging.info("Get text_quantity_basket")
        quantity = self.find_element(TestSearchLocators.LOCATOR_QUANTITY_IN_BASKET)
        text = quantity.get_attribute('textContent')
        return text

    # увеличение товаров в корзине
    def more_position_basket(self):
        logging.info("Add in basket")
        self.find_element(TestSearchLocators.LOCATOR_PLUS).click()

    # общая цена товаров в корзине
    def get_total_price(self):
        logging.info("Get total_price")
        price = self.find_element(TestSearchLocators.LOCATOR_TOTAL_PRICE)
        text = price.get_attribute('textContent')
        return text

    # получение цены 1 товара
    def get_price_1(self):
        logging.info("Get price_1")
        price = self.find_element(TestSearchLocators.LOCATOR_PRICE_1)
        text = price.get_attribute('textContent')
        return text

    # получение цены 2 товара
    def get_price_2(self):
        logging.info("Get price_2")
        price = self.find_element(TestSearchLocators.LOCATOR_PRICE_2)
        text = price.get_attribute('textContent')
        return text

    # клик на кнопку удалить
    def delite_click(self):
        logging.info("Delite basket")
        self.find_element(TestSearchLocators.LOCATOR_DELITE).click()

    # клик на кнопку оформить заказ
    def click_ckeckout(self):
        logging.info("Click ckeckout")
        self.find_element(TestSearchLocators.LOCATOR_CHECKOUT).click()

    # Получение текста страницы оформления заказа
    def get_ckeckout_text(self):
        logging.info("Get ckeckout_text")
        ckeckout = self.find_element(TestSearchLocators.LOCATOR_CHECKOUT_TEXT)
        text = ckeckout.text
        return text

