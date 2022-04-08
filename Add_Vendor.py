from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

Vendor_Name = "kurdonerze@enayu.com"
Email = "kurdonerze@enayu.com"

browser = webdriver.Chrome("C:\\Users\\codemen\\PycharmProjects\\FirstSelenium\\Driver\\chromedriver.exe")


browser.set_page_load_timeout(40)
browser.get("https://dev.premisehq.co/Home/Login")
browser.find_element_by_name("UserName").send_keys("sqa1")
browser.find_element_by_name("Password").send_keys("123456")
browser.find_element_by_id("LogIn").click()
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/a/div").click()
browser.implicitly_wait(40)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[4]/a").click()
browser.implicitly_wait(40)
browser.find_element_by_id("SearchVendor").send_keys(Vendor_Name)
browser.implicitly_wait(40)
browser.find_element_by_xpath("//div[@id='app']/div/div/div[4]/div/div/div/div[2]/div[2]/div/ul/li/div/b").click()
browser.implicitly_wait(20)
browser.find_element_by_id("AddVendor").click()
browser.find_element_by_id("CompanyName").send_keys(Vendor_Name)
browser.find_element_by_id("ContactName").send_keys(Vendor_Name)
browser.find_element_by_id("GstOrHSt").send_keys(Vendor_Name)
browser.find_element_by_id("Commercial").click()
browser.implicitly_wait(20)

#------------------------------------for select region---------------

browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[1]/div[5]/div/div/span[1]").click()
browser.implicitly_wait(20)

select_region = browser.find_element_by_id("pro")
browser.implicitly_wait(20)
time.sleep(5)
select_region.send_keys(Keys.ARROW_DOWN)
select_region.send_keys(Keys.ARROW_DOWN)
select_region.send_keys(Keys.ARROW_DOWN)
select_region.send_keys(Keys.RETURN)
browser.implicitly_wait(30)


#--------------------------------For Email---------------
browser.find_element_by_id("NewVendoremail").send_keys(Email)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[1]/div[6]/div[1]/div/div[2]/div/textarea").send_keys("TEST")
#------------------------------for select city--------
time.sleep(5)
browser.find_element_by_xpath("//div[@id='app']/div/div/div[4]/div/div/div/div[2]/div/div[6]/div/div/div/div/div/div/span[2]").click()
time.sleep(5)
select_city = browser.find_element_by_id("city")
browser.implicitly_wait(50)
select_city.send_keys("A")
time.sleep(5)
select_city.send_keys(Keys.DOWN,Keys.ENTER)
browser.implicitly_wait(10)
browser.implicitly_wait(4000)
browser.find_element_by_id("submit").click()

time.sleep(30)

