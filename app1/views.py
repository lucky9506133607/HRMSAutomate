from django.shortcuts import render
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
import time

# Create your views here.

def hrms(request):
    gettitle = ''
    if request.POST:
        Valid_user = ['et/amd/189@elsner.com']
        Valid_pass = ['Lucky@123']
        # try:
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-sh-usage")
        driver = webdriver.Chrome(service=Service(executable_path=os.environ.get("CHROMEDRIVER_PATH")), chrome_options=chrome_options)
        time.sleep(6)
        driver.get("https://hrms.orangetechnolab.com/Elsner/Login_Comm1.aspx")
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="txtusename"]').send_keys(Valid_user[0])
        driver.find_element(By.XPATH, '//*[@id="txtpassword"]').send_keys(Valid_pass[0])
        driver.find_element(By.XPATH, '//*[@id="btnlogin"]').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/a').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/aside/div/section/ul/li[1]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[1]/aside/div/section/ul/li[1]/ul/li[3]').click()
        gettitle = driver.title
        driver.quit()
        # except Exception:
            # gettitle = 'something went wrong'
    return render(request, 'index.html', {'key': gettitle})
