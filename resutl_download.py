from selenium import webdriver
from selenium.webdriver.firefox.options import Options



def get_result_type0(url, id_num, pwd, path):
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
    if driver.find_elements_by_id("regnum"):
        RegNo = driver.find_element_by_id("regnum")
        RegNo.send_keys(id_num)
        if driver.find_elements_by_id("dob"):
            DoB = driver.find_element_by_id("dob")
            DoB.send_keys(pwd)
        login = driver.find_element_by_name('sub')
        login.click()
        driver.close()
    elif driver.find_element_by_name("regno"):
        if driver.find_element_by_name("regno"):
            temp = driver.find_element_by_name("regno")
            temp.send_keys(id_num)
        else :
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
        driver.close()
    else:
        print("code missing")


'''
BCA-BSc
http://14.139.185.44/online/UG/bsc3semresult2019/bsc3semresult.php


BBA-Bcom
http://14.139.185.44/online/UG/commerce3sem2019result/index.php


BA/BBM/BSW
http://14.139.185.44/online/UG/ba3semresult/ba3semresult.php


'''

link = ''
register_number = ''
date_of_birth = ''
download_path = ''

try:
    get_result_type0(link, register_number, date_of_birth, download_path)
except Exception as e:
    print(e) 
