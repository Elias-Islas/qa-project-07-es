import data
import time
from UrbanRoutesPage import UrbanRoutesPage
from retrieve_phone_code import retrieve_phone_code
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()  # configura que la ventana inicialice maximizado
        cls.driver.get(data.urban_routes_url)  # Abre la página de UrbanRouter
        cls.routes_page = UrbanRoutesPage(cls.driver)  # Instancia la clase routes_page, enviando el driver

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        (WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located(self.routes_page.from_field)))
        self.routes_page.set_route(address_from, address_to)

        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to
        time.sleep(5)

    def test_select_comfort(self): # selecciona comfort
        (WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(self.routes_page.order_a_taxi_button)))
        self.routes_page.order_a_taxi_click()
        (WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(self.routes_page.comfort_image)))
        assert self.routes_page.is_visible_taxi_back_arrow()  #valida que se haya seleccionado taxi
        self.routes_page.comfort_image_click()
        assert self.routes_page.is_visible_order_requirements_section()  #valida que se haya seleccionado comfort

    def test_set_register_phone_number(self): #regista el numero de telefono
        phone_number = data.phone_number
        self.routes_page.set_register_phone_number(phone_number)
        assert self.routes_page.get_phone_number_field()==data.phone_number  #valida que se haya capturado el teléfono
        code = retrieve_phone_code(self.driver)
        assert code != ""   #valida que se haya generado el código que llega por SMS
        self.routes_page.set_register_sms_code(code)

    def test_set_card_to_pay(self):
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.set_way_to_pay(card_number, card_code)
        assert self.routes_page.is_card_selected()  #valida que la tarjeta se agregó y se seleccionó

    def test_set_message_for_driver(self):
        self.routes_page.set_order_requirements(data.message_for_driver)
        assert self.routes_page.get_driver_comment_field() == data.message_for_driver #valida el mensaje al conductor

    def test_select_manta_scarves(self):
        assert self.routes_page.is_selected_manta_and_scarves_check_box_field() #valida selección de bufanda

    def test_select_two_ice_cream(self):
        assert self.routes_page.get_ice_cream_counter() == '2' #valida seleccionar 2 helados

    def test_ask_for_a_taxi(self):
        self.routes_page.ask_for_a_taxi_click()
        (WebDriverWait(self.driver, 50).until(
            expected_conditions.visibility_of_element_located(self.routes_page.order_body)))
        assert self.routes_page.is_visible_modal_order_body()  #se valida que aparezca la modal de buscar automóvil

    def test_view_driver_information(self):
        (WebDriverWait(self.driver, 50).until(
            expected_conditions.visibility_of_element_located(self.routes_page.bender_image)))
        assert self.routes_page.is_visible_driver_information()  #se valida que aparece la información del conductor


    @classmethod
    def teardown_class(cls):
        time.sleep(8)
        cls.driver.quit()