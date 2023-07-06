import speech_recognition as s_r
from speech_to_text_transcriber import SpeechToTextTranscriber

def main():
    print("Your speech_recognition version is: "+s_r.__version__)
    codeword_start = "Whisper"
    codeword_pause = "Pause"
    codeword_end = "Bye Bye"
    idle_timeout = 2
    language = "en-IN"
    accent = "indian"

    transcriber = SpeechToTextTranscriber(codeword_start, codeword_pause, codeword_end, idle_timeout, language, accent)
    transcriber.start_transcribing()
    # r = s_r.Recognizer()
    # my_mic_device = s_r.Microphone(device_index=1)
    # with my_mic_device as source:
    #     print("Say what you want to calculate, example: 3 plus 3")
    #     r.adjust_for_ambient_noise(source)
    #     audio = r.listen(source)
    # my_string=r.recognize_google(audio)
    # print(my_string)

if __name__ == "__main__":
    main()
