import sys
import win32com.client as wincl
def text2Speech(text):
	service=wincl.Dispatch("SAPI.SpVoice")
	service.Speak(text)
for i in range(10):
     text2Speech(input("enter your text to listen its audio:-"))
     input()
sys.exit()
