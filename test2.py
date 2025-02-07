from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

# 크롬 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 열지 않음
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 드라이버 설치 및 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 지정된 URL로 이동
url = "https://smartstore.naver.com/swagkey/products/10527708328"
driver.get(url)

# try:
#     # "구매하기" 버튼 찾기
#     buy_button = driver.find_element(By.XPATH, "//a[contains(text(), '구매하기')]")
    
#     if buy_button:
#         print("구매하기 버튼을 찾았습니다. 클릭합니다.")
#         ActionChains(driver).move_to_element(buy_button).click().perform()
#     else:
#         print("구매하기 버튼이 없습니다.")
# except Exception as e:
#     print("구매하기 버튼을 찾는 중 오류가 발생했습니다:", str(e))

# 드라이버 종료
driver.quit()
