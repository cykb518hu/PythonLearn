from selenium import webdriver


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

browser.get("https://www.zeekbeek.com/sbm")

file = open("C:\\IIS\\scrape data\\data\\zeekbeek\\all Ids.txt") 
page =0
while page<10:
    userid = file.readline()
    url="https://www.zeekbeek.com/sbm" #"http://www.zeekbeek.com/vcard.ashx?userId=" + userid
    js = 'window.open("'+url+'");'
    print(js)
    browser.execute_script(js)
    page=page+1
file.close()