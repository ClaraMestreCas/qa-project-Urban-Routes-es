#Pruebas de clase
import data
from phone_code import retrieve_phone_code
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urban_routes_page import UrbanRoutesPage



class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.page = UrbanRoutesPage(cls.driver)
        cls.driver.get(data.urban_routes_url)




    def test_1configurar_direccion(self):
        # 1. Ingresar ruta
        self.page.set_route(data.address_from, data.address_to)
        assert self.page.get_from_adress() == data.address_from
        assert self.page.get_to_adress() == data.address_to


    def test_2selc_tarifa_comfort(self):
        assert self.page.is_select_taxi_enabled() == True
        # 2. Pedir un taxi
        self.page.select_pedir_taxi()
        # 3. Seleccionar tarifa Comfort
        self.page.select_tariff_comfort()

    def test_3rellenar_numero_telefono(self):
        # 4. Ingresar número de teléfono
        self.page.enter_phone_number(data.phone_number)
        assert self.page.get_phone_number() == data.phone_number
        # 5. Seleccionar siguiente
        self.page.click_next_button()
        # 6. Introducir código SMS
        self.page.enter_sms_code(retrieve_phone_code(self.driver))
        # 7. Seleccionar continuar SMS
        self.page.confirmar_sms()

    def test_4agregar_tarjeta(self):
        assert self.page.is_open_metod_pago_enabled() == True
        # 8. Metodo de pago
        self.page.abrir_metodo_pago()
        # 9. Seleccionar agregar tarjeta
        self.page.bot_agregar_tarjeta()
        # 10. Click agregar número tarjeta
        self.page.click_card_number()
        # 10.1 Agregar tarjeta
        self.page.add_card(data.card_number)
        # 10.2 Click agregar número CVV
        self.page.click_cvv_number()
        # 10.3 Agregar CVV
        self.page.add_cvv(data.card_code)
        # 11. Cerrar con la X
        self.page.agregar_y_cerrar()

    def test_5mensaje_controlador(self):
       # 12. Escribir mensaje para el conductor
        self.page.write_message(data.message_for_driver)
        assert self.page.get_write_message() == data.message_for_driver

    def test_6_manta_panuelos(self):
        assert self.page.is_blanket_tissues_enabled() == True
        # 13. Pedir manta y pañuelos
        self.page.request_blanket_and_tissues()

    def test_7helado(self):
        assert self.page.is_add_ice_cream_enabled() == True
        self.page.add_ice_cream(2)


    def test_8modal_taxi(self):
        assert self.page.is_order_taxi_enabled() == True
        # 15. Pedir taxi
        self.page.order_taxi()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()