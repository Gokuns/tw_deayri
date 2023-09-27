from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from keys import username, password
import grammar_checker


def qrt_with_grammar_check(searchStr):
    # Initialize the web driver (for Chrome)
    driver = webdriver.Chrome()

    # URL of Twitter login page
    login_url = 'https://twitter.com/i/flow/login'

    # Navigate to the Twitter login page
    driver.get(login_url)

    time.sleep(5)

    # login_button = driver.find_element(By.CSS_SELECTOR, '.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty')

    username_field = driver.find_element(By.CLASS_NAME, 'r-30o5oe')
    username_field.send_keys(username)
    username_field.send_keys(Keys.ENTER)

    time.sleep(3)

    password_field = driver.find_element(By.CLASS_NAME, 'r-homxoj')
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)

    # Wait for some time to ensure the login is complete
    time.sleep(5)

    # URL of Twitter search results
    search_url = 'https://twitter.com/search?q=' + searchStr + '&f=live'

    # Navigate to the Twitter search page
    driver.get(search_url)

    time.sleep(2)

    # Find tweet elements
    tweet_elements = driver.find_elements(By.XPATH, '//div[contains(@data-testid, "tweet")]')
    retweets = [tweet.find_element(By.XPATH, '//div[contains(@data-testid, "retweet")]') for tweet in tweet_elements]

    tweet_text = tweet_elements[0].text
    retweets[0].click()

    time.sleep(2)

    qrt_button = driver.find_element(By.CSS_SELECTOR, ".css-18t94o4.css-1dbjc4n.r-1loqt21.r-18u37iz.r-1ny4l3l")
    qrt_button.click()

    time.sleep(2)

    qrt_text_field = driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")


    res = grammar_checker.check_de(tweet_text)
    qrt_text_field.send_keys(res)

    time.sleep(30)

    post_btn = driver.find_element(By.CSS_SELECTOR, ".css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf")

    time.sleep(5)

    # Close the web driver
    driver.quit()