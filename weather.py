import requests as re,speech_recognition as sr,pyttsx3 as p

r=sr.Recognizer()

def checkWeather(cityName):
    p.speak(f"Checking the weather of {cityName}")
    response =re.get(f"http://api.weatherapi.com/v1/current.json?key=fb410b65058a4cafbc3205204251209&q={cityName}&aqi=no").json()
    try:
      city=response["location"]["name"]
      time=response["location"]["localtime"]
      temp=response["current"]["temp_c"]
      lat=response["location"]["lat"]
      lon=response["location"]["lon"]
      
      print(f"City: {city}\nDate and Time: {time}\nTemperature: {temp}°C\nLatitude: {lat},Longitude: {lon}\n ")
      p.speak(f"The weather of {cityName} is {temp}°C at {time}")
     
    except Exception as e:
     print("There is no such city\n",e)  
     p.speak("There is no such city\n",e)

def selectInput():
  p.speak("would you like to enter the city name by voice or text  ")
  print("would you like to enter the city name by voice or text  ".title())
  with sr.Microphone() as src:
    selectInputMethod=r.listen(src)
    selectInputMethod=r.recognize_google(selectInputMethod).lower()
    print(selectInputMethod)

  if "voice" in selectInputMethod:
     
     p.speak("Give the city name")
     print("Give the city name")

     with sr.Microphone() as src:
           cityName=r.listen(src)
           cityName=r.recognize_google(cityName).lower()
           cityName=cityName.split(" ")
           checkWeather(cityName[-1])
  elif "text" in selectInputMethod:
     cityName = input("Enter the city name: ").lower()
     checkWeather(cityName)
  else:
    p.speak("Invalid input method. Please select 'voice' or 'text'") 
    print("Invalid input method. Please select 'voice' or 'text'")
      
if __name__=="__main__":
 
 execute="max"
 p.speak(f"You can ask me about weather by saying {execute}")
 print(f"You can ask me about weather by saying {execute}".title())
 
 while True:

   try:
     with sr.Microphone() as src:
      userMessage=r.listen(src)
      userMessage=r.recognize_google(userMessage).lower()
      print(userMessage)

      if "exit" in userMessage :
        p.speak("Bye Bye")
        print("Bye Bye")
        break
      
      elif execute in userMessage:
       selectInput()
   except Exception as e:
     pass  
   