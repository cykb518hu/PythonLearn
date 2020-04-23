from selenium import webdriver
from time import sleep
import ppp

# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
chrome_path ='C:\\Dev Tool\\chromedriver_win32\\chromedriver.exe'

chrom_opt = webdriver.ChromeOptions()
#prefs = { "profile.managed_default_content_settings.images": 2 }
#chrom_opt.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrom_opt)

#县长信箱
browser.get("http://www.njwlwz.gov.cn/Mail/Allemail.aspx?MailBox=%C7%F8%CF%D8%D0%C5%CF%E4&Manager=%D7%CA%D6%D0%CF%D8%D5%FE%B8%AE")
list=[]

while int(browser.find_element_by_id("ctl00_ContentPlaceHolder1_SmailSearch1_GridView1_ctl23_LabelCurrentPage").text)<5:
    table=browser.find_element_by_id("ctl00_ContentPlaceHolder1_SmailSearch1_GridView1")
    trs=table.find_elements_by_tag_name("tr")
    first=0
    for tr in trs:
        first=first+1
        if first==1:
            continue
        if first>21:
            break
        tds=tr.find_elements_by_tag_name("td")
        da=[tds[0].text,tds[1].text,tds[3].text,tds[4].text]
        list.append(da)
    browser.find_element_by_id("ctl00_ContentPlaceHolder1_SmailSearch1_GridView1_ctl23_LinkButtonNextPage").click()
print(list)







 
    