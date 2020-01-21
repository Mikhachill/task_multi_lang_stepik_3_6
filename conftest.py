import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")
    #именно эта функция заставляет терминал запрашивать новые параметры!
 
@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language") 
    
    if  lang == 'ru':
        user_lang='ru'
    elif lang== 'fr':
        user_lang='fr'
    elif lang=='en':
        user_lang='en'
    elif lang=='es':
        user_lang='es'
    else:
        raise pytest.UsageError("You need write --language =en or =fr or =ru or =es")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
    browser = webdriver.Chrome(options=options)
    
    yield browser
    time.sleep(2) 
  
    browser.quit()
