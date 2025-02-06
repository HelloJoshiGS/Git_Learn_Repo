from selenium import webdriver
from behave import given, when, then
from pages.home_page import Home_page

@given('I open the Login page')
def step_open_Login_page(context):
    context.driver = webdriver.Chrome()
    context.page = Home_page(context.driver)
    context.page.open_home_page()    

@when('I click on the "Login" button')
def step_click_on_the_Login_button(context):
    context.page.click_login_button()
    
@then('I should see the {Value}')
def step_see_the_Login(context, Value):
    context.page.verify_login_header(Value)
    context.driver.quit()
    
    