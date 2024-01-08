from selenium.webdriver import Keys

from site_griol_page1 import OperationsHelper
import logging, time, yaml


with open(r"C:\Users\user\Desktop\pythonProject1\MY_DIP_GRIOL\config.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    url = testdata['address']

# Проверка возможности регистрации с уже существующем аккаунтом
def test_step1(browser):
    logging.info('Test_1 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    testpage.find_registration_field()
    testpage.enter_email('nechaeva@mail.ru')
    time.sleep(1)
    testpage.enter_pass('testtest')
    time.sleep(1)
    testpage.enter_name('test')
    time.sleep(1)
    testpage.click_login_button()
    time.sleep(2)
    assert testpage.get_error_text() == 'Пользователь с логином "nechaeva@mail.ru" уже существует.'


# Проверка возможности войти в аккаунт с валидными данными пользователя
def test_step2(browser):
    logging.info('Test_2 Starting')
    testpage = OperationsHelper(browser, url)
    # testpage.go_to_site()
    time.sleep(1)
    testpage.entr_click()
    # testpage.find_login_field()
    testpage. enter_email_entr('nechaeva@mail.ru')
    testpage.enter_passw_entr("testtest")
    testpage.click_entrance_button()
    time.sleep(5)
    testpage.find_login_field()
    time.sleep(5)
    assert testpage.get_lk_text() == 'Мои заказы'


 # Проверка возможности войти в аккаунт с не валидными данными пароля
def test_step3(browser):
    logging.info('Test_3 Starting')
    testpage = OperationsHelper(browser, url)
    # testpage.go_to_site()
    time.sleep(1)
    testpage.exit_lk()
    time.sleep(1)
    testpage.find_login_field()
    testpage.enter_email_entr('nechaeva@mail.ru')
    testpage.enter_passw_entr("test")
    testpage.click_entrance_button()
    time.sleep(2)
    assert testpage.get_error_login_text() == 'Неверный логин или пароль.'

# Проверка возможности войти в аккаунт с данными, не существующего аккаунта
def test_step4(browser):
    logging.info('Test_4 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    testpage.find_login_field()
    testpage.enter_email_entr('nechaeva_lena@mail.ru')
    testpage.enter_passw_entr("test")
    testpage.click_entrance_button()
    time.sleep(2)
    assert testpage.get_error_login_text() == 'Неверный логин или пароль.'

# Проверка наличия иконки для поиска товара
def test_step5(browser):
    logging.info('Test_5 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    time.sleep(2)
    icon_fild = testpage.find_icon_search()
    icon_fild_text =icon_fild.get_attribute("textContent")
    time.sleep(1)
    assert icon_fild_text == 'поиск'

# Проверка правильности работы иконки корзина
def test_step6(browser):
    logging.info('Test_6 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    time.sleep(2)
    testpage.find_icon_search()
    assert 'Корзина' in testpage.get_basket_text()

# Поиск товара по ключевому слову «блузка»
def test_step7(browser):
    logging.info('Test_7 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    time.sleep(2)
    icon = testpage.find_icon_search_btn()
    time.sleep(1)
    icon.click()
    time.sleep(2)
    testpage.enter_keyword_seach(testdata['keyword1'])
    time.sleep(2)
    assert 'Блузка' in testpage.get_text_result_search()

# Поиск по частичному совпадению «блу» в ключевом слове «блузка»
def test_step8(browser):
    logging.info('Test_8 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    time.sleep(2)
    icon = testpage.find_icon_search_btn()
    time.sleep(1)
    icon.click()
    time.sleep(2)
    testpage.enter_keyword_seach(testdata['keyword2'])
    time.sleep(2)
    assert 'Блузка' in testpage.get_text_result_search()

# Добавление товаров в корзину
def test_step9(browser):
    logging.info('Test_9 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    time.sleep(2)
    testpage.find_catalog_cloth()
    testpage.product_selection()
    testpage.size_selection()
    testpage.add_in_basket()
    testpage.find_icon_basket()
    assert '1' in testpage.get_text_quantity_basket()

# Обновление количества товаров в корзине
def test_step10(browser):
    logging.info('Test_10 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    time.sleep(2)
    # testpage.find_catalog_cloth()
    # testpage.product_selection()
    # testpage.size_selection()
    # testpage.add_in_basket()
    testpage.find_icon_basket()
    testpage.more_position_basket()
    time.sleep(2)
    assert '2' in testpage.get_text_quantity_basket()

# Добавление товаров в корзину, в которой уже есть одно наименование
def test_step11(browser):
    logging.info('Test_11 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    time.sleep(2)
    testpage.find_icon_basket()
    testpage.delite_click()
    testpage.find_catalog_cloth()
    testpage.product_selection()
    testpage.size_selection()
    testpage.add_in_basket()
    testpage.find_catalog_cloth()
    testpage.product_selection_2()
    testpage.size_selection()
    testpage.add_in_basket()
    testpage.find_icon_basket()
    time.sleep(2)

    pr_1 = testpage.get_price_1()
    price_1 = pr_1.split()
    price_one = int(price_1[0]+price_1[1])
    pr_2 = testpage.get_price_2()
    price_2 = pr_2.split()
    price_two = int(price_2[0]+price_2[1])
    time.sleep(2)
    pr_tot = testpage.get_total_price()
    price_tot = pr_tot.split()
    price_total = int(price_tot[0]+price_tot[1])

    assert price_total == price_two+price_one

# Удаление товаров из корзины, в которой больше чем одно наименование
def test_step12(browser):
    logging.info('Test_12 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    time.sleep(2)
    # testpage.find_catalog_cloth()
    # testpage.product_selection()
    # testpage.size_selection()
    # testpage.add_in_basket()
    # testpage.find_catalog_cloth()
    # testpage.product_selection_2()
    # testpage.size_selection()
    # testpage.add_in_basket()
    testpage.find_icon_basket()
    time.sleep(2)

    testpage.delite_click()
    time.sleep(2)
    assert '1' in testpage.get_text_quantity_basket()

# Удаление товаров из корзины, в которой одно наименование товара
def test_step13(browser):
    logging.info('Test_13 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    time.sleep(2)
    testpage.find_catalog_cloth()
    testpage.product_selection()
    testpage.size_selection()
    testpage.add_in_basket()
    testpage.find_icon_basket()
    time.sleep(2)
    testpage.delite_click()
    time.sleep(2)
    assert 'Корзина' in testpage.get_basket_text()

# Проверка работы кнопки оформить заказ
def test_step14(browser):
    logging.info('Test_14 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    time.sleep(2)
    testpage.find_catalog_cloth()
    testpage.product_selection()
    testpage.size_selection()
    testpage.add_in_basket()
    testpage.find_icon_basket()
    time.sleep(2)

    testpage.click_ckeckout()
    time.sleep(2)
    assert 'Оформление заказа' in testpage.get_ckeckout_text()
