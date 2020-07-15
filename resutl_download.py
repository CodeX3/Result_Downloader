from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", '/home/dh12/PycharmProjects/ResultDownloader/result')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
profile.set_preference("pdfjs.disabled", True);

driver = webdriver.Firefox(firefox_profile=profile,options=options)
driver.get("http://14.139.185.44/online/UG/bsc3semresult2019/bsc3semresult.php")
RegNo = driver.find_element_by_id("regnum")
DoB = driver.find_element_by_id("dob")
RegNo.send_keys("DB18BCAR02")
DoB.send_keys("01-01-2001")
login = driver.find_element_by_name('sub')
login.click()

print("completed")

driver.close()