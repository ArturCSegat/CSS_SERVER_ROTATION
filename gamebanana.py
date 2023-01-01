from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


"""This fie handles scraping data from gamebanana, as it is the most time consuming and the most intensive operation
to be performed it will be done in the server host's computer"""


"""This function gets the map link from the search term, it should be used to prompt the user if the map found is correct"""
def get_map_from_name(term):

    term.replace(" ", "+")

    url = f"https://gamebanana.com/search?_nPage=1&_sOrder=best_match&_sSearchString={term}+cs+source"




    # Set the path to the webdriver executable
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path="./geckodriver.exe")
    

    # Open the website in the web browser
    driver.get(url)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Name"))
    )

    first_map = driver.find_element(By.CLASS_NAME, "Name")


    # Get the element's position on the page
    position = first_map.location

    # Scroll the page to bring the element into view
    driver.execute_script(f"window.scrollTo({position['x']-200}, {position['y']-200})")
    
    first_map.click()

    e = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "DownloadOptions"))
    )

    map_link = driver.current_url

    driver.close()

    return map_link



"""Given the donwload link (wich should be aquired trough get_map_from_link) this function return an object with atributes
such as the url for donwloading the map, this should be called and used as a parameter for the api call"""
def get_download_link_from_link(link):

    
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path="./geckodriver.exe")

    driver.get(link)
    
    map_name = driver.find_element(By.ID, "PageTitle").text

    download = driver.find_element(By.CLASS_NAME, "GreenColor")

    position = download.location
    
    driver.execute_script(f"window.scrollTo({position['x']-200}, {position['y']-200})")


    download.click()


    a = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "DownloadOptions"))
    )

    download_link = driver.current_url

    driver.close()

    download_id = download_link.split("#FileInfo_")





    return {'map_url':link,'download_url':f"https://gamebanana.com/dl/{download_id[1]}","name": map_name, "download_id": download_id[1]}




