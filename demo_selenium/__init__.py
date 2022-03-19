# import time

from selenium import webdriver
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
# # #
# driver.get('http://www.google.com/')
# driver.get('http://facebook.com/')
# from time import sleep
#
# #
# # from selenium.webdriver import Chrome
# # driver = Chrome('chromedriver')
# # # driver.get('https://www.actitime.com/demo-request/')
# # sleep(2)
# # # driver.minimize_window()
# # sleep(2)
# # # driver.maximize_window()
# # # url= driver.title
# # # print(url)
# # # print(driver.current_url)
# # # driver.find_element_by_xpath("//input[@id='first-name']").send_keys('nizam')
# # # driver.find_elements_by_link_text("Enter Mobile number")
# # # driver.send_keys(7758888772)
# # # driver.find_element_by_xpath("//a[@class='button header__button']").click()
# # # driver.find_element_by_xpath("file:///C:/Users/asd/Downloads/demo.html")
# # # links = driver.find_elements_by_xpath("//a")
# #
# # # for item in links:
# # #     print(item)
# # # driver.get("file:///C:/Users/asd/Downloads/demo.html")
# # driver.get("https://www.python.o rg/downloads/")
# # c = driver.find_elements_by_xpath("//a[text()='Python 3.9.9']/../..//a[text()='Release Notes']")
# # for item in c:
# #     item.click()
# from selenium.webdriver.support.select import Select
# driver.get("http://demowebshop.tricentis.com/")
# mul_car = driver.find_element_by_id("multiplecars")
# select = Select(mul_car)
# print(select.is_multiple)
# x = driver.find_elements_by_xpath("//a[text()='$25 Virtual Gift Card']/../..//input [@value='Add to cart']")
# for i in x:
#     i.click()
# #
# # driver.get("file:///C:/Users/asd/Desktop/Python%20notes/New%20folder/demo.html")
# # companies = ['AAPL','AA','MSFT','FB']
# # for company in companies:
# #     _xpath  = f"//td[text()='{company}']/..//td[@class='price']"
# #     share_price = float(driver.find_element_by_xpath(_xpath).text)
# #     # print(f'{company} : {share_price}')
# # # driver.get("https://www.monsterindia.com/trex/")
# # # driver.find_elements_by_id("SE_home_autocomplete").send_keys("Python")
# #
#
# driver.get("https://dotpe.in/landing-ecomm.html?&utm_source=Google&utm_medium=CPC&utm_campaign=Ecommerce_Search_EM")
# driver.title
# driver.maximize_window()
# driver.find_element_by_id("landing-form-show-update").click()
# driver.find_element_by_id("name").send_keys('nizam')
# driver.get("http://demowebshop.tricentis.com/")
# links = driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")
# for link in links:
#     print(link.text)




import time
from    time    import sleep
#
# driver.get("http://demowebshop.tricentis.com/")
# links = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//a")
# p = []
# for link in links:
#     sleep(1)
#     p.append(link.text)
#
# print(p)




# 1select by visible text
# 2by index
# 3by value
# 4diselct by visible text
# 5by value
# 6by index
#
# 1options
# 2first.selected.option
# 3all selected option
# 4diselect all

# absolute xpath
# relative xpath ///mostly used
# browser action
# locators
# selenium arcitecture
# link text
# partial linktext
# findelement and find elements
# click,sendkeys,text,get attribute
# select class
#
# driver.get("http://demowebshop.tricentis.com/")
# driver.find_element_by_xpath("//ul[@class='poll-options']//input[@id='pollanswers-2']").click()
#




# STale element Exception- once we select the element page get refreshed and  when we again select the eleemnt from that old page we get this exception
# no such element exception-
# unexpected tag name exception- which you pass a link,button or text,if that is nopt present in the list then this exception shows
# how we check we select multiple or not = is_  multiple = true or false
# timeout exception
#element not interactable exception- when an input not accpeting sendkeys



# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# wait = WebDriverWait(driver,10)
# driver.get("file:///C:/Users/asd/Desktop/Python%20notes/New%20folder/demo.html")
# v = visibility_of_element_located(("firstname","lastname"))
# wait.until(v)
# driver.find_element_by_id("firstname").send_keys("Nizam")
# driver.find_element_by_id("lastname").sen_keys("Mujawar")
# driver.find_element_by_id("submit").click()
# Visibility of element located
# __call__+
# return webelement if the element is loaded in the DOM and element is visible on the web page
# false



#
#/////////////////////////////////////////////////////////////////////////////////////////////////////
from selenium.webdriver.support.ui import Select
# driver.get("file:///C:/Users/asd/Desktop/Python%20notes/New%20folder/demo.html")
# element  = driver.find_element_by_xpath("//select[@id='multiple_cars']")
# drp= Select(element)
# drp.select_by_visible_text('BMW')
# drp.select_by_visible_text('Audi')
# drp.deselect_all()


# ///////////////////////////////////////////////////////////////////////////////////////////////////////
from selenium.webdriver.remote.webelement import WebElement
# driver.get("http://demowebshop.tricentis.com/")
# sleep(3)
#
# driver.find_element_by_link_text("Twitter").click()
# sleep(3)
# ids =driver.window_handles
# # switchiong to chiild id
# driver.switch_to.window(ids[1])
# sleep(5)
# driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys('hello')

# ///////////////////////////////////////////////////////////////////////////////////////////////
# driver.get("file:///C:/Users/asd/Desktop/Python%20notes/New%20folder/demo.html")
# driver.find_elements_by_xpath("file:///C:/Users/asd/Desktop/Python%20notes/New%20folder/demo.html")







#//////////////////////////////////////////////////////////////////////////////////////////////////////
# from selenium.common.exceptions import NoSuchElementException
# driver.get("https://www.goibibo.com/")
# sleep(3)
# driver.find_element_by_xpath("//span[@class='sc-kfPuZi dprjVP fswDownArrow']").click()
# _mon_year = "July 2022"
# _day = "15"
# def select_date(_mon_year,_day):
#     for _ in range(12):
#         try:
#             driver.find_element_by_xpath(f"//div[text()='{_mon_year}']/../..//p[text()='{_day}']").click()
#             sleep(4)
#             break
#         except NoSuchElementException:
#             driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
#             sleep(2)
#             continue
# select_date("February 2023", "28")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
# driver.get("https://www.monsterindia.com/")
# sleep(4)
# driver.find_element_by_xpath("//a[@class='btn block resume-btn btn-orange mt20']").click()
# sleep(3)
# driver.find_element_by_xpath("(//input[@id='file-upload'])[2]").send_keys(R"C:\Users\asd\Desktop\Python_notes\class.pdf")
# sleep(2)
# driver.find_element_by_xpath("(//input[@value='Submit'])[1]").click()
# //////////////////////////////////////////////////////////////////////////////////////////////////////////
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains



class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self,driver):
        result = super().__call__(driver)
        if isinstance(result,WebElement):
            return result.is_enabled()
        else:
            return False

def wait(func):
    def wrapper(*args,**kwargs):
        locator = args[0]
        wait = WebDriverWait(driver , 20)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args,**kwargs)

@wait
def click_element(locator):
    """
    clicks on the element
    return wrapper

    """
    driver.find_element(*locator).click()       #finf_element(*linktext,*register )

@wait
def enter_text(locator,value):
    """enters something inside the text box"""
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(value)

@wait
def select_item(locator,item):
    """select same item from the list"""
    element = driver.find_element(*locator)
    s = Select(element)
    if isinstance(item,str):
        s.select_by_visisble_text(item)
    elif isinstance(item,int):
        s.select_by_index(item)
    else:
        raise TypeError


driver.get("https://demowebshop.tricentis.com/")

click_element(("link text", "Register"))
click_element(("id","gender-male"))







