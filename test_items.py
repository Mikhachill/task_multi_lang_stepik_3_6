link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    

  #  correct1='Correct!'


    #assert  == f"Correct!" ,"Слово не Correct! а {correct1}"
    
