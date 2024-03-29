from bs4 import BeautifulSoup
import requests
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse, urljoin
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

genes = []



with open('Gene_names.txt', 'r') as texto:
	for line in texto:
		linha = line.split()
		if len(linha) > 0:
			genes.append(linha[0])
			
files = os.listdir('download/')
total = len(genes)
done_genes = []

for file in files:
	done_genes.append(file[:-4]) 

genes = [value for value in genes if value not in done_genes]



def main():
	start_time = time.time()
	i = 0
	download_dir = '~/Desktop/Coding/timer2scraper/download'
	firefox_options = Options()
	firefox_options.set_preference("browser.download.folderList", 2)
	firefox_options.set_preference("browser.download.dir", download_dir)
	firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/pdf")  # Specify MIME types
	firefox_options.set_preference("pdfjs.disabled", True)  # Disable the built-in PDF viewer
	#firefox_options.add_argument('--headless')
	driver = webdriver.Firefox(options=firefox_options)
	driver.get('http://timer.comp-genomics.org/timer/')
	button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'jumpToGenede')))
	button.click()
	input_element = driver.find_element(By.ID, 'genedeInput_gene-selectized')
	driver.execute_script("arguments[0].scrollIntoView(true);", input_element)

	# Wait for the element to be visible
	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of(input_element))

	# Create an ActionChains instance
	action_chains = ActionChains(driver)

	# Move to the element to ensure it is in the viewable area
	action_chains.move_to_element(input_element).perform()

	# Click on the input field to activate the dropdown
	input_element.click()

	# Use ActionChains to send the down arrow key
	action_chains.send_keys(Keys.ARROW_DOWN).perform()

	# Select the first value by sending the Enter key
	action_chains.send_keys(Keys.BACKSPACE).perform()

        # Press Enter to select the typed value
	action_chains.send_keys(Keys.RETURN).perform()
	input_element.click()
	count=len(done_genes)
	i=0
	for value in genes:
		sleep(2)
		input_element = driver.find_element(By.ID, 'genedeInput_gene-selectized')

		# Type the new value into the input field
		input_element.send_keys(Keys.BACKSPACE)  # Clear the existing value
		input_element.send_keys(value)
		sleep(2)
		input_element.send_keys(Keys.ARROW_UP)
		input_element.send_keys(Keys.ARROW_UP)
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)		
		input_element.send_keys(Keys.ARROW_UP)
		input_element.send_keys(Keys.ARROW_UP)
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ARROW_UP)				
		input_element.send_keys(Keys.ENTER)

		sleep(2)
		button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "genedeInput_submit")))
		try:
			button.click()
		except:
			driver.close()
			main()
		sleep(8)
		try:
			warn_element = WebDriverWait(driver,10).until(lambda x: 'Gene symbol must be provided!' in x.page_source)
			print(warn_element)
			name = 'download/' + value + '.csv'
			i+=1
			with open(name,'w') as texto:
				texto.write(',')
				pass
			continue
		except:
			pass
		button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "downloadTXT4")))
		button.click()
		sleep(10)
		os.rename('/home/luciane/Desktop/Coding/timer2scraper/download/genede.csv',f'/home/luciane/Desktop/Coding/timer2scraper/download/{value}.csv')
		sleep(2)
		count+=1
		i+=1
		end_time = time.time()
		elapsed_time = end_time - start_time
		mean_time = round(elapsed_time/i, 2)
		print(f'Done: {count}/{total} ({mean_time} s/gene)')

main()	
	
	



