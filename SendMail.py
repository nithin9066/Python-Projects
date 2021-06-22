import smtplib as sm
import speech_recognition as sr
import pyttsx3 as py
class send:
    flag =0
    email =""
    pas = ""
    def talk(this,text):
        engine = py.init()
        engine.setProperty('rate', 145)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()

    def mic(self, question):
        try:
            listener = sr.Recognizer()
            listener.pause_threshold = 0.7
            listener.energy_threshold = 400
            with sr.Microphone() as source:
                s.talk(question)
                print("listening.....")
                voice = listener.listen(source,timeout=5)

                answer = listener.recognize_google(voice)
                print(answer)
            return answer
        except:
            d = s.mic("Please Say Again")
            return d
    def send(self,ch):
        if ch != 1:
            s.subject = s.mic("Please say the subject")
            c = s.mic("You Said, " + s.subject + " is this correct?")
            if c == "no":
                s.send(0)
            if c == "yes":
                s.flag = 1
            else:
                s.send(0)
        if ch == 1 or s.flag == 1:
            msg = s.mic("Say The text Message")
            print(msg)
            mail = message = 'Subject: {}\n\n{}'.format(s.subject, msg)
            print(send.to1)
            conform = s.mic("You Said " + msg + " Do you want to send or do you want to change")
            if (conform == "send" or conform == "yes send" or conform == "yes"):
                print(send.to1)
                server = sm.SMTP('smtp.gmail.com', 587)
                server.starttls()
                username = s.email
                password = s.pas
                server.login(username, password)
                server.sendmail(username, send.to1, mail)
                s.talk("Mail Is Successfully Sent...")
                z = s.mic("do u want to another mail")
                if z == 'yes' or z == "s":
                    s.to(s.email, s.pas)
                elif z == "no":
                    s.talk("Exiting Have a Nice Day")
            elif (conform == "change" or conform == "chenge" or conform == "i want to change"):
                s.send(1)
            else:
                s.talk("could'nt Recognized")
                s.send(1)

    def conf(self):
        replay = s.mic("You Said " + send.to1 + "Is this correct?")
        print(replay)
        if (replay == "yes" or replay == "s"):
            s.send(0)
        elif (replay == "no"):
            s.to()
        else:
            s.talk( "plaese Say Again")
            s.conf()


    def to(this,username,password):
        s.email=username
        s.pas=password
        answer2 = s.mic("to whome you want to send")
        temp = answer2.replace(" ", "")
        tomail = temp.lower()
        send.to1 = tomail + "@gmail.com"
        print(send.to1)
        s.conf()



s = send()
s.to('Enter you mail address','Enter you mail password')
