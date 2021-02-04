import speech_recognition as sr

def speech(prompt = ""):
	r = sr.Recognizer()
	with sr.Microphone() as source: # source -> microphone
		print(f"{prompt}: ")
		audio = r.listen(source)

		text = r.recognize_google(audio)
		return text

