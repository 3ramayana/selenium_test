from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.st.com/cas/login?lang=en&service=https%3A%2F%2Fwww.st.com%2Fcontent%2Fst_com%2Fen.html")

form = driver.find_element(By.ID, "fm1")
email = form.find_element(By.ID, "username")
password = form.find_element(By.ID, "password")
email.send_keys("administrator")
password.send_keys("123")

driver.find_element(By.ID, "loginSubmit").click()
