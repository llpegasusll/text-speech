from gtts import gTTS
import os

def lang():
    print("enter your language")
    print("--*1 English--")
    print("--*2 French--")
    print("--*3 Spanish--")
    print("--*4 Portuguese--")
    c=input()
    if int(c)==1:
        return 'en'
    elif int(c)==2:
        return 'fr'
    elif int(c)==3:
        return 'es'
    elif int(c)==4:
        return 'pt'
    else :
        return 'en'
        
    
def choice():
    print("****What you want to read?****")
    print("--1 for Personal text--")
    print("--2 for Open a text file--")
    print("--0 to exit--")
    b=input("Enter choice")
    return b

a=choice()

while(a!="none" or a!="exit"):
    if int(a)==1:
        txt=str(input("enter your statement to convert"))
        language=lang()
        output=gTTS(text=txt, lang=language, slow=False)
        output.save("your.mp3")
        os.system("start your.mp3")
        a=choice()
        continue
        

    

    elif int(a)==2:
        print("enter your statements")
        para=input()
        fh=open("mytxt.txt","w")
        fh.write(para)
        fh.close
        fh=open("mytxt.txt","r")
        test=fh.read().replace("\n", " ")
        language=lang()
        output=gTTS(text=test, lang=language, slow=False)
        output.save("your.mp3")
        os.system("start your.mp3")
        fh.close()
        a=choice()
        
        
        

    elif int(a)==0:
        test="Thank you"
        language='en'
        output=gTTS(text=test, lang=language, slow=False)
        output.save("your.mp3")
        os.system("start your.mp3")
        
        break
    else:
        choice()
        
    
