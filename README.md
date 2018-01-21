# smarter-muelleimer
Public project by Leon Bartle and Sascha Haag for a school project.

Parts:

-Raspberry Pi Zero

-4 M6 Schrauben

-5V 5mW Laser (bevorzugt Rot)

-Kondensator 1uF 50V

-Photoresistor 

-Mülleimer ¯\_༼ ಥ ‿ ಥ ༽_/¯




3d Modell Ausdrucken und mit vier M6 Schrauben an Eimer befestigen. 

Pi Zero im Gehäuse befestigen.

Raspbian auf Pi Zero installieren (siehe hier:https://www.raspberrypi.org/downloads/raspbian/)

Beide Files (auth.py und Mülleimer2.py) laden.

In auth.py keys und tokens mit eigenen (hier: https://apps.twitter.com/ ) generierten keys ersetzen.

5V 5mw Laser in Mülleimer befestigen.

Photoresistor in Mülleimer befestigen.

Laser an 5V out und Ground löten.

Photoresistor Pin 1 (Ausrichtung egal) an 3.3V out löten. 

Photoresistor Pin 2 (Ausrichtung egal) an GPIO 2 löten (GPIO pins siehe hier:https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/)

1uF 50V Capacitor Positive an GPIO 2 löten.

1uF 50V Capacitor Negative an Ground löten.

Laser (evtl. über Spiegel) auf Photoresistor.

Fixierungsbeispiel bei "Beispiel1.png"

Variable "Grenzwert" in Code so umändern, dass Müll erkannt wird.


Viel Spaß beim Müll-rausholen ! :D




Coding by Leon Bartle

