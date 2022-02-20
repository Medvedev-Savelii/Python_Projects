

	final_info = condition + '\n' + str(temp) + "°C" 
	final_data = "\n"+ 'Min Temp: ' + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" +"Sunrise: "  + sunrise + "\n" + "Sunset: " + sunset
	label1.config(text= final_info)
	label2.config(text= final_data)



canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()






canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title('Weather App')

f = ('poppins', 15, 'bold')
t = ('poppins', 35, 'bold')

textfiled = tk.Entry(canvas,justify='center', width= 20, font = t)
textfiled.pack(pady = 20)
textfiled.focus()
