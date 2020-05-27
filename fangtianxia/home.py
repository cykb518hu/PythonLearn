from selenium import webdriver
from time import sleep


chrome_path ='C:\\Dev Tool\\chromedriver_win32\\chromedriver.exe'

chrom_opt = webdriver.ChromeOptions()
prefs={
     'profile.default_content_setting_values': {
        'images': 2,
        'javascript':2
    }
}
#chrom_opt.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrom_opt)

browser.get("https://sh.esf.fang.com/housing/?rfss=1-37080e0ec52386ce00-70")
#browser.get("https://www.gabar.org/membersearchresults.cfm?start=64501&id=0DF19A5B-5056-8BF7-F5A714C0FE3468DF")
list=[]

try:
    page=0
    while page<3:
        members=browser.find_elements_by_xpath("//a[@class='plotTit']")
        for member in members:
            link=member.get_attribute('href')
            #link = link.replace('https://www.gabar.org/MemberSearchDetail.cfm?ID=','')
            da=[member.text,link]
            list.append(da)
        browser.find_element_by_xpath("//a[@class='pageNow']/following-sibling::a[1]").click()
        page=page+1
except:
    print('-----------------------------------------------------------------')
    print(page)
finally:
    print('-----------------------------------------------------------------')
    print(list)
    print('-----------------------------------------------------------------')








 
    