# Nur GPIO 0.3.1a oder neuere, sonst funktioniert nicht
 
import RPi.GPIO as GPIO, time, os
from twython import Twython
from auth import(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        
)
twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret)

 

INSWURF = 0 
INSVOLL = 0
ISTVOLL = 0
JETZTWURF = 0
SENS = 0


#GPIO Modus setzten

GPIO.setmode(GPIO.BCM)
 

#Funktion zum messen der Rückzeit vom Kondensator

def Zeitmessung (PinzumMessen):
        reading = 0
        GPIO.setup(PinzumMessen, GPIO.OUT)
        GPIO.output(PinzumMessen, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(PinzumMessen, GPIO.IN)
        
        while (GPIO.input(PinzumMessen) == GPIO.LOW):
                reading += 1
        return reading
         


#Funktion zum Festlegen ob Voll oder nicht, Pin sollte immer 2 sein

def sensor():
        var = Zeitmessung(2)
        grenzwert = 45
#45 durch Kalibrierwert ersetzen
        if var < grenzwert:
                return 0
        else:
                return 1

         




#===================Hauptcode zur Berrechung===========================
    

#Mülleinwurfzähler 
while (1==1):
        STAT = sensor()
        if(STAT == 1):
                ISTVOLL = 1
        if (STAT == 0):
                ISTVOLL = 0
        if (STAT == 1 and SENS == 0):
                SENS = 1
        
        if (STAT == 1 and SENS >= 1 and SENS < 20):
                SENS = SENS+1
        else:
                
                INSVOLL = INSVOLL + 1
                 SENS = 0
                ANZAHL = str(JETZTWURF)
                #TwitterNachricht
                twitter.update_status(status="Hallo ich bin voll und zwar mit " + ANZAHL + " Einwürfen")
                JETZTWURF = 0
        #Müllvollzähler
        if (STAT == 0 and SENS <=20):
                
                            
                        SENS = 0
                        JETZTWURF = JETZTWURF + 1
                
        
                
                
        

        #Endnachricht (wird bei jedem Zyklus geupdated)
        print (ISTVOLL, "DER Mülleimer war schon ", INSVOLL, " mal voll ", " Schon ", JETZTWURF, " Würfe ", SENS)
         
#======Program by Leon Bartle=========
