# LANGUAGES = {
# 'af': 'afrikaans',
# 'sq': 'albanian',
# 'am': 'amharic',
# 'ar': 'arabic',
# 'hy': 'armenian',
# 'az': 'azerbaijani',
# 'eu': 'basque',
# 'be': 'belarusian',
# 'bn': 'bengali',
# 'bs': 'bosnian',
# 'bg': 'bulgarian',
# 'ca': 'catalan',
# 'ceb': 'cebuano',
# 'ny': 'chichewa',
# 'zh-cn': 'chinese (simplified)',
# 'zh-tw': 'chinese (traditional)',
# 'co': 'corsican',
# 'hr': 'croatian',
# 'cs': 'czech',
# 'da': 'danish',
# 'nl': 'dutch',
# 'en': 'english',
# 'eo': 'esperanto',
# 'et': 'estonian',
# 'tl': 'filipino',
# 'fi': 'finnish',
# 'fr': 'french',
# 'fy': 'frisian',
# 'gl': 'galician',
# 'ka': 'georgian',
# 'de': 'german',
# 'el': 'greek',
# 'gu': 'gujarati',
# 'ht': 'haitian creole',
# 'ha': 'hausa',
# 'haw': 'hawaiian',
# 'iw': 'hebrew',
# 'he': 'hebrew',
# 'hi': 'hindi',
# 'hmn': 'hmong',
# 'hu': 'hungarian',
# 'is': 'icelandic',
# 'ig': 'igbo',
# 'id': 'indonesian',
# 'ga': 'irish',
# 'it': 'italian',
# 'ja': 'japanese',
# 'jw': 'javanese',
# 'kn': 'kannada',
# 'kk': 'kazakh',
# 'km': 'khmer',
# 'ko': 'korean',
# 'ku': 'kurdish (kurmanji)',
# 'ky': 'kyrgyz',
# 'lo': 'lao',
# 'la': 'latin',
# 'lv': 'latvian',
# 'lt': 'lithuanian',
# 'lb': 'luxembourgish',

# 'mk': 'macedonian',
# 'mg': 'malagasy',
# 'ms': 'malay',
# 'ml': 'malayalam',
# 'mt': 'maltese',
# 'mi': 'maori',
# 'mr': 'marathi',
# 'mn': 'mongolian',
# 'my': 'myanmar (burmese)',
# 'ne': 'nepali',
# 'no': 'norwegian',
# 'or': 'odia',
# 'ps': 'pashto',
# 'fa': 'persian',
# 'pl': 'polish',
# 'pt': 'portuguese',
# 'pa': 'punjabi',
# 'ro': 'romanian',
# 'ru': 'russian',
# 'sm': 'samoan',
# 'gd': 'scots gaelic',
# 'sr': 'serbian',
# 'st': 'sesotho',
# 'sn': 'shona',
# 'sd': 'sindhi',
# 'si': 'sinhala',
# 'sk': 'slovak',
# 'sl': 'slovenian',
# 'so': 'somali',
# 'es': 'spanish',
# 'su': 'sundanese',
# 'sw': 'swahili',
# 'sv': 'swedish',
# 'tg': 'tajik',
# 'ta': 'tamil',
# 'te': 'telugu',
# 'th': 'thai',
# 'tr': 'turkish',
# 'uk': 'ukrainian',
# 'ur': 'urdu',
# 'ug': 'uyghur',
# 'uz': 'uzbek',
# 'vi': 'vietnamese',
# 'cy': 'welsh',
# 'xh': 'xhosa',
# 'yi': 'yiddish',
# 'yo': 'yoruba',
# 'zu': 'zulu'
# }
# Importing necessary modules required
import speech_recognition as spr
from gtts import gTTS
from deep_translator import GoogleTranslator
import os
# Creating Recogniser() class object
recog1 = spr.Recognizer()
# Creating microphone instance
mc = spr.Microphone()

Origin_Lang = input("enter from language")
Dest_Lang = input("enter destination language")
# Capture Voice
with mc as source:
print("Speak 'hello' to initiate the Translation !")
print("~~~~~~~~~~~~~~~~")
recog1.adjust_for_ambient_noise(source, duration=0.2)
audio = recog1.listen(source)
MyText = recog1.recognize_google(audio)
MyText = MyText.lower()
# Here initialising the recorder with
# hello, whatever after that hello it
# will recognise it.
if 'hello' in MyText:
# Translator method for translation
# short form of english in which
# you will speak
# from_lang = 'en'
# In which we want to convert, short
# form of hindi
# to_lang = 'hi'
with mc as source:
print("Speak sentence in Your Original Language...")
# Storing the speech into audio variable
audio = recog1.listen(source)
# Using recognize.google() method to
# convert audio into text
get_sentence = recog1.recognize_google(audio)
# Using try and except block to improve
# its efficiency.
try:
# Printing Speech which need to
# be translated.
print("Phase to be Translated :" + get_sentence)
# Using translate() method which requires
# three arguments, 1st the sentence which
# needs to be translated 2nd source language
# and 3rd to which we need to translate in
translated = GoogleTranslator(source=Origin_Lang,
target=Dest_Lang).translate(get_sentence)
# Storing the translated text in text
# variable
print(translated)
f = open("translated_2.txt", "w+")
f.write(translated)
f.close()
os.system("start translated_2.txt")
# Using Google-Text-to-Speech ie, gTTS() method
# to speak the translated text into the
# destination language which is stored in to_lang.
# Also, we have given 3rd argument as False because

# by default it speaks very slowly
if Dest_Lang == 'english':
language = 'en'
if Dest_Lang == 'hindi':
language = 'hi'
if Dest_Lang == 'telugu':
language = 'te'
if Dest_Lang == 'tamil':
language = 'ta'
if Dest_Lang == 'bengali':
language = 'bn'
if Dest_Lang == 'marathi':
language = 'mr'
if Dest_Lang == 'malayalam':
language = 'ml'
if Dest_Lang == 'kannada':
language = 'kn'
if Dest_Lang == 'german':
language = 'de'
if Dest_Lang == 'gujarati':
language = 'gu'
if Dest_Lang == 'chinese (traditional)':
language = 'zh-cn'
file = open("translated_2.txt", "r").read().replace("\n", "
")
speech = gTTS(text=str(file), lang=language, slow=False)
speech.save("voice.mp3")
os.system("start voice.mp3")
except spr.UnknownValueError:
print("Unable to Understand the Input")
except spr.RequestError as e:
print("Unable to provide Required Output".format(e))