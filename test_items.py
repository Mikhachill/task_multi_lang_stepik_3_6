import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test__multi_lang_button(browser):
    browser.get(link)
    time.sleep(1)
    button=browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")

    assert button is not None, "Button does not exist"    
