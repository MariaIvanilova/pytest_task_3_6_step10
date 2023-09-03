from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_add_to_basket_button(browser):
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
