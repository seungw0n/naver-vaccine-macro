# Macro for NAVER remainder vaccines

### Python Version
    - python 3.7

### Environment
    - Compatiable with macOS
    - Works in Chrome
    
 
### Description
    본 프로그램은 2020년부터 지속된 코로나 팬더믹 상황에 빠르게 백신 접종을 원하는 모든 사람들을 위해 제작되었습니다.
    현재 배포중인 잔여백신 매크로 프로그램을 상업적인 목적으로 배포를 하는 경우가 많습니다.
    본 프로그램은 "무료"입니다.
    
    간단한 python 구동 방식만 알면 실행 시킬 수 있도록 제작했습니다.
    구동 방식은 "How to run"을 참조해주세요.
    궁금한 부분, 불편한 부분, 혹은 추가되었으면 하는 features 들은 밑 이메일 혹은 github 로 연락 바랍니다.
    
    본 프로그램은 Chrome 에서만 작동합니다.
    
    Created by seungw0n (stevenswjoeng@gmail.com)

### How to run
    1) Scripts 을 clone 혹은 저장 (tester.py 제외)
    2) packages 설치하기 (if needed)
        setup.install_chrome(), setup.install_packages() - main.py 에 주석처리 해놓았습니다.
    3) main.py 을 run 하기
    4) 네이버 로그인 페이지가 켜지면 제한시간(default: 20sec)내에 로그인 하기
    5) 네이버 잔여백신 페이지가 켜지면 제한시간(default: 20sec)내에 원하는 위치 설정하기
    

### Function Descriptions
    installer.py
        - install_packages() : 필요한 library 설치
        - install_chrome() : 크롬 설치 및 자신의 크롬 버전 확인
        - setup_driver() : 리턴 크롬 드라이버
        
    library.py
        - wait(aTime) : aTime 만큼 pause
        - move_page(driver, url) : url 주소로 이동
        - open_list(driver) : 병원 목록 오픈
        - refresh(driver) : 새로고침 (잔여백신용)
        - clickOne(driver), clickTwo(driver) : 예약
        
    
        
### External Library
    Everything will be installed if you run setup.install_packages()
    - selenium, chromedriver-autoinstaller, pyautogui(not used)

### Update
    - 15 Jul 2021: Chrome이 없으신 분들은 setup.py 의 install 함수를 실행시켜주세요.
    - 19 Jul 2021: Fixed Selenium's Element Is Not Clickable at Point error. But still not optimized yet.
    

### Common Errors - will be updated
    - installer.get_chrome_version()
        ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1091)
    
        Solution) https://blog.minamiland.com/551
        
    - pyautogui not working
        Security feature where you must explicitly allow applications to use your mouse/keyboard.
        Security Preferences > Security & Privacy > Privacy > Accessibility
        You might have to allow your terminal application (PyCharm, etc) in the list.