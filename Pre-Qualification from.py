from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import gspread #for_Google_Excel
from oauth2client.service_account import ServiceAccountCredentials#for_Google_Excel




from selenium.webdriver.chrome.webdriver import WebDriver

browser = webdriver.Chrome("C:\\Users\\codemen\\PycharmProjects\\FirstSelenium\\Driver\\chromedriver.exe")

Link = "https://www.google.com/url?q=https://dev.premisehq.co/VendorCompliance/index.html%23/qform/supplier?n%3Dtrue%26AppKey%3Dcc3fdca374904ae89e3393779805efaf%26Key%3D2018111708394924e59a0b974c95bbcb37436d852989%26id%3Dd441c413234e483c84e2d03a10b03601&sa=D&source=hangouts&ust=1582262791610000&usg=AFQjCNH3BXJirBKf0aUb_31dyuqygCgxfg"
Password = "123456"
Confirm_Password = "123456"
Company_Name = "Test Company"
Company_Address = "Test,test,test,canada"
Phone = "01720448274"
General_Liability = "1250"


browser.set_page_load_timeout(40)
browser.get(Link)
browser.implicitly_wait(30)
browser.implicitly_wait(30)
time.sleep(20)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/input").send_keys(Password)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div/input").send_keys(Confirm_Password)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/input").send_keys(Company_Name)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/input").send_keys(Company_Address)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/div/input").send_keys(Phone)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[3]/div[2]/div[5]/div[1]/div/input").send_keys(Phone)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[4]/div[1]/div/input").send_keys(General_Liability)

#-----------------------------For Date picker First Notification----------------------
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
VC_Dates = ServiceAccountCredentials.from_json_keyfile_name("Test Automation-d80004c7278c.json" , scope)
client = gspread.authorize(VC_Dates)
sheet = client.open("VC_DATE_API_FOR_AUTOMATION").sheet1 # Open the spreadhseet


First_Notification_Cell = sheet.cell(3,2).value#FOR FIRST NOTIFICATION
PWCB_Date_Today = sheet.cell(3,1).value#FOR PWCB NOTIFICATION
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/div/div/div/input").send_keys(First_Notification_Cell)
browser.find_element_by_xpath("//div[@id='app']/div/div/div[4]/div/div/div/div[2]").click()
#---------------------------------FOR FILE UPLOAD---------------------------------------
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[3]/div[4]/div[2]/div/label/input").send_keys("C://Users//codemen//Documents//Nashrif//test help//pdf//insurance_secure - 1.docx")
browser.implicitly_wait(10)
#browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[3]/div[4]/div[3]/div/label/input").send_keys("C://Users//codemen//Documents//Nashrif//test help//pdf//insurance_secure - 1.docx")
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[3]/div[4]/div[4]/div/label/input").send_keys("C://Users//codemen//Documents//Nashrif//test help//pdf//insurance_secure - 2.docx")
#------------------------------------FOR PWCB DATE-----------------------------------------
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[2]/div[2]/div[3]/div[3]/div/div[1]/div/input").send_keys(PWCB_Date_Today)
browser.find_element_by_xpath("//div[@id='InsuranceFrom']/div[3]/div").click()

#---------------------------------------FOR CAPTCHA------------------------

read_captcha = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[5]/div/div/div[2]/span").text
#print(read_captcha)
fields = read_captcha.split("+")
a = fields[0]
b = fields[1]
c = b.split("=")
d = c[0]
captcha = int(a)+int(d)
#print(fields)#For check
#print(c1)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[5]/div/div/div[3]/input").send_keys(captcha)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[4]/div/div/div/div[6]/div/button[2]").click()
time.sleep(40)
browser.quit()
