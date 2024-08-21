from tkinter import *
from PIL import ImageTk,Image
import requests

url="https://api.openweathermap.org/data/2.5/weather"
api_key="18430610dd10b19ca4c1997c79361e26" #Enter your own API key
iconUrl='https://openweathermap.org/img/wn/{}@2x.png'

def getWeather(city):
    params = {'q':city,'appid':api_key}
    data=requests.get(url,params=params).json()
    if data:
        city=data["name"].capitalize()
        country=data["sys"]["country"]
        temp=int(data["main"]["temp"] - 273)
        icon =data["weather"][0]["icon"]
        condition = data["weather"][0]["description"]
        return (city,country,temp,icon,condition)

def main():
    city= cityEntry.get()
    weather =getWeather(city)
    if weather:
        locationLabel["text"]='{},{}'.format(weather[0],weather[1])
        tempLabel["text"]= '{}°C'.format(weather[2])
        conditionLabel["text"]=weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]),stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image=icon

app = Tk()
app.geometry('300x450')
app.title('AY Weather App')

cityEntry=Entry(app,justify="center")
cityEntry.pack(fill=BOTH,ipady=10,padx=18,pady=5)
cityEntry.focus()

searchButton=Button(app,text="Search",font=("Ariel",15),command=main)
searchButton.pack(fill=BOTH,ipady=10,padx=20)

iconLabel=Label(app)
iconLabel.pack()

locationLabel=Label(app,font=("Ariel",40))
locationLabel.pack()

tempLabel=Label(app,font=("Ariel",50,"bold"))
tempLabel.pack()

conditionLabel = Label(app,font=("Ariel",20))
conditionLabel.pack()

app.mainloop()