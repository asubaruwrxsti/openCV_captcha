from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


import configparser
config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

cfg = config['DEFAULT']

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get(cfg['url'])
print('mPower present in title') if ("mPower" in driver.title) else input('mPower not present in title, continue?')

username = driver.find_element(By.NAME, "j_username")
username.send_keys(cfg['username'])

password = driver.find_element(By.NAME, "j_password")
password.send_keys(cfg['password'])

captcha = driver.find_element(By.ID, 'image')
captcha.screenshot('screenshot.png')

#im = cv2.imread('public\scrapper\screenshot.png')

key =  input("Enter captcha: ")

captcha_input = driver.find_element(By.NAME, "WordVerification")
captcha_input.send_keys(key)

driver.find_element(By.NAME, "Submit").click()

########### has filled and solved the captcha ############

client_code = Select(driver.find_element(By.NAME, "scnum1")) # finds the selector
client_code.select_by_visible_text(cfg['CLIENT_ID']) # selects the client_code from the selector
driver.find_element(By.XPATH, "/html/body/div[5]/div/center/table/tbody/tr[4]/td/table/tbody/tr/td/form/table/tbody/tr[3]/td/table/tbody/tr/td[2]/input").click() # submit

########## has found and submitted the client code ###########

bils_table = driver.find_element(By.XPATH, "/html/body/div[5]/div/form/center/table[2]") # finds table
rows = bils_table.find_elements(By.TAG_NAME, "tr") # finds rows

for row in rows: # iterates rows
    month = row.find_elements(By.TAG_NAME, "td")[1] # finds columns
    price = row.find_elements(By.TAG_NAME, "td")[4]
    print ("{}: {}".format(month.text, price.text)) # prints columns

driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[5]/a').click # logout
driver.quit

