from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class UrbanRoutesPage:
    from_field = (By.ID, 'from')  # $("#from")
    to_field = (By.ID, 'to')  # $("#to")

    order_a_taxi_button = (By.CSS_SELECTOR, "button[type='button'].button.round")
    comfort_image = (By.CSS_SELECTOR, "img[alt='Comfort']")


    phone_number_section = (By.CSS_SELECTOR, "div.np-text")
    phone_number_field = (By.ID, 'phone')
    following_button = (By.CSS_SELECTOR, "button[type='submit'].button.full")
    sms_field = (By.ID, 'code')
    confirm_button = (By.CSS_SELECTOR, "div.section.active button[type='submit'].button.full")
    close_number_window_button = (By.CSS_SELECTOR, "div.number-picker button.close-button.section-close")

    way_to_pay_section = (By.CSS_SELECTOR, "div.pp-button.filled")
    add_a_card_section = (By.CSS_SELECTOR, "div.pp-row.disabled")
    card_number_field = (By.ID, 'number')
    code_field = (By.CSS_SELECTOR, '#code.card-input')
    link_button = (By.CSS_SELECTOR, "div.pp-buttons button[type='submit'].button.full")
    close_payment_window_button = (By.CSS_SELECTOR, "div.payment-picker button.close-button.section-close")

    driver_comment_field = (By.ID, 'comment')
    manta_and_scarves_check_box = (By.CSS_SELECTOR, "div.reqs-body > div span.slider.round")
    ice_cream_section = (By.CSS_SELECTOR, "div.r-group-items > div:nth-child(1) div.counter-plus")
    chocolate_section = (By.CSS_SELECTOR, "div.r-group-items > div:nth-child(2) div.counter-plus")

    ask_for_a_taxi_button = (By.CSS_SELECTOR, "button.smart-button")
    set_order_body = (By.XPATH, "//div[@class='number']")
    bender_image = (By.CSS_SELECTOR, "div.order-body img[alt='close']")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def set_sms_code(self, code):
        self.driver.find_element(*self.sms_field).send_keys(code)

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self, card_code):
        print("cvv:",card_code)
        self.driver.find_element(*self.code_field).send_keys(card_code)
        print("obteniendo cvv")
        self.driver.find_element(*self.code_field).send_keys(Keys.TAB)
        print("sacando de foco")


    def set_message_for_driver(self, message_for_driver):
        self.driver.find_element(*self.driver_comment_field).send_keys(message_for_driver)

    def order_a_taxi_click(self):  # Da clic al boton "Pedir un taxi"
        self.driver.find_element(*self.order_a_taxi_button).click()

    def comfort_image_click(self):  # Dar clic al boton "imagen de comfort"
        self.driver.find_element(*self.comfort_image).click()

    def phone_number_click(self):  # Da clic al boton "Pedir un taxi"
        self.driver.find_element(*self.phone_number_section).click()

    def confirm_button_click(self):
        self.driver.find_element(*self.confirm_button).click()

    def following_click(self):  # Dar clic al boton "imagen de comfort"
        self.driver.find_element(*self.following_button).click()

    def close_number_window_click(self):
        self.driver.find_element(*self.close_number_window_button).click()

    def way_to_pay_click(self):  # Dar clic al boton "imagen de comfort"---------------------------------
        self.driver.find_element(*self.way_to_pay_section).click()

    def add_a_card_click(self):  # Dar clic al boton "imagen de comfort"
        self.driver.find_element(*self.add_a_card_section).click()

    def link_click(self):
        self.driver.find_element(*self.link_button).click()

    def close_payment_window_click(self):
        self.driver.find_element(*self.close_payment_window_button).click()

    def manta_and_scarves_check_box_click(self):
        self.driver.find_element(*self.manta_and_scarves_check_box).click()

    def ice_cream_click(self):
        self.driver.find_element(*self.ice_cream_section).click()

    def chocolate_click(self):
        self.driver.find_element(*self.chocolate_section).click()

    def ask_for_a_taxi_click(self):
        self.driver.find_element(*self.ask_for_a_taxi_button).click()

    def set_route(self, from_field, to_field):
        self.set_from(from_field)
        self.set_to(to_field)

    def set_register_phone_number(self, phone_number):
        self.phone_number_click()
        self.set_phone_number(phone_number)
        self.following_click()

    def set_register_sms_code(self, sms_code):
        self.set_sms_code(sms_code)
        self.confirm_button_click()

    def set_way_to_pay(self, card_number_field, card_code_field):
        self.way_to_pay_click()
        self.add_a_card_click()
        self.set_card_number(card_number_field)
        self.set_card_code(card_code_field)
        self.link_click()
        self.close_payment_window_click()

    def set_order_requirements(self, driver_comment_field):
        self.set_message_for_driver(driver_comment_field)
        self.manta_and_scarves_check_box_click()
        self.ice_cream_click()
        self.chocolate_click()
        self.chocolate_click()

    def set_ask_for_a_taxi(self):
        self.ask_for_a_taxi_click()

    def get_from(self) -> str:
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self) -> str:
        return self.driver.find_element(*self.to_field).get_property('value')

    def get_phone_number_field(self) -> str:
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def get_sms_code(self) -> str:
        return self.driver.find_element(*self.sms_field).get_property('value')

    def get_card_number_field(self) -> str:
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_code_field(self) -> str:
        code_field = self.driver.find_element(*self.code_field)  # Find the code field element
        return code_field.get_property('value')  # Retrieve the value after tabulation

    def get_driver_comment_field(self) -> str:
        return self.driver.find_element(*self.driver_comment_field).get_property('value')
