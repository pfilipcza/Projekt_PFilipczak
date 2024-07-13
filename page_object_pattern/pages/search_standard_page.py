from selenium.webdriver.common.keys import Keys
class Wiedza_PKN:
    def __init__(self, driver):
        self.driver = driver
        self.cookie_id = "_appcookiepolicyinfo_WAR_p4scommoncookiepolicyinfoportlet_accept"
        self.standard_status_id = "_searchstandards_WAR_p4scustomerpknzwnelsearchstandardsportlet_standardActual"
        self.standard_no_id = "_searchstandards_WAR_p4scustomerpknzwnelsearchstandardsportlet_standardNumber"


    def cookie_accept(self):
        self.driver.find_element("id", self.cookie_id).click()
    def standard_status(self):
        self.driver.find_element("id", self.standard_status_id).click()
        self.driver.find_element("id", self.standard_status_id).send_keys("aktualne")
        self.driver.find_element("id", self.standard_status_id).click()
    def enter_standard_no(self):
        self.driver.find_element("id", self.standard_no_id).click()
        self.driver.find_element("id", self.standard_no_id).send_keys("PN-EN 1401-1")
        self.driver.find_element("id", self.standard_no_id).send_keys(Keys.ENTER)








