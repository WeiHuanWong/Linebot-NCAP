from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from requests import get
from bs4 import BeautifulSoup
import requests 
from urllib.request import urlretrieve

app=Flask(__name__)

line_bot_api=LineBotApi('HACqpoMm/ob0Y8xVmAZq/w/vPnNzbaNpkGZevUXwph9NuWbyxchrVm0mW4A/GAFHC1C6V7wI4lXZE806+U6sEGgESX2EwFV1vkwQVH+24oZwqVbOVElx/UiyHUI4fatBQvfYsGGeoGJr15aJSBiUyQdB04t89/1O/w1cDnyilFU=')
handler=WebhookHandler('6735ab4ed9ae2c1f4f5e3e165501443b')

@app.route('/')
def homepage():
	return "OK"
	
@app.route('/callback',methods=['POST'])
def callback():
	#get X-Line-Signature header value
	signature=request.headers['X-Line-Signature']
	#get request body as text
	body =request.get_data(as_text=True)
	app.logger.info("Request body:"+body)
	#handle webhook body
	try:
		handler.handle(body,signature)
	except:
		print("InvalidSignatureError")
	return 'OK'

def ncap_best2010():
    response=get('https://www.euroncap.com/zh/%E8%AF%84%E7%BA%A7%E5%92%8C%E5%A5%96%E9%A1%B9/%E6%9C%80%E4%BD%B3%E8%BD%A6%E5%9E%8B/'+'2010'+'/')
    page_html=BeautifulSoup(response.text,'html.parser')	
    content = ""


    for container in page_html.div.find_all(class_='car-container'):
        if container.find('div',class_='adult-occupant') is not None:
            
            names=container.find('div',class_="car-name").text
            name=(names.strip('\n').split(','))
        
            a=container.find('div',class_="car-images")
            picurl=(a.find('img')['src'])

            b=container.find('div',class_="car-movies")
            yturl=(b.find('img')['data'])
            content+='{}\n{}\n{}\n'.format(name,picurl,yturl)
    return content

def ncap_best2011():
    response=get('https://www.euroncap.com/zh/%E8%AF%84%E7%BA%A7%E5%92%8C%E5%A5%96%E9%A1%B9/%E6%9C%80%E4%BD%B3%E8%BD%A6%E5%9E%8B/'+'2011'+'/')
    page_html=BeautifulSoup(response.text,'html.parser')	
    content = ""


    for container in page_html.div.find_all(class_='car-container'):
        if container.find('div',class_='adult-occupant') is not None:
            
            names=container.find('div',class_="car-name").text
            name=(names.strip('\n').split(','))
        
            a=container.find('div',class_="car-images")
            picurl=(a.find('img')['src'])

            b=container.find('div',class_="car-movies")
            yturl=(b.find('img')['data'])
            content+='{}\n{}\n{}\n'.format(name,picurl,yturl)
    return content

def ncap_best2012():
    response=get('https://www.euroncap.com/zh/%E8%AF%84%E7%BA%A7%E5%92%8C%E5%A5%96%E9%A1%B9/%E6%9C%80%E4%BD%B3%E8%BD%A6%E5%9E%8B/'+'2012'+'/')
    page_html=BeautifulSoup(response.text,'html.parser')	
    content = ""


    for container in page_html.div.find_all(class_='car-container'):
        if container.find('div',class_='adult-occupant') is not None:
            
            names=container.find('div',class_="car-name").text
            name=(names.strip('\n').split(','))
        
            a=container.find('div',class_="car-images")
            picurl=(a.find('img')['src'])

            b=container.find('div',class_="car-movies")
            yturl=(b.find('img')['data'])
            content+='{}\n{}\n{}\n'.format(name,picurl,yturl)
    return content

def ncap_best2013():
    response=get('https://www.euroncap.com/zh/%E8%AF%84%E7%BA%A7%E5%92%8C%E5%A5%96%E9%A1%B9/%E6%9C%80%E4%BD%B3%E8%BD%A6%E5%9E%8B/'+'2013'+'/')
    page_html=BeautifulSoup(response.text,'html.parser')	
    content = ""


    for container in page_html.div.find_all(class_='car-container'):
        if container.find('div',class_='adult-occupant') is not None:
           
            names=container.find('div',class_="car-name").text
            name=(names.strip('\n').split(','))
        
            a=container.find('div',class_="car-images")
            picurl=(a.find('img')['src'])

            b=container.find('div',class_="car-movies")
            yturl=(b.find('img')['data'])
            content+='{}\n{}\n{}\n'.format(name,picurl,yturl)
    return content


def ncap_best2014():
    response=get('https://www.euroncap.com/zh/%E8%AF%84%E7%BA%A7%E5%92%8C%E5%A5%96%E9%A1%B9/%E6%9C%80%E4%BD%B3%E8%BD%A6%E5%9E%8B/'+'2014'+'/')
    page_html=BeautifulSoup(response.text,'html.parser')	
    content = ""


    for container in page_html.div.find_all(class_='car-container'):
        if container.find('div',class_='adult-occupant') is not None:
            
            names=container.find('div',class_="car-name").text
            name=(names.strip('\n').split(','))
        
            a=container.find('div',class_="car-images")
            picurl=(a.find('img')['src'])

            b=container.find('div',class_="car-movies")
            yturl=(b.find('img')['data'])
            content+='{}\n{}\n{}\n'.format(name,picurl,yturl)
    return content


def ncap_best2015():
    response=get('https://www.euroncap.com/zh/%E8%AF%84%E7%BA%A7%E5%92%8C%E5%A5%96%E9%A1%B9/%E6%9C%80%E4%BD%B3%E8%BD%A6%E5%9E%8B/'+'2015'+'/')
    page_html=BeautifulSoup(response.text,'html.parser')	
    content = ""


    for container in page_html.div.find_all(class_='car-container'):
        if container.find('div',class_='adult-occupant') is not None:
            
            names=container.find('div',class_="car-name").text
            name=(names.strip('\n').split(','))
        
            a=container.find('div',class_="car-images")
            picurl=(a.find('img')['src'])

            b=container.find('div',class_="car-movies")
            yturl=(b.find('img')['data'])
            content+='{}\n{}\n{}\n'.format(name,picurl,yturl)
    return content


def ncap_best2016():
    response=get('https://www.euroncap.com/zh/%E8%AF%84%E7%BA%A7%E5%92%8C%E5%A5%96%E9%A1%B9/%E6%9C%80%E4%BD%B3%E8%BD%A6%E5%9E%8B/'+'2016'+'/')
    page_html=BeautifulSoup(response.text,'html.parser')	
    content = ""


    for container in page_html.div.find_all(class_='car-container'):
        if container.find('div',class_='adult-occupant') is not None:
            
            names=container.find('div',class_="car-name").text
            name=(names.strip('\n').split(','))
        
            a=container.find('div',class_="car-images")
            picurl=(a.find('img')['src'])

            b=container.find('div',class_="car-movies")
            yturl=(b.find('img')['data'])
            content+='{}\n{}\n{}\n'.format(name,picurl,yturl)
    return content



def ncap_best2017():
    response=get('https://www.euroncap.com/zh/%E8%AF%84%E7%BA%A7%E5%92%8C%E5%A5%96%E9%A1%B9/%E6%9C%80%E4%BD%B3%E8%BD%A6%E5%9E%8B/'+'2017'+'/')
    print(response,'eoor')
    page_html=BeautifulSoup(response.text,'html.parser')
    print(page_html)	
    content = ""


    for container in page_html.div.find_all(class_='car-container'):
        if container.find('div',class_='adult-occupant') is not None:

            names=container.find('div',class_="car-name").text
            name=(names.strip('\n').split(','))
        
            a=container.find('div',class_="car-images")
            picurl=(a.find('img')['src'])

            b=container.find('div',class_="car-movies")
            yturl=(b.find('img')['data'])
            content+='{}\n{}\n{}\n'.format(name,picurl,yturl)
    return content


@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    if event.message.text == "2010最佳車型":
        n=ncap_best2010()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=n))
    elif event.message.text == "2011最佳車型":
        n=ncap_best2011()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=n))
    elif event.message.text == "2012最佳車型":
        n=ncap_best2012()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=n))
    elif event.message.text == "2013最佳車型":
        n=ncap_best2013()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=n))
    elif event.message.text == "2014最佳車型":
        n=ncap_best2014()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=n))
    elif event.message.text == "2015最佳車型":
        n=ncap_best2015()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=n))
    elif event.message.text == "2016最佳車型":
        n=ncap_best2016()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=n))
    elif event.message.text == "2017最佳車型":
        n=ncap_best2017()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=n))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


if __name__ == '__main__':
        app.run(debug=True,use_reloader=True)