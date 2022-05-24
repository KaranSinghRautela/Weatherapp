from tkinter import *
import requests
import json
import geocoder

root=Tk()
root.title("Weather")
root.geometry("400x600")
root.resizable(False,False)
root.iconbitmap("kp.ico")
root["bg"]="cyan"
g=geocoder.ip('me')
global my_label
global my_label1
global my_label2
global my_label3
my_label=Label(root,text="",bg="cyan")
my_label.grid(row=2)
my_label1=Label(root,text="",bg="cyan")
my_label1.grid(row=3)
my_label2=Label(root,text="",bg="cyan")
my_label2.grid(row=4)
my_label3=Label(root,text="",bg="cyan")
my_label3.grid(row=5)



def getw(a):
	global e
	try:
		api_req=requests.get("https://api.weatherapi.com/v1/current.json?key=a13fea2e1e8b44de9a151903220505&q="+a+"&aqi=yes")
		api_load=json.loads(api_req.content)
		city=api_load["location"]["name"]
		region=api_load["location"]["region"]
		country=api_load["location"]["country"]
		localtime=api_load["location"]["localtime"]
		temp_c=api_load["current"]["temp_c"]
		con=api_load["current"]["condition"]["text"]
		winds=api_load["current"]["wind_kph"]
		wind_d=api_load["current"]["wind_dir"]
		pressure=api_load["current"]["pressure_mb"]
		precip=api_load["current"]["precip_mm"]
		hum=api_load["current"]["humidity"]
		feelslike=api_load["current"]["feelslike_c"]
		uv=api_load["current"]["uv"]
		co=api_load["current"]["air_quality"]["co"]
		no2=api_load["current"]["air_quality"]["no2"]
		o3=api_load["current"]["air_quality"]["o3"]
		so2=api_load["current"]["air_quality"]["so2"]
		pm2_5=api_load["current"]["air_quality"]["pm2_5"]
		pm10=api_load["current"]["air_quality"]["pm10"]
	except Exception as w:
		api_load="Error...."
	
	try:
		global my_label
		global my_label1
		global my_label2
		global my_label3
		my_label.grid_forget()
		my_label1.grid_forget()
		my_label2.grid_forget()
		my_label3.grid_forget()
		my_label=Label(root,text="Location:"+city+"\n"+region+"\n"+country+"\n"+localtime,padx=10,pady=10,font=("Helvetica",12),bg="cyan")
		my_label.grid(row=2,column=1,columnspan=2,pady=5)
		my_label1=Label(root,text="Temperature:"+str(temp_c)+"°"+"\n"+"Real Feel:"+str(feelslike)+"°"+"\n"+con,font=("Helvetica",12),bg="cyan")
		my_label1.grid(row=3,column=1,columnspan=2,pady=5)
		my_label2=Label(root,text="Wind Speed(kph):"+str(winds)+"\n"+"Wind Direction:"+wind_d+"\n"+"Pressure(mb):"+str(pressure)+"\n"
			+"Precipitation(mm):"+str(precip)+"\n"+"Humidity:"+str(hum)+"%"+"\n"+"UV:"+str(uv),padx=10,pady=10,font=("Helvetica",12),bg="cyan")
		my_label2.grid(row=4,column=1,columnspan=2,pady=5)
		my_label3=Label(root,text="Air Quality"+"\n"+"co(ug/m3):"+str(co)+"\n"+"no2(ug/m3):"+str(no2)+"\n"+"so2(ug/m3):"+str(so2)+"\n"+
			"pm2.5(ug/m3):"+str(pm2_5)+"\n"+"pm10(ug/m3):"+str(pm10)+"\n"+"o3(ug/m3):"+str(o3),font=("Helvetica",12),bg="cyan")
		my_label3 .grid(row=5,column=1,columnspan=2,pady=5)
	except Exception as q:
		e.delete(0,END)
		e.insert(0,"No such city")

getw(g.city)
my_label4=Label(root,text="Enter city name:",pady=8,padx=10,font=("Helvetica",11,"bold"),bg='cyan').grid(row=0,column=1,pady=20,padx=30)
global e
e=Entry(root,bd=2,font=("Helvetica",12),bg="light cyan")
e.grid(row=0,column=2)
b=Button(root,text="Enter",command=lambda: getw(e.get()),padx=10,pady=6,font=("Helvetica",11,"bold"),bg="light cyan").grid(row=1,column=1,columnspan=2)
root.mainloop()