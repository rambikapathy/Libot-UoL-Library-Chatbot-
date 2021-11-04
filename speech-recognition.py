#speech recognition
#use 'pip install SpeechRecognition' and 'pip install pyaudio' to allow use of microphone with python

def voice():
	import speech_recognition as speech
	robot = speech.Recognizer()
	microphone = speech.Microphone()
	with microphone as source:
		print("Please speak.")
		audio = robot.listen(source) #recieves voice input from microphone
	try:
		print("The sentence was: " + robot.recognize_google(audio)) #outputs voice input as text
		s = robot.recognize_google(audio) #currently using google speech recognition
		return s
	except speech.UnknownValueError:
		print("Not understood, sorry.")
	except speech.RequestError:
		print("Something went wrong, error {0}".format(error))
	except speech.UnboundLocalError:
		print("Something went wrong, error {0}".format(error))

sentence = voice()

#basic inputs and outputs to test but replace these with library Q&A
#allow multiple inputs/use language detection
while True:
	if sentence == "hello": #input
		print("hi") #output
	if sentence == "bye":
		print("goodbye")
		break
	sentence = voice()
