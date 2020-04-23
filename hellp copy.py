from selenium import webdriver
from time import sleep
import ppp


chrome_path ='C:\\Dev Tool\\chromedriver_win32\\chromedriver.exe'

chrom_opt = webdriver.ChromeOptions()
prefs={
     'profile.default_content_setting_values': {
        'images': 2,
        'javascript':2
    }
}
chrom_opt.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrom_opt)

browser.get("https://www.gabar.org/membersearchresults.cfm")
browser.get("https://www.gabar.org/membersearchresults.cfm?start=64501&id=0DF19A5B-5056-8BF7-F5A714C0FE3468DF")
list=[]

try:
    page=0
    while page<3:
        members=browser.find_elements_by_xpath("//a[contains(@href,'MemberSearchDetail.cfm?ID=')]")
        for member in members:
            link=member.get_attribute('href')
            link = link.replace('https://www.gabar.org/MemberSearchDetail.cfm?ID=','')
            list.append(link)
        browser.find_elements_by_xpath("//a[@class='page-link' and @aria-label='Next']")[0].click()
        page=page+1
except expression as identifier:
    print('-----------------------------------------------------------------')
    print(page)
finally:
    print('-----------------------------------------------------------------')
    print(list)
    print('-----------------------------------------------------------------')








 
    