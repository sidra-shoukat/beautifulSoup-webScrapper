from bs4 import BeautifulSoup
import requests

# Step 1: Fetch webpage
url = 'https://www.geeksforgeeks.org/courses'
web = requests.get(url)

# Step 2: Parse HTML content
soup = BeautifulSoup(web.content, "html.parser")

# Step 3: Find all anchor tags
data = soup.find_all('a')

# Step 4: Extract href attributes (links)
links = []
for dt in data:
    href = dt.get('href')
    if href:  # Only if href exists
        links.append(href)

# Step 5: Save to text file
path = 'D:/web scrapping/project_2/links.txt'
with open(path, 'w', encoding='utf-8') as f:
    for link in links:
        f.write(link + '\n')  # Use \n not /n

#Now text:
text='https://www.geeksforgeeks.org/ai-ml-ds/'
data=requests.get(text)
soup=BeautifulSoup(web.content, "html.parser")
spans=soup.find_all('span')
span_texts = []
for span in spans:
    text = span.get_text(strip=True)
    if text:
        span_texts.append(text)
path = 'D:/web scrapping/project_2/span_texts.txt'
with open(path, 'w', encoding='utf-8') as f:
    for text in span_texts:
        f.write(text + '\n')

ul = soup.find('ul') 

# Find all list items inside the list
if ul:
    items = ul.find_all('li')
    for item in items:
        print(item.get_text(strip=True))
path = 'D:/web scrapping/project_2/list_items.txt'
with open(path, 'w', encoding='utf-8') as f:
    for item in items:
        f.write(item.get_text(strip=True) + '\n')
