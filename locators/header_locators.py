from selenium.webdriver.common.by import By

# Локатор логотипа самоката
logo_samokat_locator = [By.XPATH, './/img[@alt="Scooter"]']
# Локатор логотипа яндекса
logo_yandex_locator = [By.XPATH, './/img[@alt="Yandex"]']

# Локатор для проверки перехода на страницу яндекса
check_redirect_yandex_locator = [By.ID, 'ya-dist-splashscreen']