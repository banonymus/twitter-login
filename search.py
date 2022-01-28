#import  #selenium.webdriver as webdriver
#import selenium.webdriver as webdriver
import from selenium.webdriver.common.by import By



def get_results(search_term):
    url = 'https://www.skroutz.gr/'
    browser = webdriver.firefox
    browser.get(url)
    search_box= browser.find_elements(By.ID,"query")
    search_box.send_keys(search_term)
    search_box.sumbmit()
    try:
        links = browser.find_element(By.XPATH,"//ol[@class='web-regular-results']//h3///a")

        #element = driver.find_element(By.XPATH, "element_xpath")
    except:
        links= browser.find_element(By.XPATH,"//h3///a")
        results = []
        for link in links:
            href = link.get_attribute("href")
            print(href)
            results.append(href)
            browser.close()
            return results

get_results('hp')