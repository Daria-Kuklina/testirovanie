from selenium import webdriver 
from selenium.webdriver.common.by import By 

browser=webdriver.Chrome() 
browser.get(' http://localhost:3000/signup') 

login=browser.find_element(by=By.ID, value='login') 
login.send_keys('uaer1') 

password=browser.find_element(by=By.ID, value='password') 
password.send_keys('') 

email=browser.find_element(by=By.ID, value='email') 
email.send_keys('user_1@mail.ru') 

button=browser.find_element(by=By.CSS_SELECTOR, value='#registrbtn') 

button.click()

