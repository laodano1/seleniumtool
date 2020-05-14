from selenium import webdriver
from colorama import Fore, Back, Style
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJrdWJvYXJkLXVzZXItdG9rZW4tZndsc2QiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoia3Vib2FyZC11c2VyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiNzdjZTE5NmYtMjljYy00NWExLWI4NGQtNzM1Zjc0NGM0ZDJmIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmt1Ym9hcmQtdXNlciJ9.k3A7nD3KRKVzBuMMJEKRzUE2PUUA3-lkJgB1-xip2qsto-Ohjx_XlAjjeNcaopD3NgVrTBGh2PpF6gGrdr_OEYhcpFzja_E-frWyIKnH8UcIWs486LMECM-BosXd1sqhsBQphTWQf-5EDdWDMMQbzlQko5yWGqbHwm5SXPlXt3waKZnRGGijB8JeQ0wiVj-aP2FHLclxoc7hMDp1vVoBSljYlCjzpGxewgrweqhBQYjUELTgvTlAGRXzC0qOj25yLrF8v1EOMkNBvYNGzPI1QFmsiv2OmnnTGGLRoM8cqPLusZyfjsdDXvZDL0E2bVL7MSi9e2q_7QLBn6kfWmDjXw"

# print(help('modules'))
# print(help('os'))
# print(Fore.RED + 'some red text')
# print(Fore.GREEN + 'and with a green background')
# print(Fore.GREEN + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')


############
# for firefox
############
def config_firefox_driver():
    firefox_options = FirefoxOptions()
    # chrome_options.add_argument("--headless")
    firefox_driver = webdriver.Firefox(options=firefox_options)
    return chromeDriver


############
# for chrome
############
def config_chrome_driver():
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(options=chrome_options)
    return chrome_driver


############
# move to given element and click
############
def move_and_click(driver, btn):
    ActionChains(driver).move_to_element(btn).perform()
    btn.click()


############
def login_to_page(driver, link, tk):
    driver.get(link)
    chromeDriver.save_screenshot("1.png")
    driver.find_element_by_tag_name("textarea").get_attribute("placeholder")
    driver.find_element_by_tag_name("textarea").clear()
    driver.find_element_by_tag_name("textarea").send_keys(tk)
    move_and_click(driver, driver.find_element_by_tag_name("button"))
    # driver.find_element_by_tag_name("button").click()
    chromeDriver.save_screenshot("2.png")


# enter namespace
def get_namespace_btn(driver, btns):
    for i in range(len(btns)):
        if i == len(btns) - 2:
            d = btns[i].find_element_by_class_name("ih-item.square.effect11.left_to_right")
            print("  class 2: ", d.get_attribute("class"))

            # chromeDriver.implicitly_wait(2000)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'bg'))
            )

            print("  current_url 3: " + driver.current_url)
            driver.save_screenshot("3.png")
            return d
        else:
            continue


# enter import workload
def get_import_workload_btn(slt):
    # btns = slt.find_element_by_tag_name("div").find_elements_by_tag_name("span")  #.find_elements_by_tag_name("button")
    btns = slt.find_elements_by_tag_name("button")
    for btn in btns:
        # if btn.get_attribute("style") ==  "display: inline-block; text-align: left; line-height: 12px;":
        # print("  2-- btn text: " + btn.text)
        if btn.text == "导入工作负载":
            print("  1-- btn text: " + btn.text)
            return btn
        else:
            print("  2-- btn text: " + btn.text)


############
chromeDriver = config_chrome_driver()
# chromeDriver = config_firefox_driver()
login_to_page(chromeDriver, "http://10.0.0.200:32567/login", token)
print("title: " + chromeDriver.title)
print("current_url 1: " + chromeDriver.current_url)

# assert "Kuboard" in chromeDriver.title
print("current_url 2: " + chromeDriver.current_url)

# chromeDriver.implicitly_wait(2)
# WebDriverWait(chromeDriver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, 'namespaceWrapperBody'))
# )

###
# find namespace and enter
div_list = chromeDriver.find_element_by_class_name("namespaceWrapperBody").find_elements_by_class_name("namespace")
ns_btn = get_namespace_btn(chromeDriver, div_list)
move_and_click(chromeDriver, ns_btn)

# enter import workload
chromeDriver.get("http://10.0.0.200:32567/namespace/wanda-games")
# chromeDriver.implicitly_wait(2)
WebDriverWait(chromeDriver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'slot'))
)
ipt_btn = get_import_workload_btn(chromeDriver.find_element_by_class_name("slot"))
move_and_click(chromeDriver, ipt_btn)
chromeDriver.save_screenshot("4.png")

# click upload button
# uplder = chromeDriver.find_element_by_class_name("el-upload-dragger")
# print("  --- class 5: " + uplder.get_attribute("class"))
# ActionChains(chromeDriver).move_to_element(uplder).perform()
# uplder.click()
# uplder.send_keys("C:\\Users\\kinge\\Downloads\\kuboard_wanda-games_2020_04_16_17_55_34.yaml")

# select uploaded file


# click next step button








