from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys


s = Service(r"D:\sel_fish\Downloads\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument('-ignore-certificate-errors')
chrome_options.add_argument('-ignore -ssl-errors')
wd = webdriver.Chrome(service = s, options = chrome_options)
wd.implicitly_wait(10)
wd.get("http://10.2.5.251/a79.htm?wlanuserip=10.4.249.112&wlanacname=NAS&ssid=Ruijie&nasip=10.2.4.1&mac=dc215cadb574&t=wireless-v2-plain&url=http://9.9.9.9/")
wd.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[2]/select/option[3]').click()
element1 = wd.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[2]/form/input[2]')
element1.send_keys("08213158")
element2 = wd.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[2]/form/input[3]')
element2.send_keys("195235\n")
wd.close()
sys.exit()