from flask import Flask
import time
from selenium import webdriver


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello world!</h1>"

@app.route('/test')
def test():
    driver=webdriver.PhantomJS(executable_path='bin/phantomjs')
    driver.get("https://www.baidu.com/")
    time.sleep(3)
    news = driver.find_element_by_class_name('mnav').text
    return news


