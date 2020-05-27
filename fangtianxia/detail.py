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

browser.get("https://huatangmingdiqt.fang.com/")
list=[]

category=browser.find_elements_by_xpath("//div[@class='Rinfolist']/ul/li")
for li in category:
    text=li.text
    list.append(text)

#tabs=browser.find_elements_by_xpath("//div[@id='typeTab']/span")
div=browser.find_element_by_xpath('//div[@class="mapbox"]')

js4 = "arguments[0].scrollIntoView();" 
browser.execute_script(js4, div)  



iframe = browser.find_element_by_xpath("//iframe[@id='iframe_map']")
browser.switch_to_frame(iframe)


spans=browser.find_elements_by_xpath("//div[@id='typeTab']/span")
for span in spans:
    span.click()
    sleep(5)
    tabsText=span.text
    details=browser.find_elements_by_xpath("//div[@class='hx1']/ul/li")
    for de in details:
        detailsText=tabsText+"--"+de.text
        list.append(detailsText)

print(list)








 
    