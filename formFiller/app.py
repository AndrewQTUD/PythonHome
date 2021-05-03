from selenium import webdriver

web = webdriver.Firefox(
    executable_path=r'C:\\Users\andyt\Desktop\geckodriver.exe')

web.get('https://fcbayern.com/en/fans/crm-aktionen/musiala')
