from selenium import webdriver

browser = webdriver.Chrome('/Users/ReginaGurung/Downloads/chromedriver')

# Edith has heard about a cool new online to-do app. Shes goes to check out its homepage.
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists.
assert 'To-Do' in browser.title, "Browser title was " + browser.title

# She is invited to enter a to-do item straight away.
# She types "Buy peacock feathers" into a text box (Edith's hobby is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list
# Edith wonders whether the site will remember her list. Then she sees that the site has generated a unique url for her.

# She visits that url - her to-do list is still there.
# Satistified, she goes back to sleep.

browser.quit()
