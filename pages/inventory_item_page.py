from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
