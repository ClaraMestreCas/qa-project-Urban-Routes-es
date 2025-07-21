#Localizadores y métodos necesarios
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    pedir_taxi = (By.CSS_SELECTOR, ".button.round")
    comfort_tariff = (By.CSS_SELECTOR, 'img[alt="Comfort"]')
    phone_button = (By.CSS_SELECTOR, "div.np-button")
    phone_button2 = (By.CSS_SELECTOR, "div.np-input")
    phone_input = (By.CSS_SELECTOR, "div.input-container.error")
    submit_phone_button = (By.CSS_SELECTOR, '.smart-button-main')
    card_input = (By.ID, 'number')
    card_cvv_input = (By.ID, 'code')
    link_card_button = (By.ID, 'link')
    message_input = (By.ID, 'comment')
    blanket_checkbox = (By.ID, 'blanket')
    tissues_checkbox = (By.ID, 'towels')
    ice_cream_counter = (By.ID, 'ice-cream')
    order_button = (By.ID, 'order')
    modal_searching = (By.CLASS_NAME, 'searching-for-taxi-modal')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def set_route(self, from_address, to_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(EC.visibility_of_element_located(self.from_field)).send_keys(from_address)
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def select_pedir_taxi(self):
        self.wait.until(EC.element_to_be_clickable(self.pedir_taxi)).click()

    def select_tariff_comfort(self):
        self.wait.until(EC.element_to_be_clickable(self.comfort_tariff)).click()

    def enter_phone_number(self, phone_number):
        self.wait.until(EC.element_to_be_clickable(self.phone_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.phone_button2)).click()
        self.wait.until(EC.visibility_of_element_located(self.phone_input)).send_keys(phone_number)

    def add_card(self, number, cvv):
        self.driver.find_element(*self.card_input).send_keys(number)
        cvv_field = self.driver.find_element(*self.card_cvv_input)
        cvv_field.send_keys(cvv)
        # Simular TAB para perder enfoque (activar botón)
        cvv_field.send_keys(Keys.TAB)
        self.driver.find_element(*self.link_card_button).click()

    def enter_confirmation_code(self, code):
        confirmation_input = self.wait.until(EC.presence_of_element_located((By.ID, 'code-confirm')))
        confirmation_input.send_keys(code)

    def write_message(self, message):
        self.driver.find_element(*self.message_input).send_keys(message)

    def request_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_checkbox).click()
        self.driver.find_element(*self.tissues_checkbox).click()

    def add_ice_cream(self, count=2):
        counter = self.driver.find_element(*self.ice_cream_counter)
        for _ in range(count):
            counter.send_keys(Keys.ARROW_UP)

    def order_taxi(self):
        self.driver.find_element(*self.order_button).click()

    def is_searching_modal_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.modal_searching)) is not None