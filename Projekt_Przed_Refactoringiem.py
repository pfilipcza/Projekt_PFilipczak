import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.pkn.pl/")
driver.maximize_window()

# Krok nr 1 - "Szukaj"
search = driver.find_element("id", "search-click")
search.click()

# Krok nr 2 - "Wyszukaj norme"
search_standard = driver.find_element("xpath","//*[@id='block-formblock']/nav/ul/li[1]/a")
search_standard.click()

#Krok nr 3 - Przejscie na drugą stronę:
print("Aktualne okno:", driver.title)

currentWindow = driver.current_window_handle
windowsNames = driver.window_handles

for window in windowsNames:
    if window != currentWindow:
        driver.switch_to.window(window)

print("Aktualne okno po przełączeniu:", driver.title)

# Krok nr 4 - Akceptacja ciasteczek

cookie = driver.find_element("id", "_appcookiepolicyinfo_WAR_p4scommoncookiepolicyinfoportlet_accept")
cookie.click()

# Krok 5 - wybieramy status normy
standard_status = driver.find_element("id", "_searchstandards_WAR_p4scustomerpknzwnelsearchstandardsportlet_standardActual")
standard_status.click()
standard_status.send_keys("aktualne")
standard_status.click()

# Krok nr 6 - Wprowadzamy nr normy
standard_number = driver.find_element("id", "_searchstandards_WAR_p4scustomerpknzwnelsearchstandardsportlet_standardNumber")
standard_number.send_keys("PN-EN 1401-1")
standard_number.send_keys(Keys.ENTER)

# Krok nr 7 - Wynik wyszukiwania
standards = driver.find_elements("xpath", "//a[contains(@class, 'p4s-search-results-link')]")
standards_names = [standard.get_attribute("textContent") for standard in standards]
standards_names_search = standards_names[0]
print(standards_names_search)



time.sleep(600)
driver.quit()
