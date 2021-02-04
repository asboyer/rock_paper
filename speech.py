import speech_recognition as sr

def speech(prompt = ""):
	r = sr.Recognizer()
	with sr.Microphone() as source: # source -> microphone
		print(f"{prompt}: ")
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			return text
		except:
			print("Sorry, I couldn't recognize your voice.")
			return "askdjf kajsfd; j;klj"
