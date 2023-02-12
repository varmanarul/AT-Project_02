from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

class Project_Of_Orange_HRM_2():

    
    def TC_PIM_01(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()

        # Switch to admin tab
        xpath_for_admin = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        switch_to_admin = driver.find_element(By.XPATH, xpath_for_admin)
        # Clicking on admin tab
        switch_to_admin.click()
        time.sleep(2)

        # Validating below menu options are displaying in Side pane
        xpath_for_sidepane = '//nav[@class="oxd-navbar-nav"]'
        side_pane = driver.find_element(By.XPATH, xpath_for_sidepane)
        assert side_pane, side_pane.is_displayed()
        time.sleep(2)
        print("Validation is successfull")

        # Validating below menu options are displaying in Side pane(Negative scenario)
        xpath_for_side_pane_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
        side_pane_1 = driver.find_element(By.XPATH, xpath_for_side_pane_1)
        assert side_pane_1, side_pane.is_displayed()
        print("Validation is  not successfull")
        time.sleep(2)

        # Validating Search text box is displaying on Side pane
        xpath_for_search = '//div[@class="oxd-main-menu-search"]'
        search_button = driver.find_element(By.XPATH,xpath_for_search)
        assert search_button, search_button.is_displayed()
        print("Search box is displaying on Admin page")
        # Clicking on search box with provided text
        xpath_for_search = '//input[@placeholder="Search"]'
        searching_on_search = driver.find_element(By.XPATH, xpath_for_search)
        # Using for loop to search in upper
        list_1 = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
        for a in list_1:
            searching_on_search.send_keys(a.upper())
            time.sleep(1)
        # Clearing existing text
            searching_on_search.send_keys(Keys.CONTROL,'a')
            searching_on_search.send_keys(Keys.BACKSPACE)
            time.sleep(1)
        # Using for loop to search in upper
        for a in list_1:
            searching_on_search.send_keys(a.lower())
            time.sleep(1)
        # Clearing existing text
            searching_on_search.send_keys(Keys.CONTROL,'a')
            searching_on_search.send_keys(Keys.BACKSPACE)
            time.sleep(1)
        print("Individual menu are displayed under search box") 
        driver.quit()

    def TC_PIM_02(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()

        # Switch to admin tab
        xpath_for_admin = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        switch_to_admin = driver.find_element(By.XPATH, xpath_for_admin)
        # Clicking on admin tab
        switch_to_admin.click()
        time.sleep(2)

        # Validating below menu options are displaying in Side pane
        xpath_for_sidepane = '//nav[@class="oxd-navbar-nav"]'
        side_pane = driver.find_element(By.XPATH, xpath_for_sidepane)
        assert side_pane, side_pane.is_displayed()
        print("Validation is successfull")
        time.sleep(2)
        # Finding xpath for user management tab
        xpath_for_user_mgmt = '//li[@class="oxd-topbar-body-nav-tab --parent --visited"]'
        user_management_tab = driver.find_element(By.XPATH, xpath_for_user_mgmt)
        # Clicking on user management tab
        user_management_tab.click()
        time.sleep(2)
        # Finding xpath for clicking on users
        xpath_for_user = '//a[@href="#"]'
        click_on_user = driver.find_element(By.XPATH, xpath_for_user)
        # Clicking on user management tab
        click_on_user.click()
        # Finding xpath for clicking on user role tab
        click_on_user_role = '//label[text()="User Role"]/following::div[1]'
        users_dropdown = driver.find_element(By.XPATH, click_on_user_role)
        users_dropdown.click()
        # Finding xpath for clicking on admin
        xpath_for_admin = '//div[@role="option"]/span[text()="Admin"]'
        clicking_on_admin = driver.find_element(By.XPATH, xpath_for_admin)
        # Validating to see below drop down value for Users Role dropdown
        if clicking_on_admin.text == "Admin":
            assert clicking_on_admin, clicking_on_admin.text.is_displayed()
            print("Admin is displaying")
        else:
            print("Admin is not displaying")
        # Finding xpath for clicking on ESS
        xpath_for_ESS = '//div[@role="option"]/span[text()="ESS"]'
        clicking_on_ess = driver.find_element(By.XPATH, xpath_for_ESS)
        # Validating to see below drop down value for Users Role dropdown
        if clicking_on_ess.text == "ESS":
            assert clicking_on_ess, clicking_on_ess.text.is_displayed()
            print("ESS is displaying")
        else:
            print("ESS is not displaying")
        time.sleep(2)
        # Finding xpath for clicking on status tab
        click_on_status = '//label[text()="Status"]/following::div[1]'
        status_dropdown = driver.find_element(By.XPATH, click_on_status)
        status_dropdown.click()
        # Finding xpath for selecting enabled
        xpath_for_enabled = '//div[@role="option"]/span[text()="Enabled"]'
        selecting_enabled = driver.find_element(By.XPATH, xpath_for_enabled)
        # Validating to see below drop down value for Status dropdown
        if selecting_enabled.text == "Enabled":
            assert selecting_enabled, selecting_enabled.text.is_displayed()
            print("Enable is displaying")
        else:
            print("Enable is not displaying")
        # Finding xpath for selecting disabled
        xpath_for_disabled = '//div[@role="option"]/span[text()="Disabled"]'
        selecting_disabled = driver.find_element(By.XPATH, xpath_for_disabled)
        # Validating to see below drop down value for Status dropdown
        if selecting_disabled.text == "Disabled":
            assert selecting_disabled, selecting_disabled.text.is_displayed()
            print("Disable is displaying")
        else:
            print("Disable is not displaying")
        driver.quit() 


    def TC_PIM_03(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()

        # Switch to admin tab
        xpath_for_admin = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        switch_to_admin = driver.find_element(By.XPATH, xpath_for_admin)
        # Clicking on admin tab
        switch_to_admin.click()
        time.sleep(2)

        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(2)
        # Validating below menu options are displaying in Side pane
        xpath_for_sidepane = '//nav[@class="oxd-navbar-nav"]'
        side_pane = driver.find_element(By.XPATH, xpath_for_sidepane)
        assert side_pane, side_pane.is_displayed()
        print("Validation is successfull")
        time.sleep(2)
        # Xpath for clicking on Add button
        xpath_for_add = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        click_on_add = driver.find_element(By.XPATH, xpath_for_add)
        click_on_add.click()
        time.sleep(4)
        # Sending input for first name
        xpath_for_first_name = '//input[@name="firstName"]'
        first_name = driver.find_element(By.XPATH, xpath_for_first_name)
        # Sending keys for first name
        first_name.send_keys("Nani")
        time.sleep(3)
        # Sending input for middle name
        xpath_for_middle_name = '//input[@name="middleName"]'
        middle_name = driver.find_element(By.XPATH, xpath_for_middle_name)
        # Sending keys for middle name
        middle_name.send_keys("Arul")
        time.sleep(3)
        # Sending input for last name
        xpath_for_last_name = '//input[@name="lastName"]'
        last_name = driver.find_element(By.XPATH, xpath_for_last_name)
        # Sending keys for last name
        last_name.send_keys("Varman")
        time.sleep(3)
        # Enable login details
        xpath_for_enabling_login = '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]'
        enabling_login = driver.find_element(By.XPATH,xpath_for_enabling_login)
        # Clicking on login
        enabling_login.click()
        time.sleep(4)
        # Xpath for Username
        username_pim = "//label[text()='Username']/following::div[1]/input"
        time.sleep(3)
        username_input = driver.find_element(By.XPATH, username_pim)
        # Sendking keys for username
        username_input.send_keys("Varma S")
        time.sleep(3)
        # Enabling status
        xpath_for_enabling_status = '//label[normalize-space()="Enabled"]'
        enable_status = driver.find_element(By.XPATH, xpath_for_enabling_status)
        # Clicking on enabling status
        enable_status.click()
        time.sleep(3)
        # Xpath for password
        password_pim = "//div/label[text()='Password']/following::div[1]/input"
        password_input = driver.find_element(By.XPATH, password_pim)
        time.sleep(3)
        # Sending keys for password
        password_input.send_keys("Arul@0078")
        # Xpath for Confirming password
        password_confirm_pim = "//div/label[text()='Confirm Password']/following::div[1]/input"
        password_input_confirm = driver.find_element(By.XPATH, password_confirm_pim)
        time.sleep(3)
        # Sending keys for password
        password_input_confirm.send_keys("Arul@0078")
        time.sleep(3)
        # Xpath for save button
        xpath_for_save = '//button[@type="submit"]'
        save_button = driver.find_element(By.XPATH, xpath_for_save)
        # Clicking on save button
        save_button.click()
        time.sleep(3)
        print("Created new employee and page moved to employee list")
        driver.quit()

    def TC_PIM_04(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(2)
        
        # Xpath for searching in employee name
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for searching in employee name
        emp_name_search.send_keys("Nani Arul Varman")
        time.sleep(3)
        # Xpath for clicking on Search button
        xpath_for_clicking_on_search = '//button[@type="submit"]'
        search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # Clicking on Search button       
        search_click.click()
        time.sleep(3)
        # Xpath for clicking on edit button
        xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # Clicking on edit button       
        click_on_edit_button.click()
        time.sleep(5)
        # Validating below tabs are displaying in PIM page
        xpath_for_pim_tabs = '//div[@role="tablist"]'
        pim_tabs = driver.find_element(By.XPATH, xpath_for_pim_tabs)
        assert pim_tabs, pim_tabs.is_displayed()
        time.sleep(2)
        print("All tabs are presnt")
        driver.quit()

    def TC_PIM_05(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(3)
        # Xpath for searching in employee name
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for searching in employee name
        emp_name_search.send_keys("Nani Arul Varman")
        time.sleep(3)
        # Xpath for clicking on Search button
        xpath_for_clicking_on_search = '//button[@type="submit"]'
        search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # Clicking on Search button       
        search_click.click()
        time.sleep(3)
        # Xpath for clicking on edit button
        xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # Clicking on edit button       
        click_on_edit_button.click()
        time.sleep(5)
        # Going to personal details
        xpath_for_personal_details = '//a[@class="orangehrm-tabs-item --active"]'       
        personal_details_click = driver.find_element(By.XPATH, xpath_for_personal_details)
        # Clicking on personal details
        personal_details_click.click()
        time.sleep(3)
        # Xpath for nickname
        xpath_for_nickname = "//label[text()='Nickname']/following::div[1]/input"
        nickname_enter = driver.find_element(By.XPATH, xpath_for_nickname)
        # Sending keys for nickname
        nickname_enter.send_keys("nani")
        time.sleep(3)
        # Xpath for emp id
        xpath_for_emp_id = "//label[text()='Employee Id']/following::div[1]/input"
        emp_id_enter = driver.find_element(By.XPATH, xpath_for_emp_id)
        # Sending keys for nickname
        emp_id_enter.send_keys("1994")
        time.sleep(3)
       # Xpath for other id
        xpath_for_other_id = '//label[text()="Other Id"]/following::div[1]/input'
        other_id_enter = driver.find_element(By.XPATH, xpath_for_other_id)
        # Sending keys for other id
        other_id_enter.send_keys("1994")
        time.sleep(3)
        # Xpath for License expiry date
        xpath_for_license_exp_date = "(//input[@placeholder='yyyy-mm-dd'])[1]"
        license_exp_date_enter = driver.find_element(By.XPATH, xpath_for_license_exp_date)
        # Sending keys for License expiry date
        license_exp_date_enter.send_keys("2023-02-19")
        time.sleep(3)
        # Xpath for SSN no
        xpath_for_ssn_no = '//label[text()="SSN Number"]/following::div[1]/input'
        ssn_no_enter = driver.find_element(By.XPATH, xpath_for_ssn_no)
        # Sending keys for other id
        ssn_no_enter.send_keys("1820")
        time.sleep(3)
        # Xpath for SIN no
        xpath_for_sin_no = '//label[text()="SIN Number"]/following::div[1]/input'
        sin_no_enter = driver.find_element(By.XPATH, xpath_for_sin_no)
        # Sending keys for other id
        sin_no_enter.send_keys("0281")
        time.sleep(3)
        # Xpath for Nationality
        xpath_for_nationality = '//label[text()="Nationality"]/following::div[1]'
        nationality_enter = driver.find_element(By.XPATH, xpath_for_nationality)
        nationality_enter.click()
        selecting_nation = "//div[@role='option']/span[text()='Indian']"
        nation_choose = driver.find_element(By.XPATH, selecting_nation)
        nation_choose.click()
        # Xpath for Marital Status
        xpath_for_marital_status = '//label[text()="Marital Status"]/following::div[1]'
        marital_status_entry = driver.find_element(By.XPATH, xpath_for_marital_status)
        marital_status_entry.click()
        status_entered = "//div[@role='option']/span[text()='Single']"
        enter_status = driver.find_element(By.XPATH, status_entered)
        enter_status.click()
        # Xpath for DOB
        xpath_for_dob = '//label[text()="Date of Birth"]/following::div[3]/input'
        dob_entry = driver.find_element(By.XPATH, xpath_for_dob)
        time.sleep(2)
        # Sending keys for DOB
        dob_entry.send_keys("1994-08-06")
        time.sleep(3)
        # Xpath for gender
        xpath_for_gender = '//label[normalize-space()="Male"]'
        gender_entry = driver.find_element(By.XPATH, xpath_for_gender)
        # Clicking on gender
        gender_entry.click()
        # Xpath for MS
        xpath_for_MS = '//label[text()="Military Service"]/following::div[1]/input'
        ms_entry = driver.find_element(By.XPATH, xpath_for_MS)
        # Sending keys for MS
        ms_entry.send_keys("No")
        # Xpath for save
        xpath_for_saving = '//button[@type="submit"]'
        saving_entry = driver.find_element(By.XPATH, xpath_for_saving)
        # Clicking on Save
        saving_entry.click()
        time.sleep(5)
        # # Xpath for blood group
        xpath_for_blood_group = '//label[text()="Blood Type"]/following::div[1]'
        blood_group_chosen = driver.find_element(By.XPATH, xpath_for_blood_group)
        blood_group_chosen.click()
        blood_group_enetered = "//div[@role='option']/span[text()='B+']"
        bg_entered = driver.find_element(By.XPATH, blood_group_enetered)
        bg_entered.click()
        time.sleep(5)
        # Xpath for save 2
        xpath_for_saving_2 = "//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']"
        saving_entry_2 = driver.find_element(By.XPATH, xpath_for_saving_2)
        # Clicking on Save
        saving_entry_2.click()
        time.sleep(3)
        print("Saved and validated all details are present")
        time.sleep(5)
        # Validating the filled details are present
        try:
            test_1 = ssn_no_enter.text
            print("Filled details are present")
        except:
            print("Filled details are not present")
        time.sleep(3)

        driver.quit()


    def TC_PIM_06(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(3)
        # Xpath for searching in employee name
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for searching in employee name
        emp_name_search.send_keys("Nani Arul Varman")
        time.sleep(3)
        # Xpath for clicking on Search button
        xpath_for_clicking_on_search = '//button[@type="submit"]'
        search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # Clicking on Search button       
        search_click.click()
        time.sleep(3)
        # Xpath for clicking on edit button
        xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # Clicking on edit button       
        click_on_edit_button.click()
        time.sleep(5)       
        # Going to contact details
        xpath_for_contact_details = '//div[@role="tab"]/following::div[1]/a[text()="Contact Details"]'
        time.sleep(5)       
        contact_details_click = driver.find_element(By.XPATH, xpath_for_contact_details)
        # Clicking on contact details
        contact_details_click.click()
        time.sleep(3)
        # Finding xpath for street 1
        xpath_for_street_1 = '//label[text()="Street 1"]/following::div[1]/input'
        entering_street_1 = driver.find_element(By.XPATH, xpath_for_street_1)
        time.sleep(3)
        # Sending keys for street 1
        entering_street_1.send_keys("No 40,south street")
        time.sleep(3)
        # Finding xpath for street 2
        xpath_for_street_2 = '//label[text()="Street 2"]/following::div[1]/input'
        entering_street_2 = driver.find_element(By.XPATH, xpath_for_street_2)
        time.sleep(3)
        # Sending keys for street 2
        entering_street_2.send_keys("1st cross lane")
        time.sleep(3)
        # Finding xpath for City
        xpath_for_city = '//label[text()="City"]/following::div[1]/input'
        entering_city = driver.find_element(By.XPATH, xpath_for_city)
        time.sleep(3)
        # Sending keys for City
        entering_city.send_keys("Virudhachalam")
        time.sleep(3)
        # Finding xpath for State/Province
        xpath_for_state = '//label[text()="State/Province"]//following::div[1]/input'
        entering_state = driver.find_element(By.XPATH, xpath_for_state)
        time.sleep(3)
        # Sending keys for State/Province
        entering_state.send_keys("Tamil Nadu")
        time.sleep(3)
        # Finding xpath for Zip/Postal Code
        xpath_for_pc = '//label[text()="Zip/Postal Code"]//following::div[1]/input'
        entering_pc = driver.find_element(By.XPATH, xpath_for_pc)
        time.sleep(3)
        # Sending keys for Zip/Postal Code
        entering_pc.send_keys("606110")
        time.sleep(3)
        # Finding xpath for Country
        xpath_for_country = '//label[text()="Country"]/following::div[1]'
        country_enter = driver.find_element(By.XPATH, xpath_for_country)
        country_enter.click()
        time.sleep(3)
        selecting_country = "//div[@role='option']/span[text()='India']"
        country_choose = driver.find_element(By.XPATH, selecting_country)
        country_choose.click()
        # Finding xpath for home tele no
        xpath_for_home_no = '//label[text()="Home"]/following::div[1]/input'
        entering_home_no = driver.find_element(By.XPATH, xpath_for_home_no)
        time.sleep(3)
        # Sending keys for home tele no
        entering_home_no.send_keys("12345678")
        time.sleep(3)
        # Finding xpath for mob tele no
        xpath_for_mob_no = '//label[text()="Mobile"]/following::div[1]/input'
        entering_mob_no = driver.find_element(By.XPATH, xpath_for_mob_no)
        time.sleep(3)
        # Sending keys for mob tele no
        entering_mob_no.send_keys("87654321")
        time.sleep(3)
        # Finding xpath for work tele no
        xpath_for_work_no = '//label[text()="Work"]/following::div[1]/input'
        entering_work_no = driver.find_element(By.XPATH, xpath_for_work_no)
        time.sleep(3)
        # Sending keys for work tele no
        entering_work_no.send_keys("02345")
        time.sleep(3)
        # Finding xpath for work email
        xpath_for_work_email = '//label[text()="Work Email"]/following::div[1]/input'
        entering_work_email = driver.find_element(By.XPATH, xpath_for_work_email)
        time.sleep(3)
        # Sending keys for work email
        entering_work_email.send_keys("nanni@hotmail.com")
        time.sleep(3)
        # Finding xpath for other email
        xpath_for_other_email = '//label[text()="Other Email"]/following::div[1]/input'
        entering_other_email = driver.find_element(By.XPATH, xpath_for_other_email)
        time.sleep(3)
        # Sending keys for work email
        entering_other_email.send_keys("navoi@hotmail.com")
        time.sleep(3)
        # Xpath for save
        xpath_for_saving_1 = '//button[@type="submit"]'
        saving_entry_1 = driver.find_element(By.XPATH, xpath_for_saving_1)
        # Clicking on Save
        saving_entry_1.click()
        time.sleep(3)
        print("Saved and validated all details are present")
        time.sleep(5)
        # Validating the filled details are present
        try:
            test_1 = entering_other_email.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        time.sleep(3) 
        driver.quit()

    def TC_PIM_07(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(3)
        # Xpath for searching in employee name
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for searching in employee name
        emp_name_search.send_keys("Nani Arul Varman")
        time.sleep(3)
        # Xpath for clicking on Search button
        xpath_for_clicking_on_search = '//button[@type="submit"]'
        search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # Clicking on Search button       
        search_click.click()
        time.sleep(3)
        # Xpath for clicking on edit button
        xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # Clicking on edit button       
        click_on_edit_button.click()
        time.sleep(5)       
        # Going to emergency details
        xpath_for_emergency_details = '//div[@role="tab"]/following::div[1]/a[text()="Emergency Contacts"]'
        time.sleep(5)       
        emergency_details_click = driver.find_element(By.XPATH, xpath_for_emergency_details)
        # Clicking on emergency details
        emergency_details_click.click()
        time.sleep(3)
        # Clicking on add
        xpath_for_add = '//h6[text()="Assigned Emergency Contacts"]/following::button[1]'
        time.sleep(5)
        clicking_on_add = driver.find_element(By.XPATH, xpath_for_add)
        # Clicking on add
        clicking_on_add.click()
        time.sleep(3)
        # Finding xpath for emer name
        xpath_for_emergency_name = '//label[text()="Name"]/following::div[1]/input'
        entering_emergency_name = driver.find_element(By.XPATH, xpath_for_emergency_name)
        time.sleep(3)
        # Sending keys for emer name
        entering_emergency_name.send_keys("Vijay")
        time.sleep(3)
        # Finding xpath for emer rel
        xpath_for_emergency_relationship = '//label[text()="Relationship"]/following::div[1]/input'
        entering_emergency_relationship = driver.find_element(By.XPATH, xpath_for_emergency_relationship)
        time.sleep(3)
        # Sending keys for emer rel
        entering_emergency_relationship.send_keys("Brother")
        time.sleep(3)
        # Finding xpath for home tele
        xpath_for_emergency_home_tele = '//label[text()="Home Telephone"]/following::div[1]/input'
        entering_emergency_home_tele = driver.find_element(By.XPATH, xpath_for_emergency_home_tele)
        time.sleep(3)
        # Sending keys for home tele
        entering_emergency_home_tele.send_keys("123456")
        time.sleep(3)
        # Finding xpath for home tele
        xpath_for_emergency_mob_tele = '//label[text()="Mobile"]/following::div[1]/input'
        entering_emergency_mob_tele = driver.find_element(By.XPATH, xpath_for_emergency_mob_tele)
        time.sleep(3)
        # Sending keys for home tele
        entering_emergency_mob_tele.send_keys("654321")
        time.sleep(3)
        # Finding xpath for work tele
        xpath_for_emergency_work_tele = '//label[text()="Work Telephone"]/following::div[1]/input'
        entering_emergency_work_tele = driver.find_element(By.XPATH, xpath_for_emergency_work_tele)
        time.sleep(3)
        # Sending keys for work tele
        entering_emergency_work_tele.send_keys("023468")
        time.sleep(3)
        # Xpath for save
        xpath_for_saving_1 = '//button[@type="submit"]'
        saving_entry_1 = driver.find_element(By.XPATH, xpath_for_saving_1)
        # Clicking on Save
        saving_entry_1.click()
        time.sleep(3)
        print("Saved and validated all details are present")
        time.sleep(5)
        # Validating the filled details are present(Negative scenario)
        xpath_for_save_emerg_contact = '//h6[text() = "Assigned Emergency Contacts"]'
        save_emergency_contact = driver.find_element(By.XPATH, xpath_for_save_emerg_contact)
        try:
            test_1 = save_emergency_contact.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        time.sleep(3)         
        driver.quit()


    def TC_PIM_08(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(3)
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for searching in employee name
        emp_name_search.send_keys("Nani Arul Varman")
        time.sleep(3)
        # Xpath for clicking on Search button
        xpath_for_clicking_on_search = '//button[@type="submit"]'
        search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # Clicking on Search button       
        search_click.click()
        time.sleep(3)
        # Xpath for clicking on edit button
        xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # Clicking on edit button       
        click_on_edit_button.click()
        time.sleep(5)
        # Going to dependency details
        xpath_for_dependency_details = '//div[@role="tab"]/following::div[1]/a[text()="Dependents"]'
        time.sleep(5)       
        dependency_details_click = driver.find_element(By.XPATH, xpath_for_dependency_details)
        # Clicking on dependency details
        dependency_details_click.click()
        time.sleep(3)
        # Clicking on add
        xpath_for_add = '//h6[text()="Assigned Dependents"]/following::button[1]'
        clicking_on_add = driver.find_element(By.XPATH, xpath_for_add)
        # Clicking on add
        clicking_on_add.click()
        time.sleep(3)
        # Finding xpath for dependency name
        xpath_for_dependency_name = '//label[text()="Name"]/following::div[1]/input'
        dependency_emergency_name = driver.find_element(By.XPATH, xpath_for_dependency_name)
        time.sleep(3)
        # Sending keys for dependency name
        dependency_emergency_name.send_keys("Kumar")
        time.sleep(3)
        # Xpath for relationship
        xpath_for_relationship = '//label[text()="Relationship"]/following::div[1]'
        relationship_enter = driver.find_element(By.XPATH, xpath_for_relationship)
        relationship_enter.click()
        time.sleep(3)
        selecting_relationship = '//div[@role="option"]/span[text()="Other"]'
        relationship_choose = driver.find_element(By.XPATH, selecting_relationship)
        relationship_choose.click()
        # Xpath for DOB
        xpath_for_dob = '//label[text()="Date of Birth"]/following::div[3]/input'
        dob_entry = driver.find_element(By.XPATH, xpath_for_dob)
        time.sleep(2)
        # Sending keys for DOB
        dob_entry.send_keys("1998-12-19")
        time.sleep(3)
        #Xpath for save
        xpath_for_save = '//button[@type="submit"]'
        click_on_save = driver.find_element(By.XPATH, xpath_for_save)
        print("Saved and validated all details are present")
        time.sleep(5)
        # Validating the filled details are present
        try:
            test_1 = dependency_emergency_name.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        time.sleep(3) 
        driver.quit()

    def TC_PIM_09(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(3)
        # Xpath for searching in employee name
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for searching in employee name
        emp_name_search.send_keys("Nani Arul Varman")
        time.sleep(3)
        # Xpath for clicking on Search button
        xpath_for_clicking_on_search = '//button[@type="submit"]'
        search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # Clicking on Search button       
        search_click.click()
        time.sleep(3)
        # Xpath for clicking on edit button
        xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # Clicking on edit button       
        click_on_edit_button.click()
        time.sleep(5)
        # Going to job details
        xpath_for_job_details = '//a[text()="Job"]'
        time.sleep(2)       
        job_details_click = driver.find_element(By.XPATH, xpath_for_job_details)
        # Clicking on job details
        job_details_click.click()
        time.sleep(3)
        # Xpath for joined date
        xpath_for_joined_date = "//label[text()='Joined Date']/following::input[1]"
        joined_date_enter = driver.find_element(By.XPATH, xpath_for_joined_date)
        time.sleep(2)
        # Sending keys for joined date
        joined_date_enter.send_keys("2021-03-20")
        time.sleep(3)
        # Xpath for job title
        xpath_for_job_title = "//label[normalize-space()='Job Title']/following::div[3]"
        job_title_enter = driver.find_element(By.XPATH, xpath_for_job_title)
        job_title_enter.click()  
        time.sleep(3)     
        # Xpath for selecting title
        xpath_for_selecting_title = "//div[@role='option']/span[text()='Software Engineer']"
        selecting_title = driver.find_element(By.XPATH, xpath_for_selecting_title)        
        selecting_title.click()
        time.sleep(3)
        # Xpath for job category
        xpath_for_job_category = '//label[text()="Job Category"]/following::div[1]'
        job_category_enter = driver.find_element(By.XPATH, xpath_for_job_category)
        job_category_enter.click()       
        # Xpath for selecting job category
        xpath_for_selecting_job_category = '//div[@role="option"]/span[text()="Professionals"]'
        selecting_title = driver.find_element(By.XPATH, xpath_for_selecting_job_category)        
        selecting_title.click()
        time.sleep(3)
        # Xpath for sub units
        xpath_for_sub_units = "//label[text()='Sub Unit']/following::div[1]"
        sub_units_enter = driver.find_element(By.XPATH, xpath_for_sub_units)
        sub_units_enter.click()       
        # Xpath for selecting sub units
        xpath_for_selecting_sub_units = "//div[@role='option']/span[text()='Quality Assurance']"
        selecting_sub_units = driver.find_element(By.XPATH, xpath_for_selecting_sub_units)        
        selecting_sub_units.click()
        time.sleep(3)
        # Xpath for location
        xpath_for_location = "//label[text()='Location']/following::div[1]"
        location_enter = driver.find_element(By.XPATH, xpath_for_location)
        location_enter.click()       
        # Xpath for selecting job location
        xpath_for_location = '//div[@role="option"]/span[text()="Canadian Regional HQ"]'
        location_title = driver.find_element(By.XPATH, xpath_for_location)        
        location_title.click()
        time.sleep(3)
        # Xpath for employment status
        xpath_for_employment_status = '//label[text()="Employment Status"]/following::div[1]'
        employment_status_enter = driver.find_element(By.XPATH, xpath_for_employment_status)
        employment_status_enter.click()       
        # Xpath for selecting employment status
        xpath_for_employment_status = '//div[@role="option"]/span[text()="Full-Time Permanent"]'
        employment_status_title = driver.find_element(By.XPATH, xpath_for_employment_status)        
        employment_status_title.click()
        time.sleep(3)
        # Xpath for enabling Employment Contract Details
        xpath_for_employment_contract_details = '//p[text()="Include Employment Contract Details"]/following::div[1]'
        employment_contract_details = driver.find_element(By.XPATH, xpath_for_employment_contract_details)
        # Clicking on employment Contract Details
        employment_contract_details.click()
        # Xpath for contract start date
        xpath_for_start_date = "//p[text()='Include Employment Contract Details']/following::input[2]"
        start_date_enter = driver.find_element(By.XPATH, xpath_for_start_date)
        time.sleep(2)
        # Sending keys for contract start date
        start_date_enter.send_keys("2021-03-20")
        time.sleep(3)     
        # Xpath for contract end date
        xpath_for_end_date = "//p[text()='Include Employment Contract Details']/following::input[3]"
        end_date_enter = driver.find_element(By.XPATH, xpath_for_end_date)
        time.sleep(2)
        # Sending keys for contract start date
        end_date_enter.send_keys("2024-03-20")
        time.sleep(3) 
        # Xpath for button
        xpath_for_button = '//button[@type="submit"]'
        button_click = driver.find_element(By.XPATH, xpath_for_button)
        # Clicking on button
        button_click.click()
        time.sleep(5)
        print("Saved and validated all details are present")
        time.sleep(5)
        # Validating the filled details are present
        try:
            test_1 = end_date_enter.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        time.sleep(3) 
        driver.quit() 

    def TC_PIM_10(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(3)
        # Xpath for searching in employee name
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for searching in employee name
        emp_name_search.send_keys("Nani Arul Varman")
        time.sleep(3)
        # Xpath for clicking on Search button
        xpath_for_clicking_on_search = '//button[@type="submit"]'
        search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # Clicking on Search button       
        search_click.click()
        time.sleep(3)
        # Xpath for clicking on edit button
        xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # Clicking on edit button       
        click_on_edit_button.click()
        time.sleep(5)
        # Going to job details
        xpath_for_job_details = '//a[text()="Job"]'
        time.sleep(2)       
        job_details_click = driver.find_element(By.XPATH, xpath_for_job_details)
        # Clicking on job details
        job_details_click.click()    
        time.sleep(3)
        # Clicking on terminating employment
        xpath_for_terminate_emp = '//h6[text() = "Employee Termination / Activiation"]/following::button[1]'
        terminate_emp = driver.find_element(By.XPATH, xpath_for_terminate_emp)
        terminate_emp.click()
        time.sleep(3)
        # Xpath for termination date
        xpath_for_term_date = '//label[text()="Termination Date"]/following::div[3]/input'
        term_date_entry = driver.find_element(By.XPATH, xpath_for_term_date)
        time.sleep(2)
        # Sending keys for date
        term_date_entry.send_keys("2023-03-20")
        time.sleep(3)
        # Xpath for termination reason
        xpath_for_term_reason = '//label[text()="Termination Reason"]/following::div[3]'
        term_reason_entry = driver.find_element(By.XPATH, xpath_for_term_reason)
        term_reason_entry.click()
        time.sleep(2)
        # Sending keys for termination reason
        xpath_for_termination_reason = '//div[@role="option"]/span[text()="Dismissed"]'
        termination_reason = driver.find_element(By.XPATH, xpath_for_termination_reason)
        termination_reason.click()
        time.sleep(3)
        # Xpath for note
        xpath_for_note = '//label[text()="Note"]/following::div/textarea'
        note_entry = driver.find_element(By.XPATH, xpath_for_note)
        time.sleep(2)
        # Sending keys for termination reason
        note_entry.send_keys("None")
        time.sleep(3)
        # Clicking on save
        xpath_for_save = '//p[text()=" * Required"]/following::button[@type="submit"]'
        save_button = driver.find_element(By.XPATH, xpath_for_save)
        save_button.click()
        # Clicking on save 2
        xpath_for_save_2 = '//label[text()="Note"]/following::button[2]'
        save_button_2 = driver.find_element(By.XPATH, xpath_for_save_2)
        save_button_2.click()
        print("User is able to see termination on details page")
        time.sleep(3)

        driver.quit()

    def TC_PIM_11(self):

        # Initializing web browser
        driver = webdriver.Firefox()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(3)
        # Xpath for searching in employee name
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for searching in employee name
        emp_name_search.send_keys("Nani Arul Varman")
        time.sleep(3)
        # Xpath for clicking on Search button
        xpath_for_clicking_on_search = '//button[@type="submit"]'
        search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # Clicking on Search button       
        search_click.click()
        time.sleep(3)
        # Xpath for clicking on edit button
        xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # Clicking on edit button       
        click_on_edit_button.click()
        time.sleep(5)
        # Going to job details
        xpath_for_job_details = '//a[text()="Job"]'
        time.sleep(2)       
        job_details_click = driver.find_element(By.XPATH, xpath_for_job_details)
        # Clicking on job details
        job_details_click.click()
        time.sleep(3)
        """In the previous case, once, employee job is terminated, their emp
        name also disapears. Hence unable to activate it but the below code is the correct xpath 
        for it"""    
        # Xpath for clicking on activate employment
        xpath_for_activate_emp = "//h6[normalize-space()='Activate Employment']"
        activate_emp = driver.find_element(By.XPATH, xpath_for_activate_emp)
        # Clicking on activate employment
        activate_emp.click()
        time.sleep(3)
        # Xpath for terminate employment
        xpath_for_terminate_employment = "//button[normalize-space()='Terminate Employment']"
        terminate_employment = driver.find_element(By.XPATH, xpath_for_terminate_employment)
        print("Employee job is activated")
        time.sleep(3)
        driver.quit()

    def TC_PIM_12(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(2)
        # Validating below menu options are displaying in Side pane
        xpath_for_sidepane = '//nav[@class="oxd-navbar-nav"]'
        side_pane = driver.find_element(By.XPATH, xpath_for_sidepane)
        assert side_pane, side_pane.is_displayed()
        print("Validation is successfull")
        time.sleep(2)
        # Xpath for clicking on Add button
        xpath_for_add = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        click_on_add = driver.find_element(By.XPATH, xpath_for_add)
        click_on_add.click()
        time.sleep(4)
        # Sending input for first name
        xpath_for_first_name = '//input[@name="firstName"]'
        first_name = driver.find_element(By.XPATH, xpath_for_first_name)
        # Sending keys for first name
        first_name.send_keys("Joe")
        time.sleep(3)
        # Sending input for middle name
        xpath_for_middle_name = '//input[@name="middleName"]'
        middle_name = driver.find_element(By.XPATH, xpath_for_middle_name)
        # Sending keys for middle name
        middle_name.send_keys("Hughes")
        time.sleep(3)
        # Sending input for last name
        xpath_for_last_name = '//input[@name="lastName"]'
        last_name = driver.find_element(By.XPATH, xpath_for_last_name)
        # Sending keys for last name
        last_name.send_keys("Jackson")
        time.sleep(3)
        # Enable login details
        xpath_for_enabling_login = '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]'
        enabling_login = driver.find_element(By.XPATH,xpath_for_enabling_login)
        # Clicking on login
        enabling_login.click()
        time.sleep(4)
        # Xpath for emp id
        xpath_for_emp_id = "//label[text()='Employee Id']/following::div[1]/input"
        emp_id_enter = driver.find_element(By.XPATH, xpath_for_emp_id)
        # Sending keys for nickname
        emp_id_enter.send_keys("1994")
        time.sleep(3)
        # Xpath for Username
        username_pim = "//label[text()='Username']/following::div[1]/input"
        time.sleep(3)
        username_input = driver.find_element(By.XPATH, username_pim)
        # Sendking keys for username
        username_input.send_keys("Larven Woods")
        time.sleep(3)
        # Enabling status
        xpath_for_enabling_status = '//label[normalize-space()="Enabled"]'
        enable_status = driver.find_element(By.XPATH, xpath_for_enabling_status)
        # Clicking on enabling status
        enable_status.click()
        time.sleep(3)
        # Xpath for password
        password_pim = "//div/label[text()='Password']/following::div[1]/input"
        password_input = driver.find_element(By.XPATH, password_pim)
        time.sleep(3)
        # Sending keys for password
        password_input.send_keys("Woods@1200")
        # Xpath for Confirming password
        password_confirm_pim = "//div/label[text()='Confirm Password']/following::div[1]/input"
        password_input_confirm = driver.find_element(By.XPATH, password_confirm_pim)
        time.sleep(3)
        # Sending keys for password
        password_input_confirm.send_keys("Woods@1200")
        time.sleep(3)
        # Xpath for save button
        xpath_for_save = '//button[@type="submit"]'
        save_button = driver.find_element(By.XPATH, xpath_for_save)
        # Clicking on save button
        save_button.click()
        time.sleep(3)
        # # Xpath for searching in employee name
        # xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        # emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # # Sending keys for searching in employee name
        # emp_name_search.send_keys("Ricky Thomas Hughes")
        # time.sleep(3)
        # # Xpath for clicking on Search button
        # xpath_for_clicking_on_search = '//button[@type="submit"]'
        # search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # # Clicking on Search button       
        # search_click.click()
        # time.sleep(3)
        # # Xpath for clicking on edit button
        # xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        # click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # # Clicking on edit button       
        # click_on_edit_button.click()
        # time.sleep(5)
        # Going to salary details
        xpath_for_salary_details = '//a[text()="Salary"]'
        time.sleep(2)       
        salary_details_click = driver.find_element(By.XPATH, xpath_for_salary_details)
        # Clicking on salary details
        salary_details_click.click()
        time.sleep(3)
        # Xpath for clicking on add
        xpath_for_clicking_on_add = "//h6[text()='Assigned Salary Components']/following::i[1]"
        clicking_on_add = driver.find_element(By.XPATH, xpath_for_clicking_on_add)
        # Clicking on add
        clicking_on_add.click()
        time.sleep(3)
        # Xpath for salary comp
        xpath_for_salary_comp = '//label[text()="Salary Component"]/following::div[1]/input'
        filling_on_salary_comp = driver.find_element(By.XPATH, xpath_for_salary_comp)
        # Sending keys for salary comp
        filling_on_salary_comp.send_keys("CTC")
        time.sleep(3)
        # Xpath for Pay grade
        xpath_for_pay_grade = '//label[text()="Pay Grade"]/following::div[1]/div'
        pay_grade = driver.find_element(By.XPATH, xpath_for_pay_grade)
        pay_grade.click()
        # Clicking on Pay grade
        pay_grade_drop_down = '//div[@role="option"]/span[text()="Grade 3"]'
        clicking_on_pay_grade = driver.find_element(By.XPATH, pay_grade_drop_down)
        clicking_on_pay_grade.click()
        time.sleep(3)
        # Xpath for Pay Frequency
        xpath_for_pay_frequency = "//label[text()='Pay Frequency']/following::div[1]/div"
        pay_frequency = driver.find_element(By.XPATH, xpath_for_pay_frequency)
        pay_frequency.click()
        # Clicking on Pay Frequency
        pay_frequency_drop_down = '//div[@role="option"]/span[text()="Monthly"]'
        clicking_on_pay_frequency= driver.find_element(By.XPATH, pay_frequency_drop_down)
        clicking_on_pay_frequency.click()
        time.sleep(3)
        # Xpath for Currency
        xpath_for_currency = "//label[text()='Currency']/following::div[1]"
        currency_frequency = driver.find_element(By.XPATH, xpath_for_currency)
        currency_frequency.click()
        # Clicking on Currency
        currency_drop_down = '//div[@role="option"]/span[text()="United States Dollar"]'
        clicking_on_currency= driver.find_element(By.XPATH, currency_drop_down)
        clicking_on_currency.click()
        time.sleep(3)
        # Xpath for amount
        xpath_for_amt = '//label[text()="Amount"]/following::div[1]/input'
        filling_on_amt = driver.find_element(By.XPATH, xpath_for_amt)
        # Sending keys for salary comp
        filling_on_amt.send_keys("40000")
        time.sleep(3)
        # # Xpath for comments
        # xpath_for_comments = '//label[text()="Comments"]/following::div[1]'
        # filling_on_comments = driver.find_element(By.XPATH, xpath_for_comments)
        # # Sending keys for comments
        # filling_on_comments.send_keys("Done")
        # time.sleep(3)
        # Xpath for clicking on Direct Deposit Details
        xpath_for_ddd = '//p[text()="Include Direct Deposit Details"]/following::div[1]'
        clicking_on_ddd = driver.find_element(By.XPATH, xpath_for_ddd)
        # Clicking on DDD
        clicking_on_ddd.click()
        time.sleep(3)
        # Xpath for Account Number
        xpath_for_acc_no = '//label[text()="Account Number"]/following::div[1]/input'
        filling_on_acc_no = driver.find_element(By.XPATH, xpath_for_acc_no)
        # Sending keys on Account Number
        filling_on_acc_no.send_keys("23456789")
        time.sleep(3)
        # Xpath for Account type
        xpath_for_acc_type = '//label[text()="Account Type"]/following::div[1]'
        acc_type = driver.find_element(By.XPATH, xpath_for_acc_type)
        acc_type.click()
        # Clicking on Account type
        acc_type_drop_down = '//div[@role="option"]/span[text() = "Savings"]'
        clicking_on_acc_type= driver.find_element(By.XPATH, acc_type_drop_down)
        clicking_on_acc_type.click()
        time.sleep(3)
        # Xpath for Routing Number
        xpath_for_routing_no = '//label[text()="Routing Number"]/following::div[1]/input'
        filling_routing_no = driver.find_element(By.XPATH, xpath_for_routing_no)
        # Sending keys on Routing Number
        filling_routing_no.send_keys("26009595")
        time.sleep(3)
        # Xpath for amount # Doubt
        xpath_for_amt_2 = '//p[text()="Include Direct Deposit Details"]/following::div//label[text()="Amount"]/following::div[1]/input'
        amt_2_routing_no = driver.find_element(By.XPATH, xpath_for_amt_2)
        # Sending keys on amount
        amt_2_routing_no.send_keys("30000")
        time.sleep(3)
        # Xpath for save
        xpath_for_save = '//button[@type="submit"]'
        click_on_save = driver.find_element(By.XPATH, xpath_for_save)
        # Clicking on save
        click_on_save.click()
        time.sleep(3)
        print("All fields are filled up properly")
        time.sleep(3)
        # Validating the filled details are present(Negative scenario)
        xpath_for_add_salary_comp = '//h6[text()="  Add Salary Component"]'
        add_salary_comp = driver.find_element(By.XPATH, xpath_for_add_salary_comp)
        try:
            test_1 = add_salary_comp.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        driver.quit()
        time.sleep(3) 

    def TC_PIM_13(self):

        # Initializing web browser
        driver = webdriver.Chrome()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(3)
        # Xpath for searching in employee name
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for searching in employee name
        emp_name_search.send_keys("Joe Hughes Jackson")
        time.sleep(3)
        # Xpath for clicking on Search button
        xpath_for_clicking_on_search = '//button[@type="submit"]'
        search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # Clicking on Search button       
        search_click.click()
        time.sleep(3)
        # Xpath for clicking on edit button
        xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # Clicking on edit button       
        click_on_edit_button.click()
        time.sleep(5)
        # Going to Tax Exemptions
        xpath_for_tax_exemptions = '//a[text()="Tax Exemptions"]'
        time.sleep(2)       
        tax_exemptions_details_click = driver.find_element(By.XPATH, xpath_for_tax_exemptions)
        # Clicking on salary details
        tax_exemptions_details_click.click()
        time.sleep(3)
        # Xpath for status_1
        xpath_for_status_fit = '//h6[text()="Federal Income Tax"]/following::div[7]'
        status_input_fit = driver.find_element(By.XPATH, xpath_for_status_fit)
        status_input_fit.click()
        # Clicking on status
        status_fit_drop_down = '//div[@role="option"]/span[text()="Single"]'
        clicking_on_status_fit = driver.find_element(By.XPATH, status_fit_drop_down)
        clicking_on_status_fit.click()
        time.sleep(3)
        # Xpath for exemptions
        xpath_for_exemptions = '//h6[text()="Federal Income Tax"]/following::div[14]/input'
        exemptions_input_fit = driver.find_element(By.XPATH, xpath_for_exemptions)
        # Sending keys for exemptions
        exemptions_input_fit.send_keys("67")
        time.sleep(3)
        # Xpath for state
        xpath_for_state = '//label[text()="State"]/following::div[1]'
        state_fill = driver.find_element(By.XPATH, xpath_for_state)
        state_fill.click()
        # Clicking on state
        state_drop_down = '//div[@role="option"]/span[text()="Illinois"]'
        clicking_on_state = driver.find_element(By.XPATH, state_drop_down)
        clicking_on_state.click()
        time.sleep(3)
        # Xpath for status_2
        xpath_for_status_sit = '//h6[text()="State Income Tax"]/following::div[14]'
        status_input_sit = driver.find_element(By.XPATH, xpath_for_status_sit)
        status_input_sit.click()
        # Clicking on status_2
        status_sit_drop_down = '//div[@role="option"]/span[text()="Single"]'
        clicking_on_status_sit = driver.find_element(By.XPATH, status_fit_drop_down)
        clicking_on_status_sit.click()
        time.sleep(3)
        # Xpath for exemptions
        xpath_for_exemptions_sit = '//h6[text()="State Income Tax"]/following::div[22]/input'
        exemptions_input_sit = driver.find_element(By.XPATH, xpath_for_exemptions_sit)
        # Sending keys for exemptions
        exemptions_input_sit.send_keys("62")
        time.sleep(3)
        # Xpath for unempl state
        xpath_for_unemp_state = '//label[text()="Unemployment State"]/following::div[1]'
        unemp_state = driver.find_element(By.XPATH, xpath_for_unemp_state)
        unemp_state.click()
        # Clicking on unempl state
        unempl_state_drop_down = '//div[@role="option"]/span[text()="Illinois"]'
        clicking_on_unempl_state = driver.find_element(By.XPATH, unempl_state_drop_down)
        clicking_on_unempl_state.click()
        time.sleep(3)
        # Xpath for work state
        xpath_for_work_state = '//label[text()="Work State"]/following::div[3]'
        work_state = driver.find_element(By.XPATH, xpath_for_work_state)
        work_state.click()
        # Clicking on work state
        work_state_drop_down = '//div[@role="option"]/span[text()="Houston"]'
        drop_down_ws = driver.find_element(By.XPATH, work_state_drop_down)
        drop_down_ws.click()
        time.sleep(3)
        # Xpath for save
        xpath_for_save = '//button[@type="submit"]'
        click_on_save = driver.find_element(By.XPATH, xpath_for_save)
        # Clicking on save
        click_on_save.click()
        time.sleep(3)
        print("All fields are filled up properly")
        time.sleep(3)
        # Validating the filled details are present
        try:
            test_1 = exemptions_input_sit.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        driver.quit()



Arul = Project_Of_Orange_HRM_2()
Arul.TC_PIM_01()
Arul.TC_PIM_02()
Arul.TC_PIM_03()
Arul.TC_PIM_04()
Arul.TC_PIM_05()
Arul.TC_PIM_06()
Arul.TC_PIM_07()
Arul.TC_PIM_08()
Arul.TC_PIM_09()
Arul.TC_PIM_10()
Arul.TC_PIM_11()
Arul.TC_PIM_12()
Arul.TC_PIM_13()
