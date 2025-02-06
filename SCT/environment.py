from selenium import webdriver

def before_scenario(context, scenario):
    # Runs the browser before each scenario
    context.driver = webdriver.Chrome()
    
def after_scenario(context, scenario):
    # Quits the browser after each scenario
    context.driver.quit()