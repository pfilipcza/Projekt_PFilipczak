
class PKN_Page:
    def __init__(self, driver):
        self.driver = driver
        self.search_id = "search-click"
        self.search_button_xpath = "//*[@id='block-formblock']/nav/ul/li[1]/a"

    def search(self):
        self.driver.find_element("id", self.search_id).click()

    def search_button (self):
        self.driver.find_element("xpath", self.search_button_xpath).click()

    def info_actual_page (self):
        print("Aktualne okno:", self.driver.title)

    def change_page (self):
        currentWindow = self.driver.current_window_handle
        windowsNames = self.driver.window_handles
        for window in windowsNames:
            if window != currentWindow:
                self.driver.switch_to.window(window)

        print("Aktualne okno po przełączeniu:", self.driver.title)

