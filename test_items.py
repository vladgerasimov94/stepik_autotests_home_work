import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    browser.find_element_by_css_selector(".btn-primary")

# Написать внятный ассерт
