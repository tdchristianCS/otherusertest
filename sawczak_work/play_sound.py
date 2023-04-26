import gtts
from playsound import playsound

chorus = "Peanut Butter Jelly Time"
tts = gtts.gTTS(chorus)
tts.save('hello.mp3')

for i in range(15):
    playsound('hello.mp3')
