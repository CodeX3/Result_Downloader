from selenium import webdriver
import os
import platform
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import sqlite3
from sqlite3 import Error
import logging

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s :: %(levelname)s - %(message)s',
                    datefmt='%m-%d-%Y %I:%M:%S %p')


def get_result_type0(url, id_num, pwd, path):
    options = Options()
    options.headless = True
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir",path)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    profile.set_preference("pdfjs.disabled", True)

    driver = webdriver.Firefox(firefox_profile=profile, options=options)
    driver.get(url)
    if driver.find_elements_by_id("regnum"):
        RegNo = driver.find_element_by_id("regnum")
        RegNo.send_keys(id_num)
        if driver.find_elements_by_id("dob"):
            DoB = driver.find_element_by_id("dob")
            DoB.send_keys(pwd)
        login = driver.find_element_by_name('sub')
        login.click()
        driver.quit()
    elif driver.find_element_by_name("regno"):
        if driver.find_element_by_name("regno"):
            temp = driver.find_element_by_name("regno")
            temp.send_keys(id_num)
        else:
            temp = driver.find_element_by_id("regno")
            temp.send_keys(id_num)
        if driver.find_element_by_id("dob"):
            temp1 = driver.find_element_by_id("dob")
            temp1.send_keys(pwd)
        if driver.find_elements_by_name('but'):
            login = driver.find_element_by_name('but')
            login.click()
        else:
            login = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[5]/td/input')
            login.click()
        driver.quit()
    else:
        print("code missing")
    if platform.system() in "Windows":
        os.system("Taskkill /IM firefox.exe /F")



def log(exception, reg, value):
    error_data = 'Invalid Date of Birth'
    if error_data in str(exception):
        logging.error("Register number=" + reg + "||Dob=" + value + "||error : invalid date of birth")


def get_result_type1(url, result_db, path):
    options = Options()
    options.headless = True
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", path)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    profile.set_preference("pdfjs.disabled", True)
    driver = webdriver.Firefox(firefox_profile=profile, options=options)
    driver.get(url)
    no = 0
    for _ in result_db:
        id_num = result_db[no][0]
        pwd = result_db[no][1]
        try:
            if driver.find_elements_by_id("regnum"):
                RegNo = driver.find_element_by_id("regnum")
                RegNo.send_keys(id_num)
                if driver.find_elements_by_id("dob"):
                    DoB = driver.find_element_by_id("dob")
                    DoB.send_keys(pwd)
                login = driver.find_element_by_name('sub')
                login.click()
                RegNo.clear()
                DoB.clear()
            elif driver.find_element_by_name("regno"):
                if driver.find_element_by_name("regno"):
                    temp = driver.find_element_by_name("regno")
                    temp.send_keys(id_num)
                else:
                    temp = driver.find_element_by_id("regno")
                    temp.send_keys(id_num)
                if driver.find_element_by_id("dob"):
                    temp1 = driver.find_element_by_id("dob")
                    temp1.send_keys(pwd)
                if driver.find_elements_by_name('but'):
                    login = driver.find_element_by_name('but')
                    login.click()
                else:
                    login = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[5]/td/input')
                    login.click()
                temp1.clear()
                temp.clear()
            else:
                print("code missing")
        except Exception as exception:
            log(exception, reg=id_num, value=pwd)
        no += 1
    driver.quit()
    if platform.system() in "Windows":
        os.system("Taskkill /IM firefox.exe /F")


def get_db(db_path):
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM students')
        result_db = cursor.fetchall()
        cursor.close()
        connection.close()
        return result_db
    except Error as e:
        print(e)


''' link Section
BCA-BSc
http://14.139.185.44/online/UG/bsc3semresult2019/bsc3semresult.php
BBA-Bcom
http://14.139.185.44/online/UG/commerce3sem2019result/index.php
BA/BBM/BSW
http://14.139.185.44/online/UG/ba3semresult/ba3semresult.php
'''

'''data section '''

db_path = ''
link = ''
register_number = ''
date_of_birth = ''
download_path = ''

def individual(link,register_number,date_of_birth,download_path):
    try:
        get_result_type0(link, register_number, date_of_birth, download_path)
    except TimeoutException as e:
        get_result_type0(link, register_number, date_of_birth, download_path)
    except Exception as e:
        log(e, reg=register_number, value=date_of_birth)
        print(e)


'''By database'''


def by_database(link,db_path,download_path):
    result_db = get_db(db_path)
    try:
        get_result_type1(link, result_db, download_path)
    except TimeoutException as e:
        get_result_type1(link, result_db, download_path)
    except Exception as e:
        print(e)

