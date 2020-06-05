from bs4 import  BeautifulSoup
import requests
class Corona():
      def __init__(self,keyword):
            self.keyword = keyword
      
      def get_info(self):
            key = self.keyword
            url = 'https://www.worldometers.info/coronavirus/country/{}/'.format(key)
            try:
                  response = requests.get(url)
                  soup = BeautifulSoup(response.text,'html.parser')
                  data = soup.findAll('div',{'class':'maincounter-number'})
                  #print("Current Covid-19 India Report")
                  new_data = []
                  parsed_data = list()
                  for tc in range(0,len(data)):
                        new_data.append(data[tc].text)
                  parsed_data = [new_data[0], new_data[1], new_data[2]]
                  return str(parsed_data)
            except :
                  return 'Error While Getting Data'



obj = Corona('China')
res = obj.get_info()
data = res.split("\n")
