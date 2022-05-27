import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
d = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
webpage = "https://www.linkedin.com/company/the-coca-cola-company/about/"
d.get(webpage)
username=input("Enter your Linkedn Username: ")
psword= input("Enter your Linkedn Password: ")

user=d.find_element_by_id('username')
user.send_keys(username)
time.sleep(3)
password=d.find_element_by_id('password')
password.send_keys(psword)
time.sleep(3)
login=d.find_element_by_class_name("login__form_action_container ")
login.click()
verify=d.find_element_by_xpath("//input[@class='form__input--text input_verification_pin']")
print("A verification code was sent to your mail, Enter it below.")
x=input(" Enter Verification Code: ")
verify.send_keys(x)
d.find_element_by_xpath("//button[@class='form__submit form__submit--stretch']").click()
WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//dl[@class='overflow-hidden']")))
texts=d.find_element_by_xpath("//dl[@class='overflow-hidden']").text
print("COMPANY INFORMATION")
print("===========================================================================")
print(texts)

