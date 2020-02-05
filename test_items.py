import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
BUTTON_PATH = ".btn-primary"
EXPECTED_BUTTON_LEN = 1


def test_guest_should_see_button_for_add_to_basket(browser):
    browser.get(link)
    # time.sleep(30)
    button_len = len(browser.find_elements_by_css_selector(BUTTON_PATH))
    assert button_len == EXPECTED_BUTTON_LEN, f'Ooops, i can not find button with CSS: \"{BUTTON_PATH}\". ' \
                                              f'\nExpected: {EXPECTED_BUTTON_LEN} element(s), got {button_len} element(s)'
