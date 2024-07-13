class Standard_summary:
    def __init__(self, driver):
        self.driver = driver
        self.standard_info_id = "//a[contains(@class, 'p4s-search-results-link')]"

    def get_standard_name(self):
        standards = self.driver.find_elements("xpath", self.standard_info_id)
        standards_names = [standard.get_attribute("textContent") for standard in standards]
        standards_names_search = standards_names[0]
        print(standards_names_search)
        return standards_names_search