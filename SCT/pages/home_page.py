class Home_page:
    def __init__(self, driver):
        # Here lies all the locators of the elements of that particular page (Login page)
        self.driver = driver
        self.url = "https://getpay-qa.finpos.global/sct/bank-portal/#/" 
        self.loginButton = "//button[text()='Login']"
        self.LoginText = "//h6[text()='Login']"
        
    def open_home_page(self):
        # This is method to open the home page
        self.driver.get(self.url)
        wa
        
    def click_login_button(self):
        # This is method to click on the
        self.driver.find_element_by_xpath(self.loginButton).click()
        
    def verify_login_header(self, Value):
        # This is method to verify the login header
        assert self.driver.find_element_by_xpath(self.LoginText).text == Value
        