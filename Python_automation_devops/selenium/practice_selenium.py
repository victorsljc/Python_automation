from selenium.webdriver import ActionChains
from selenium.webdriver.common.devtools.v130.page import Screenshot
from selenium.webdriver.common.devtools.v85.runtime import ExecutionContextId
'''
source link :- https://selectorshub.com/xpath-practice-page/
Xpaths
1. //*[@text='New User ? Register here/Activate']:
    This selects any element (*) that has an attribute named "text" whose value is exactly equal to "New User ? Register here/Activate".
    This is appropriate if the string you provided is the value of an attribute called text

2. //*[text()='New User ? Register here/Activate']:
    This selects any element (*) whose text content (the text displayed inside the element) is exactly equal to "New User ? Register here/Activate".
    The text() function extracts the text content of the element.
    This is appropriate if the string is the text that is displayed directly within the element, not the value of an attribute.

3. //*[contains(text(),'New User ? Register here/Activate')]
    source link - https://retail.onlinesbi.sbi/retail/login.htm

4. //*[contains(@href, 'step')]

5. //*[contains(@text, 'New User ? Register here/Activate')]
6. //div[@id='content']/child::p
7. //div[@id='main-section']/following::div
8. //div[@id='username']/parent::form
9. //input[@type='text']/ancestor::form
10. //input[@id = 'text']//self::input

Browser Navigation methods
    1. driver.get()
    2. driver.back()
    3.driver.forward()
    4.driver.refresh()

Browser window and session management
    1. driver.maximize_window()
    2.driver.minimize_window()
    3.driver.fullscreen_window()
    4.driver.get_window_size()
    5.driver.set_window_size()
    6.driver.get_widow_position()
    7.driver.set_window_position()

Finding web elements
    1.driver.find_element(By.XPATH,'')
    2.driver.find_element(By.NAME,'')
    3.driver.find_element(By.CLASS,'')
    4.driver.find_element(By.CSS_SELECTOR,'')
    5.driver.find_element(By.TAG_NAME,'')
    6.driver.find_element(By.LINK_TEXT,'')
    7.driver.find_element(By.PARTIAL_LINK_TEXT,'')

New Tab/ Window Management
    1.driver.switch_to.new_window('tab')
    2.driver.switch_to.new_window('window')
    3.w=driver.window_handle
    4.driver.switch_to.window(w[0])
    5.driver.switch_to.current_window_handle

Element Interacion Methods

    1.element.click()
    2.element.send_keys()
    3.element.is_displayed()
    4.element.is_selected()
    5.element.is_enabled()
    6.element.get_attribute()
    7.element.clear()

Wait_methods

    1.implicit_wait(10)
    2.explicit_wait()
        wait=webdriverwait(driver,10)
        wait.until(EC.presence_of_element_located(By.ID,''))

Alert and Popup handling

    alert=driver.switch_to.alert
    alert.accept()
    alert.dismiss()
    alert.send_keys()
    alert.text

Frame Handling

    driver.switch_to.frame('frame_name')
    driver.switch_to.default_content() swithces back to main content

Screenshot
    driver.save_screenshot('path')

Cookie Handling
    cookie_one={'name':'cookie_name','value':'cookie_value'}
    driver.get_cookie(cookie_one)
    driver.add_cookie(cookie_one)
    driver.get_cookies()
    driver.delete_cookie(cookie_one)
    driver.delete_all_cookies()

Javascript Execution

    driver.execute_script('window.scrollTo(0, 1000);')

Quit & close methods

    driver.close()
    driver.quit()

Keyboard Actions

    actions = ActionChains(driver)
    1.action.key_down(keys.CONTROL).send_keys('A').Key_up(key.CONTROL).perform()
    2.element.send_keys(key.ENTER)

Mouse Actions

    element=driver.find_element(By.ID,'')
    actions.click(element).perform()
    actions.double_click(element).perform()
    actions.move_to_element(element).perform()
    actions.move_to_element_with_offset(element, 100, 200).perform()
    actions.drag_and_drop_by_offset(element, 100, 200).perform()
    actions.drag_and_drop(source_element, target_element).perform()
    actions.context_click(element).perform() #performs right click operations

Dropdown

    element=driver.find_element(By.ID,'')
    dropdown=Select(element)
    dropdown.select_by_visible_text()
    dropdown.select_by_value()
    dropdown.select_by_index()

'''

