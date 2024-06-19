from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
newarr=[]
Page=1
while Page <= 10:
    response=requests.get(f'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&page={Page}')
    soup=BeautifulSoup(response.text,'html.parser')
    for flip in soup.find_all('div',class_="_13oc-S"):
        Mobile_Name=flip.find('div',class_="_4rR01T").text
        List=flip.find_all('li',class_="rgWa7D")
        if(len(List)==6):
            newarr.append({
            "Mobile_Name":Mobile_Name,
            "Storage":List[0].text,
            "display":List[1].text,
            "camera":List[2].text,
            "battery":List[3].text,
            "processor":List[4].text
            })
        else:
            newarr.append({
            "Mobile_Name":Mobile_Name,
            "Storage":List[0].text,
            "display":List[1].text,
            "camera":List[2].text,
            "battery":List[3].text,
            "processor":'Not Mentioned'
            })
    Page=Page+1
workbook = Workbook()
sheet = workbook.active

 # Add headers
headers = ["Mobile_Name", "Storage", "display", "camera", "battery", "processor"]
sheet.append(headers)

# Append data from newarr to the Excel file
for item in newarr:
    row = [item[column] for column in headers]
    sheet.append(row)

# Save the workbook
workbook.save(filename="Mobile_Data.xlsx")

print("")