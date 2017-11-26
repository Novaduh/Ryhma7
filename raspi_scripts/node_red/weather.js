if(msg.payload.weather_icon == 1)
    msg.payload = "Selkeää"
else if(msg.payload.weather_icon == 2)
    msg.payload = "Puolipilvistä"
else if(msg.payload.weather_icon == 3)
    msg.payload = "Pilvistä"
else if(msg.payload.weather_icon == 21)
    msg.payload = "Heikkoja sadekuuroja"
else if(msg.payload.weather_icon == 22)
    msg.payload = "Sadekuuroja"
else if(msg.payload.weather_icon == 23)
    msg.payload = "Voimakkaita sadekuuroja"
else if(msg.payload.weather_icon == 31)
    msg.payload = "Heikkoa vesisadetta"
else if(msg.payload.weather_icon == 32)
    msg.payload = "Vesisadetta"
else if(msg.payload.weather_icon == 33)
    msg.payload = "Voimakasta vesisadetta"
else if(msg.payload.weather_icon == 41)
    msg.payload = "Heikkoja lumikuuroja"
else if(msg.payload.weather_icon == 42)
    msg.payload = "Lumikuuroja"
else if(msg.payload.weather_icon == 43)
    msg.payload = "Voimakkaita lumikuuroja"
else if(msg.payload.weather_icon == 51)
    msg.payload = "Heikkoa lumisadetta"
else if(msg.payload.weather_icon == 52)
    msg.payload = "Lumisadetta"
else if(msg.payload.weather_icon == 53)
    msg.payload = "Voimakasta lumisadetta"
else if(msg.payload.weather_icon == 61)
    msg.payload = "Ukkoskuuroja"
else if(msg.payload.weather_icon == 62)
    msg.payload = "Voimakkaita ukkoskuuroja"
else if(msg.payload.weather_icon == 63)
    msg.payload = "Ukkosta"
else if(msg.payload.weather_icon == 64)
    msg.payload = "Voimakasta ukkosta"
else if(msg.payload.weather_icon == 71)
    msg.payload = "Heikkoja räntäkuuroja"
else if(msg.payload.weather_icon == 72)
    msg.payload = "Räntäkuuroja"
else if(msg.payload.weather_icon == 73)
    msg.payload = "Voimakkaita räntäkuuroja"
else if(msg.payload.weather_icon == 81)
    msg.payload = "Heikkoa räntäsadetta"
else if(msg.payload.weather_icon == 82)
    msg.payload = "Räntäsadetta"
else if(msg.payload.weather_icon == 83)
    msg.payload = "Voimakasta räntäsadetta"
else if(msg.payload.weather_icon == 91)
    msg.payload = "Utua"
else if(msg.payload.weather_icon == 92)
    msg.payload = "Sumua"
return msg;
