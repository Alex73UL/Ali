loc_left_menu = 'com.alibaba.aliexpresshd:id/left_action'
loc_profile_name_button = 'com.alibaba.aliexpresshd:id/profile_name_text'
loc_sign_in_button = 'com.alibaba.aliexpresshd:id/btn_sign_in'
loc_login_text = 'com.alibaba.aliexpresshd:id/et_email'
loc_password_text = 'com.alibaba.aliexpresshd:id/et_password'
loc_entered_data_button = 'com.alibaba.aliexpresshd:id/rl_ali_sign_in_btn'
loc_massage = 'android:id/message'


def start_activity(driver):
    driver.start_activity("com.alibaba.aliexpresshd", "com.aliexpress.module.home.MainActivity")


def open_page_for_sign_in(driver):
    menu_button = driver.find_element_by_id(loc_left_menu)
    menu_button.click()
    profile_name_button = driver.find_element_by_id(loc_profile_name_button)
    profile_name_button.click()

    sign_in_button = driver.find_element_by_id(loc_sign_in_button)
    sign_in_button.click()


def enter_login_password(driver, login, password):
    login_text = driver.find_element_by_id(loc_login_text)
    login_text.send_keys(login)
    password_text = driver.find_element_by_id(loc_password_text)
    password_text.send_keys(password)
    entered_data_button = driver.find_element_by_id(loc_entered_data_button)
    entered_data_button.click()


def check_authorisation(driver, massage):
    current_massage = driver.find_element_by_id(loc_massage).text
    return current_massage == massage
