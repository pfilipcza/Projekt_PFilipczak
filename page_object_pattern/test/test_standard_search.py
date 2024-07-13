import tkinter as tk
from selenium import webdriver
import pytest
import time
from page_object_pattern.pages.main_page_pkn import PKN_Page
from page_object_pattern.pages.search_standard_page import Wiedza_PKN
from page_object_pattern.pages.standard_info import Standard_summary

class StandardGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Przemysław Filipczak - Praca Dyplomowa")
        self.window_width = 500
        self.window_height = 300
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)
        self.root.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')
        self.root.resizable(False, False)
        self.target_info = tk.Label(text="Wyszukiwarka aktualnej Normy PN-EN 1401-1")
        self.target_info.pack()
        self.exit_button = tk.Button(text="PN-EN 1401-1 - Sprawdź aktualną wersję", command=self.root.quit)
        self.exit_button.place(x=100, y=50, height=50, width=300)
        self.root.mainloop()
class TestStandardSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        time.sleep(10)
        self.driver.quit()


    def test_standard_search(self, setup):
        self.driver.get("https://www.pkn.pl/")
        main_view_page = PKN_Page(self.driver)
        main_view_page.search()
        main_view_page.search_button()
        main_view_page.info_actual_page()
        main_view_page.change_page()
        second_page = Wiedza_PKN(self.driver)
        second_page.cookie_accept()
        second_page.standard_status()
        second_page.enter_standard_no()
        summary = Standard_summary(self.driver)
        summary.get_standard_name()

StandardGui()















