from flask import Flask, render_template, request
import configparser
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')

def weather_dashboard():
 return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
 zip_code = request.form['zipCode']    
 return "Zip Code: " + zip_code

def get_api_key():
 config = configparser.ConfigParser()
 config.read('config.ini')
 return config['openweathermap']['api']

def get_weather_results(zip_code, api_key):
 api_url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
 r = requests.get(api_url)
 return r.json()

if __name__ == '__main__':app.run()

