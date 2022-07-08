from selenium.webdriver.common.by import By


class MainPageLoc:

    login_loc = (By.CSS_SELECTOR, ".header_user_info")
    basket_empty_loc = (By.XPATH, '//div[@class="shopping_cart"]//span[contains(text(), "(empty)")]')
    dresses_loc = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_category=8&controller=category"]')
    customer_loc = (By.CSS_SELECTOR, '[title="Contact Us"]')
    customer2_loc = (By.CSS_SELECTOR, '.page-heading.bottom-indent')

    button_loc = (By.CSS_SELECTOR, '[title="View my shopping cart"]')
    verify_page_loc = (By.CSS_SELECTOR, '[id="cart_title"]')
