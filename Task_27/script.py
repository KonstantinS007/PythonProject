import selenium
import pickle
with open('my_cookies.txt', 'wb') as cookies:
    pickle.dump(selenium.get_cookies(), cookies)
