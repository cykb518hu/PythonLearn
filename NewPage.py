from selenium import webdriver
from time import sleep
class NewPage():
    def next_page(browser,list):
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
            data[tds[0].text + tds[1].text + tds[3].text+ tds[4].text]
            list.append(data)
        print(list)



