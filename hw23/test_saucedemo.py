from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Safari()
browser.implicitly_wait(5)
browser.set_window_size(1024, 768)


try:
    browser.get("https://www.saucedemo.com/")

    # Login
    username_input = browser.find_element(By.XPATH, '//input[@data-test="username"]')
    username_input.clear()
    username_input.send_keys("standard_user")

    password_input = browser.find_element(By.XPATH, '//input[@data-test="password"]')
    password_input.clear()
    password_input.send_keys("secret_sauce")

    login_button = browser.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # Add to cart
    add_backpack_button = browser.find_element(By.XPATH, '//button[@data-test='
                                                         '"add-to-cart-sauce-labs-backpack"]')
    add_backpack_button.click()

    add_fleece_jacket_button = browser.find_element(By.XPATH, '//button[@data-test='
                                                              '"add-to-cart-sauce-labs-fleece-jacket"]')
    add_fleece_jacket_button.click()

    # Go to Cart
    cart_button = browser.find_element(By.XPATH, '//a[contains(@class, "shopping_cart_link")]')
    cart_button.click()

    # Go to Checkout info
    checkout_button = browser.find_element(By.XPATH, '//button[@data-test="checkout"]')
    checkout_button.click()

    # Checkout information filling in
    first_name_input = browser.find_element(By.XPATH, '//input[@data-test="firstName"]')
    first_name_input.clear()
    first_name_input.send_keys("Elizaveta")

    last_name_input = browser.find_element(By.XPATH, '//input[@data-test="lastName"]')
    last_name_input.clear()
    last_name_input.send_keys("Nikolaeva")

    postal_code_input = browser.find_element(By.XPATH, '//input[@data-test="postalCode"]')
    postal_code_input.clear()
    postal_code_input.send_keys("002007")

    # Go to checkout overview
    continue_button = browser.find_element(By.XPATH, '//input[@data-test="continue"]')
    continue_button.click()

    # Finish checkout
    finish_button = browser.find_element(By.XPATH, '//button[@data-test="finish"]')
    finish_button.click()

    # Success check
    right_url = "https://www.saucedemo.com/checkout-complete.html"
    current_url = browser.current_url

    assert current_url == right_url, (f"URL: {right_url} was expected, "
                                      f"but user was redirected to URL: {current_url}")
    success_message = browser.find_element(
        By.XPATH,
        '//h2[contains(text(), "Thank you for your order!")]'
    )
    assert "Thank you for your order!" in success_message.text

    time.sleep(5)

finally:
    browser.quit()
