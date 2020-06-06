from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from bs4 import  BeautifulSoup
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///corona.db'
db = SQLAlchemy(app)


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
                  data1 = soup.find('div',{'class':'number-table-main'}).text
                  data2 = soup.findAll('span',{'class':'number-table'})
                  totalCase = data1
                  recRate = data2[0].text
                  deathRate = data2[1].text
                  #print("Current Covid-19 India Report")
                  new_data = []
                  parsed_data = ""
                  for tc in range(0,len(data)):
                        new_data.append(data[tc].text)
                  active_case = new_data[0]
                  death = new_data[1]
                  recovered = new_data[2]
                  return active_case, death, recovered,recRate,deathRate,totalCase
                  
            except :
                  return 'Error While Getting Data'


class CoronaDefault():
      def __init__(self):
            self.keyword = ''
      
      def get_info(self):
            url = 'https://www.worldometers.info/coronavirus/'
            try:
                  response = requests.get(url)
                  soup = BeautifulSoup(response.text,'html.parser')
                  data = soup.findAll('div',{'class':'maincounter-number'})
                  data1 = soup.find('div',{'class':'number-table-main'}).text
                  data2 = soup.findAll('span',{'class':'number-table'})
                  totalCase = data1
                  recRate = data2[0].text
                  deathRate = data2[1].text
                  #print("Current Covid-19 India Report")
                  new_data = []
                  parsed_data = ""
                  for tc in range(0,len(data)):
                        new_data.append(data[tc].text)
                  active_case = new_data[0]
                  death = new_data[1]
                  recovered = new_data[2]
                  return active_case, death, recovered,recRate,deathRate,totalCase
                  
            except :
                  return 'Error While Getting Data'









@app.route('/', methods=['POST','GET'])
def start_app():
      if request.method == "POST":
            keyword = request.form['content']
            obj = Corona(keyword)
            active_case, death, recovered ,recRate,deathRate,totalCase= obj.get_info()
            return render_template('index.html',cases=active_case,death=death,recovered=recovered, recRate=recRate,deathRate=deathRate,totalCase=totalCase)
            
      else:
            default = CoronaDefault()
            active_case, death, recovered ,recRate,deathRate,totalCase= default.get_info()
            return render_template('index.html',cases=active_case,death=death,recovered=recovered,recRate=recRate, deathRate=deathRate,totalCase=totalCase)


if __name__ == "__main__":
      app.run(debug=True)