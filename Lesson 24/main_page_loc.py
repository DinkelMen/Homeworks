from selenium.webdriver.common.by import By


class MainPageLoc:
    cart_page_title_loc = (By.CSS_SELECTOR, "[lang='en']>:nth-child(1)>:nth-child(2)")
    cart_empty = (By.CSS_SELECTOR, "ajax_cart_no_product")
    cart_empty_2 = (By.CSS_SELECTOR, ".alert.alert-warning")
    login_page_title_loc = (By.CSS_SELECTOR, "[lang='en']>:nth-child(1)>:nth-child(2)")
    base_page_title_loc = (By.CSS_SELECTOR, "[lang='en']>:nth-child(1)>:nth-child(2)")
    login_loc = (By.CSS_SELECTOR, ".login")
    cart_loc = (By.CSS_SELECTOR, ".shopping_cart>:nth-child(1)")
    submit_login_button = (By.CSS_SELECTOR, "[id='SubmitLogin']")
