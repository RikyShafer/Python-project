# חבילת Python התומכת במנועי ההמרה הטקסט לדיבור הנפוצים
import pyttsx3

# להבנת דיבור
import speech_recognition as sr

# לאחזור את התשובות
# לשאילתות חישוביות
import wolframalpha

# לאחזור ערכים מוויקיפדיה
import wikipedia



# פונקציה לחיפוש השאילתה
# שהוזנה או נאמרה
# על ידי המשתמש
def search(query):
    # נשתמש בניסיון עבור חיפוש עם wolframAlpha
    try:

        # יצירת מזהה האפליקציה מWolframAlpha
        app_id = "RLW4E5-4624VWK5J7"
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        print(answer)
        SpeakText("Your answer is " + answer)

    # אם אי אפשר לחפש את השאילתה באמצעות
    # WolframAlpha, אז נחפש בוויקיפדיה
    except:
        query = query.split(' ')
        query = " ".join(query[0:])

        SpeakText("I am searching for " + query)
        print(wikipedia.summary(query, sentences=3))
        SpeakText(wikipedia.summary(query, sentences=3))

# פונקציה להמרת טקסט לדיבור
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# קוד הנהג
# הזנת שאילתה מהמשתמש באמצעות
# הקלדה או באמצעות דיבור
query = input()
query = query.lower()

# אם השאילתה ריקה, המשתמש
# מתבקש לדבר משהו.
if query == '':
    print("print you word")
    r = sr.Recognizer()

    # משתמש במיקרופון המוגדר כברירת מחדל
    # כמקור להקלטת הדיבור
    with sr.Microphone() as source:
        print("Say Something ")

        # צמצום הרעש ברקע
        # והשקטה למשך 2 שניות
        r.adjust_for_ambient_noise(source, 2)

        # האזנה למקור
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio)
        search(speech)

    # טיפול בשגיאות אם הדיבור
    # לא הובן
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    # טיפול בשגיאות אם אי אפשר
    # לטפל בבקשות, קורה
    # בעיקר בגלל שגיאות רשת
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
# אחרת, נחפש את השאילתה
else:
    search(query)
