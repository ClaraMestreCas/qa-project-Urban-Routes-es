#Localizadores y métodos necesarios
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    pedir_taxi = (By.CSS_SELECTOR, ".button.round")
    comfort_tariff = (By.CSS_SELECTOR, 'img[alt="Comfort"]')
    phone_button = (By.CSS_SELECTOR, "div.np-button")
    phone_button2 = (By.CSS_SELECTOR, "div.np-input")
    phone_input = (By.ID, "phone")
    next_button = (By.CSS_SELECTOR, "button.button.full")
    boton_confirmar = (By.XPATH, "//*[text() = 'Confirmar']")
    button_metodo_pago = (By.XPATH, "(//*[text() = 'Método de pago'])[2]")
    boton_agregar_tarjeta = (By.XPATH, '//img[@alt="plus"]')
    sms_code = (By.ID, "code")
    submit_phone_button = (By.CSS_SELECTOR, '.smart-button-main')
    card_input = (By.ID, 'number')
    card_cvv_input = (By.CSS_SELECTOR, ".card-code-input > input")
    link_card_button = (By.XPATH, "//*[text() = 'Agregar']")
    x_cerrar = (By.XPATH, "//div[text() = 'Método de pago']/preceding-sibling::button")
    message_input = (By.ID, 'comment')
    blanket_and_tissues_checkbox = (By.CSS_SELECTOR, '.slider')
    ice_cream_counter = (By.XPATH, "(//div[@class='counter-plus'])[1]")
    button_order_taxi = (By.XPATH, "(//*[text() = 'Pedir un taxi'])[2]")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    #1ok
    def set_route(self, from_address, to_address):
        self.wait.until(EC.visibility_of_element_located(self.from_field)).send_keys(from_address)
        self.driver.find_element(*self.to_field).send_keys(to_address)
    def get_from_adress(self):
        return self.wait.until(EC.visibility_of_element_located(self.from_field)).get_property("value")
    def get_to_adress(self):
        return self.wait.until(EC.visibility_of_element_located(self.to_field)).get_property("value")

    #2ok
    def select_pedir_taxi(self):
        self.wait.until(EC.element_to_be_clickable(self.pedir_taxi)).click()
    def is_select_taxi_enabled(self):
        return self.wait.until(EC.element_to_be_clickable(self.pedir_taxi)).is_enabled()
    def select_tariff_comfort(self):
        self.wait.until(EC.element_to_be_clickable(self.comfort_tariff)).click()

    #3ok
    def enter_phone_number(self, phone_number):
        self.wait.until(EC.element_to_be_clickable(self.phone_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.phone_button2)).click()
        self.wait.until(EC.visibility_of_element_located(self.phone_input)).send_keys(phone_number)
    def get_phone_number(self):
        return self.wait.until(EC.visibility_of_element_located(self.phone_input)).get_property("value")
    def click_next_button(self):
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click()
    def enter_sms_code(self, code):
        self.wait.until(EC.visibility_of_element_located(self.sms_code)).send_keys(code)
    def confirmar_sms(self):
        self.wait.until(EC.element_to_be_clickable(self.boton_confirmar)).click()

    #4ok
    def abrir_metodo_pago(self):
        self.wait.until(EC.element_to_be_clickable(self.button_metodo_pago)).click()
    def is_open_metod_pago_enabled(self):
        return self.wait.until(EC.element_to_be_clickable(self.button_metodo_pago)).is_enabled()
    def bot_agregar_tarjeta(self):
        self.wait.until(EC.element_to_be_clickable(self.boton_agregar_tarjeta)).click()
    def click_card_number(self):
        self.wait.until(EC.element_to_be_clickable(self.card_input)).click()
    def add_card(self, number):
        # Ingresar número de tarjeta
        self.wait.until(EC.visibility_of_element_located(self.card_input)).send_keys(number)
    def click_cvv_number(self):
        self.wait.until(EC.element_to_be_clickable(self.card_cvv_input)).click()
    def add_cvv(self, cvv):
        # Ingresar CVV
        cvv_field = self.wait.until(EC.visibility_of_element_located(self.card_cvv_input))
        cvv_field.send_keys(cvv)

        # Simular pérdida de enfoque con TAB
        cvv_field.send_keys(Keys.TAB)

        # Esperar y hacer clic en el botón 'link'
        link_button = self.wait.until(EC.element_to_be_clickable(self.link_card_button))
        link_button.click()
    def agregar_y_cerrar(self):
        self.wait.until(EC.element_to_be_clickable(self.x_cerrar)).click()

    #5ok
    def write_message(self, message):
        self.driver.find_element(*self.message_input).send_keys(message)
    def get_write_message(self):
        return self.driver.find_element(*self.message_input).get_property("value")

    #6
    def is_blanket_tissues_enabled(self):
        return self.driver.find_element(*self.blanket_and_tissues_checkbox).is_enabled()
    def request_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_and_tissues_checkbox).click()

    #7
    def is_add_ice_cream_enabled(self):
        return self.wait.until(EC.element_to_be_clickable(self.ice_cream_counter)).is_enabled()
    def add_ice_cream(self, count=2):
        for _ in range(count):
            counter = self.wait.until(EC.element_to_be_clickable(self.ice_cream_counter))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", counter)
            counter.click()

    #8
    def is_order_taxi_enabled(self):
        return self.wait.until(EC.element_to_be_clickable(self.button_order_taxi)).is_enabled()
    def order_taxi(self):
        self.wait.until(EC.element_to_be_clickable(self.button_order_taxi)).click()

