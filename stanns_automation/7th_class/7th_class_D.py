
from datetime import datetime

import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get('https://stanns.tatotechnologies.com/login')
driver.maximize_window()
username=driver.find_element(By.NAME,'email')
password= driver.find_element(By.NAME,'password')
submit = driver.find_element(By.XPATH, "//*[contains(@class,'input-control-input')]//following::input[3]")
# form elements
def test_login():
    username.send_keys('admin@stanns.tatotechnologies.com')
    # time.sleep(5)
    password.send_keys('Stanns@1113')
    # time.sleep(5)
    submit.click()

def test_open_admission():
    driver.get('https://stanns.tatotechnologies.com/student-admission')
    time.sleep(5)

def select_class():
    time.sleep(10)
    select_class = driver.find_element(By.XPATH,
                                       "//div[@class='nice-select primary_select form-control']//span[@class='current'][contains(text(),'Class')]")
    select_class.click()
    time.sleep(2)
    # selecting class
    select_first_class = driver.find_element(By.XPATH,
                                             "//div[@class='nice-select primary_select form-control open']//li[@class='option'][normalize-space()='8 Class']")

    select_first_class.click()
    time.sleep(2)

def select_section(sec):
    # selecting section
    time.sleep(5)
    section = driver.find_element(By.XPATH, "//span[normalize-space()='Select Section *']")
    section.click()
    time.sleep(2)
    select_sec = driver.find_element(By.XPATH, f"//li[normalize-space()='{sec}']")
    select_sec.click()
    time.sleep(5)

def select_admission_number(ad_number):
    # admission number
    admission_number = driver.find_element(By.XPATH, "//input[@name='admission_number']")
    admission_number.clear()
    admission_number.send_keys(ad_number)
    # time.sleep(5)

def select_first_name(name):

    # filling first name
    first_name = driver.find_element(By.XPATH,"//input[@name='first_name']")
    first_name.send_keys(name)
    # time.sleep(5)

def select_admission_date(date):
    # selecting admission date
    admission_date = driver.find_element(By.XPATH, "//input[@id='admission_date']")
    # time.sleep(5)
    admission_date.clear()
    admission_date.send_keys(date)
    # time.sleep(5)
    # day = date.split('/')[1]  # Get DD from YYYY-MM-DD
    # pick_date = driver.find_element(By.XPATH, f"//td[ @class ='day'][normalize-space()='{day}']")
    # pick_date.click()
    # time.sleep(5)

def select_student_email(email):
    student_email = driver.find_element(By.XPATH, "//input[@id='email_address']")
    student_email.send_keys(email)

    # actions.send_keys(Keys.PAGE_DOWN).perform()  # Scroll one page down
    # actions.send_keys(Keys.PAGE_UP).perform()  # Scroll one page up
    # actions.send_keys(Keys.END).perform()  # Scroll to bottom
    actions.send_keys(Keys.PAGE_UP).perform()
    actions.send_keys(Keys.PAGE_UP).perform()
    time.sleep(5)

def select_parent_email(parent_mail):
    actions.send_keys(Keys.PAGE_UP)
    time.sleep(2)
    select_parent_section = driver.find_element(By.XPATH, "//*[@role='tablist']//child::li[2]")
    time.sleep(5)
    select_parent_section.click()

    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(5)
    parent_email = driver.find_element(By.XPATH, "//input[@id='guardians_email']")
    parent_email.send_keys(parent_mail)
    time.sleep(2)

def select_date_of_birth(date):
    ele=driver.find_element(By.XPATH,f"//input[@id='date_of_birth']")
    ele.clear()
    ele.send_keys(date)

def save_student_data():
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)
    save=driver.find_element(By.XPATH,"//button[@id='_submit_btn_admission']")
    if save.is_displayed():
        time.sleep(2)
        save.click()
    else:
        for x in range(2):
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
    time.sleep(5)

from openpyxl import load_workbook
wb = load_workbook('C:/Users/veera/Downloads/stanns_1_B_students_D.xlsx')  # Change to your file name
sheet = wb.active






def test_upload_student_bulk_data(admission_number,first_name,date,student_mail,parent_mail,date_of_birth):

    select_class() # select 1 class
    select_first_name(first_name)
    select_admission_number(admission_number)
    select_section('D') # selects A section
    select_admission_date(date)
    select_student_email(student_mail)
    select_date_of_birth(date_of_birth)
    select_parent_email(parent_mail)
    save_student_data()
    # print(admission_number,first_name,date,student_mail,parent_mail)

def test_add_data_to_portal():
    test_login()
    test_open_admission()
    for i, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
            if i >41 :  # Stop after 47th data row (row 48 in Excel)
                break
            number = str(row[0]).replace('.0', '') if row[0] else ''  # 1st column
            first_name = row[1]  # 2nd column
            email = row[2]  # 3rd column
            date_obj = datetime.strptime(str(row[3]).split()[0], '%Y-%m-%d')
            admission_date = date_obj.strftime('%m/%d/%Y')
            # admission_date = str(row[3]).split()[0] if row[3] else ''  # 4th column
            guardian_email = row[4]  # 5th column
            date_obj1 = datetime.strptime(str(row[5]).split()[0], '%Y-%m-%d')
            stu_birth = date_obj1.strftime('%m/%d/%Y')
            print('the last taken name is', number)
            test_upload_student_bulk_data(admission_number=number, first_name=first_name, date=admission_date,
                                          student_mail=email, parent_mail=guardian_email,date_of_birth=stu_birth)
            print('the last uploaded name is',number)




