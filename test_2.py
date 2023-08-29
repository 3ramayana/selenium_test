from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://smaaveros.sch.id:2083/")

username = driver.find_element(By.ID, "user")
password = driver.find_element(By.ID, "pass")
username.send_keys('smaavero')
password.send_keys('2015BB2015')

driver.find_element(By.ID, "login_submit").click()
time.sleep(3)

# On dashboard cpanel
original_window = driver.current_window_handle
driver.find_element(By.ID, "item_php_my_admin").click()
time.sleep(3)

# On new tab dashboard phpMyAdmin   
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

time.sleep(3)
driver.find_element(By.LINK_TEXT, "smaavero_nodemcu").click()

time.sleep(3)
driver.find_element(By.LINK_TEXT, "tabel_sensor").click()
