#Pruebas de clase
import data
from main import retrieve_phone_code
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

    def test_full_taxi_order_flow(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)



        # 1. Ingresar ruta
        page.set_route(data.address_from, data.address_to)

        # 2. pedir un taxi
        page.select_pedir_taxi()

        # 3. Seleccionar tarifa Comfort
        page.select_tariff_comfort()

        # 4. Ingresar número de teléfono
        page.enter_phone_number(data.phone_number)

        # 5. Agregar tarjeta
        page.add_card(data.card_number, data.card_code)

        # 6. Obtener y enviar código de confirmación
        code = retrieve_phone_code(self.driver)
        page.enter_confirmation_code(code)

        # 7. Escribir mensaje para el conductor
        page.write_message(data.message_for_driver)

        # 8. Pedir manta y pañuelos
        page.request_blanket_and_tissues()

        # 9. Pedir 2 helados
        page.add_ice_cream(2)

        # 10. Pedir taxi
        page.order_taxi()

        # 11. Verificar que se muestra el modal
        assert page.is_searching_modal_visible()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()