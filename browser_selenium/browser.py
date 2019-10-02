

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver import ChromeOptions, Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import time
import readline

ENTER = '\ue007'
MAX_WAIT_SECS = 20

SELENIUM_DRIVER_PATH = './browser_selenium/chromedriver'
ROOT = 'http://127.0.0.1:8000/'


def save_history(file='.history'):
  readline.write_history_file(file)

class Browser(Chrome):
  def __init__(self):
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    super().__init__(executable_path=SELENIUM_DRIVER_PATH, options=chrome_options)
    self.wait = WebDriverWait(self, MAX_WAIT_SECS)

  def wait_for_element(self, xpath):
    return self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

  def get_url(self, path):
    return ROOT + path

  def get_anchor_by_href(self, path):
    return self.find_elements_by_xpath(f"//a[contains(@href, {path})]")
  
  def xpath_str(self, _type, selector, value):
    return f"//{_type}[@{selector}='{value}']"

  def get_element(self, _type, selector, value):
    return self.find_element_by_xpath(f"//{_type}[@{selector}='{value}']")

  def get_element_containing_text(self, text):
    return self.find_element_by_xpath(f"//*[contains(text(), '{text}')]")

  def click_element(self, _type, selector, value):
    element = self.get_element(_type, selector, value)
    element.click()
    return element

  def click_element_with_id(self, id):
    element = self.find_element_by_id(id)
    element.click()
    return element

  def scroll_to_element(self, id):
    return self.execute_script(f'document.getElementById("{id}").scrollIntoView();')

  def scroll_to_bottom(self):
    return self.execute_script('window.scrollTo(0, document.body.scrollHeight);')

  def browse_to(self, path):
    return self.get(self.get_url(path))

  def get(self, *args, **kwargs):
    return super().get(*args, **kwargs)

  def exit(self):
    self.browse_to('logout')
    self.close()
    self.quit()
    return quit()
     

#=============================================

browser = Browser()

browser.browse_to('new-project-step-2/?id=41622')

browser.scroll_to_bottom()
save_and_continue_btn = browser.wait_for_element(browser.xpath_str('input', 'value', 'Guardar y continuar'))
save_and_continue_btn.click()


def go_back_and_continue():
  browser.back()
  browser.wait_for_element(browser.xpath_str('input', 'value', 'Guardar y continuar')).click()


'''
browser.click_element_with_id('projects-info')
## step one
browser.click_element_with_id('new-project')
browser.click_element_with_id('select2-prospect-container')

prospect_filed = browser.find_element_by_class_name('select2-search__field')
prospect_filed.send_keys('qwerty')
prospect_filed.send_keys(ENTER)

browser.scroll_to_bottom()
save_and_continue_btn = browser.wait_for_element(browser.xpath_str('input', 'value', 'Guardar y continuar'))
save_and_continue_btn.click()


# ================
# step two
required_field = browser.click_element_with_id('id_name')
required_field.send_keys('random_project_name')

required_field = browser.click_element_with_id('id_clientName')
required_field.send_keys('random_client')

browser.scroll_to_element('auto-fill')
browser.click_element_with_id('auto-fill')

browser.scroll_to_bottom()
save_and_continue_btn = browser.wait_for_element(browser.xpath_str('input', 'value', 'Guardar y continuar'))
save_and_continue_btn.click()

# ================
# step tree

time.sleep(1)
browser.scroll_to_bottom()
save_and_continue_btn = browser.wait_for_element(browser.xpath_str('input', 'value', 'Guardar y continuar'))
save_and_continue_btn.click()


# ==================
# step four

modal = browser.get_element_containing_text('Atención, se han tomado valores de referencia.')

if modal.is_displayed():
  browser.click_element('button', 'class', 'confirm')
  time.sleep(1)

browser.click_element('label', 'for', 'id_roofType_2')

browser.scroll_to_bottom()
time.sleep(1)

browser.click_element('button', 'id', 'save-continue-intro')

# ==================
# step five

time.sleep(1)
browser.scroll_to_bottom()
browser.click_element('select', 'id', 'quote-templates-select-preview')
browser.click_element('option', 'value', '914')

pdf_preview = browser.wait_for_element(browser.xpath_str('object', 'type', 'application/pdf'))

print('done!')

#viewer-pdf-toolbar

#browser.get_element_containing_text('Atención, se han tomado valores de referencia.')


#//#paymentsChart/input[@type='password']

'''

'''
def get_element(self, _type, selector, value):
    return self.find_element_by_xpath(f"//{_type}[@{selector}='{value}']")

'''
#readline.write_history_file('.history')



