import time
from selenium.webdriver.common.by import By


link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_add_to_basket_button(browser):
    browser.get(link)
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(button) > 0, 'Элемент не найден'
    
    # time.sleep(10)    # Раскомментировать строчку для удобства проверки кнопки на другом языке
