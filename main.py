from selenium import webdriver

# firefoxdriver = webdriver.Firefox()
# firefoxdriver.get("https://www.bing.com")
# driver = webdriver.Ie()        # Internet Explorer浏览器
# driver = webdriver.Edge()      # Edge浏览器
# driver = webdriver.Opera()     # Opera浏览器
# driver = webdriver.PhantomJS()   # PhantomJS

chromeDriver = webdriver.Chrome()
chromeDriver.get("https://www.bing.com")
st = chromeDriver.find_element_by_id("bgDiv").get_attribute("style")
tt = chromeDriver.title

# find element and input value to input box
chromeDriver.find_element_by_class_name("b_searchbox").send_keys("aaa")
# click button
chromeDriver.find_element_by_id("sb_go_par").click()

print(st)
print(tt)





