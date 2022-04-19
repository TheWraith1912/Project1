from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time


driver = webdriver.Chrome()




url = "https://hayyatapps.com/API/v273__/Data/?article=18"
##url = "https://hayyatapps.com/API/v273__/Data/?article=11"



driver.get(url)
time.sleep(4)
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'id':'SGSR-table-1'})
rows = table.find_all('tr')
tabledata = []
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    tabledata.append([col for col in cols if col])

df = pd.DataFrame(tabledata, columns=['Player Name and Rating', 'Version', 'Target Buy Price (Max)', 'Target Selling Price (Min)', '% From Buy Price', 'Current Market Price (Est)', 'URL'])
df.to_excel("tablescrapeXB.xlsx", index=False)