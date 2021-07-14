#Macro for NAVER remainder vaccines

### Python Version
    - python 3.7
### Environment
    - MacOS
### Description
    본 프로그램은 2020년부터 지속된 코로나 팬더믹 상황에 빠르게 백신 접종을 원하는 모든 사람들을 위해 제작되었습니다.
    본 프로그램의 기본 인터넷 브라우저 환경은 chrome 입니다.
        혹시 chrome 을 사용하지 않으시는 분들은 library.py 에 driver 교체 바랍니다.
    Created by seungw0n (stevenswjoeng@gmail.com)
    
### Function Descriptions
    installer.py
        - install_packages() : 필요한 library 설치
        - get_chrome_version() : 크롬 설치 및 자신의 크롬 버전 확인
        
### External Library
    Run installer
    - selenium, chromedriver-autoinstaller
    
    Result: ['chromedriver-autoinstaller', 'selenium', ...]
    
### Fix Errors
    - installer.get_chrome_version()
        ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1091)
    
        Solution) https://blog.minamiland.com/551