#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Chrome WebDriver 경로 설정
driver_path = './chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# 웹사이트 열기
driver.get('https://www.aytennis.or.kr/')

# 로그인 페이지로 이동
login_button_xpath = "/html/body/header/div/div[1]/div/div/div[2]/div/ul/li[1]/a"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath))).click()

# ID 및 PWD 입력
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/section/div/form/ul/li[1]/input[2]"))).send_keys('audfo2002')
driver.find_element(By.XPATH, "/html/body/div/section/div/form/ul/li[2]/input[2]").send_keys('sucksex12')

# 로그인 버튼 클릭
driver.find_element(By.XPATH, "/html/body/div/section/div/form/div[2]/button").click()

# 코트예약 페이지로 이동
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/div/nav/ul/li[3]/a/i"))).click()

# 중앙코트 선택
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div[2]/div/div/div[2]/div/nav/ul/li[3]/ul/li[6]/a"))).click()

# 원하는 체크박스의 value 값을 기준으로 해당 체크박스를 찾기
desired_value_1 = "2024-04-14|4|18|06|3500"
desired_value_2 = "2024-04-14|4|18|07|3500"

checkboxes = driver.find_elements(By.CSS_SELECTOR, f"input[type='checkbox'][value='{desired_value_1}']")
# # 예약 페이지의 특정 요소(예: 첫 번째 체크박스)가 나타날 때까지 최대 10초 대기
# first_checkbox_selector = "CSS_Selector_or_XPath_of_First_Checkbox_In_Reservation_Page"
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, first_checkbox_selector)))

while True:
    # 원하는 체크박스의 value 값을 기준으로 해당 체크박스를 찾기
    checkbox_value_1 = "2024-04-05|4|18|06|3500"
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[type='checkbox'][value='{checkbox_value_1}']")))

    checkbox_value_2 = "2024-04-05|4|18|07|3500"
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[type='checkbox'][value='{checkbox_value_2}']")))
    time.sleep(100)
    
# %%

