"""This script adds extra functionality to Orca
Some information retrieved by this script can be pasted from the clipboard
This script automatically generated by http://www.stormdragon.us/orca-customizations/
Feel free to modify and/or redistribute this script as you see fit."""
import orca.input_event # watches for input that Orca recognizes
import orca.keybindings # Handles binding keystrokes for Orca to use.
import orca.orca # Imports the main screen reader
import orca.speech # Handles Orca's speaking abilities
import orca.braille # Displays information in Braille format
from xml.dom import minidom
import commands
import gtk
import os
import pygtk
import time
import urllib
import urllib2

#variable section
#Postal code for weather information:
zipCode = "UKXX0018"
myKeyBindings = orca.keybindings.KeyBindings()

#places text in the clipboard
def setClipboardText(text):
    cb = gtk.Clipboard()
    cb.set_text(text)
    cb.store()

#getWeather function gets weather from Yahoo
def getWeather(zip_code, forecast = False):
    if zip_code != "0":
        WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
        WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'
        url = WEATHER_URL % zip_code
        dom = minidom.parse(urllib.urlopen(url))
        forecasts = []
        for node in dom.getElementsByTagNameNS(WEATHER_NS, 'forecast'):
            forecasts.append(node.getAttribute('text'))
            forecasts.append(node.getAttribute('high'))
            forecasts.append(node.getAttribute('low'))
        ycondition = dom.getElementsByTagNameNS(WEATHER_NS, 'condition')[0]
        weatherReport = "It is currently " + ycondition.getAttribute('temp') + " degrees and " + ycondition.getAttribute('text') + "."
        if forecast == True: weatherReport = "Today's forecast is " + str(forecasts[0]) + " with a high temperature of " + forecasts[1] + " and a low of " + forecasts[2] + " degrees."
        weatherReport = weatherReport.capitalize()
        weatherReport = weatherReport.replace("/", " and ")
    else:
        weatherReport = "No zip code set: Please edit .orca/orca-customizations.py"
    setClipboardText(weatherReport)
    return weatherReport

#define the battery status function
def sayBattery(script, inputEvent=None):
    message = commands.getoutput("acpi")
    if len(message) == 0:
        message = "Battery not found."
    orca.speech.speak(message)
    orca.braille.displayMessage(message)
    return True
#end battery status function

#define the readClipboard function
def readClipboard(script, inputEvent=None):
 #Library import section
    #Get the clipboard
    cb = gtk.clipboard_get()
    #assign the clipboard contents to a variable.
    cbText = cb.wait_for_text()
    if isinstance(cbText, str) != True:
        cbText = "No text in clipboard."
    #Speak and braille the info
    orca.speech.speak(cbText)
    orca.braille.displayMessage(cbText)
#end readClipboard function

#define the check for updates function
def checkForUpdates(script, inputEvent=None):
    oldVer = 4.3
    updateUrl = "http://www.stormdragon.us/orca-customizations/version.txt"
    try:
        fileHandle = urllib2.urlopen(updateUrl)
        newVer = fileHandle.read()
        fileHandle.close()
        if oldVer < float(newVer):
            message = "New version " + newVer + " is available. Opening stormdragon.us."
            orca.speech.speak(message)
            orca.braille.displayMessage(message)
            os.system("firefox http://www.stormdragon.us/orca-customizations/&")
        else:
            message = "Your orca-customizations.py file is up to date."
            orca.speech.speak(message)
            orca.braille.displayMessage(message)
    except IOError:
        message = "Can not access update information.  Please try again later."
        orca.speech.speak(message)
        orca.braille.displayMessage(message)
    return True
#end checkForUpdates function

#define the import updates function
def importUpdates(script, inputEvent=None):
    message = "New customizations file imported.  Please restart Orca so changes will take effect."
    if os.path.exists("Desktop/orca-customizations.py"):
        commands.getoutput("mv Desktop/orca-customizations.py .orca/orca-customizations.py")
    elif os.path.exists("Downloads/orca-customizations.py"):
        commands.getoutput("mv Downloads/orca-customizations.py .orca/orca-customizations.py")
    else:
        message = "customizations.py file not found.  Please make sure you saved it to your Desktop or Downloads folder."
    orca.speech.speak(message)
    orca.braille.displayMessage(message)
    return True

#Define the sayTime function
def sayTime(script, inputEvent=None):
    message = time.strftime("%I:%M%p", time.localtime())
    orca.speech.speak(message)
    orca.braille.displayMessage(message)
    setClipboardText(message)
    return True
#end sayTime function

#Define the sayDate function
def sayDate(script, inputEvent=None):
    message = time.strftime("%A, %B %d, %Y", time.localtime())
    orca.speech.speak(message)
    orca.braille.displayMessage(message)
    setClipboardText(message)
    return True
#end sayDate function

#Define the sayWeather function
def sayWeather(script, inputEvent=None):
    message = getWeather(zipCode)
    orca.speech.speak(message)
    orca.braille.displayMessage(message)
    return True
#end sayWeather function

#Define the sayForecast function
def sayForecast(script, inputEvent=None):
    message = getWeather(zipCode, True)
    orca.speech.speak(message)
    orca.braille.displayMessage(message)
    return True
#end sayForecast function

#Define the volume 0 value detect and correct function
def volumedetect():
#This function detect if the master volume is 0.
#If the master value is 0, increasing volume with 58%.
#Following command gets master volume actual value percentage
    mute = commands.getoutput('amixer get \'Master\',0|grep \'\[off\]\'')
    #If the master channel is muted unmute everything pulseaudio typically mutes
    if mute != "":
        commands.getoutput('amixer sset \'Master\',0 unmute')
        commands.getoutput('amixer sset \'Headphone\',0 unmute')
        commands.getoutput('amixer sset \'Speaker\',0 unmute')
    #If the volume value is 0%, increasing volume to 58%.
    volume = commands.getoutput('amixer get \'Master\',0|grep %| sed \'s/%.*//; s/.*\[//\'')
    if volume == "0":
        commands.getoutput('amixer set \'Master\',0 58%')
    volume = commands.getoutput('amixer get \'Headphone\',0|grep %| sed \'s/%.*//; s/.*\[//\'')
    if volume == "0":
        commands.getoutput('amixer set \'Headphone\',0 58%')
    volume = commands.getoutput('amixer get \'Speaker\',0|grep %| sed \'s/%.*//; s/.*\[//\'')
    if volume == "0":
        commands.getoutput('amixer set \'Speaker\',0 58%')
#End the volume 0 value detect and correct function

#Define the increase volume function
#Following function increasing master volume with 5 step, and spokening the new changed volume
def increasevolume(script, inputEvent=None):
    #Following command increasing volume with 5 step
    commands.getoutput("amixer sset \'Master\',0 5+")
    #Following command gets increased master volume percentage
    volume=commands.getoutput('amixer get \'Master\',0|grep %|cut -d "[" -f2')
    #Following command cut unneed ] character with spokened output.
    volume=volume.replace("]", "")
    #Final, spokening Orca the new increased volume value
    orca.speech.speak(volume)
#End increase volume function

#Define the decrease volume function
#Following function decreasing master volume with 5 step, and spokening the new changed volume
def decreasevolume(script, inputEvent=None):
    #Following command decreasing volume with 5 step
    commands.getoutput("amixer sset \'Master\',0 5-")
    #Following command gets decreased master volume percentage
    volume=commands.getoutput('amixer get \'Master\',0|grep %|cut -d "[" -f2')
    #Following command cut unneed ] character with spokened output.
    volume=volume.replace("]", "")
    #Final, spokening Orca the new decreased volume value
    orca.speech.speak(volume)
#End decrease volume function

#Define the toggle volume function
#Following function toggle master volume mute on/off
def togglevolumemute(script, inputEvent=None):
    #Following command gets master volume mute status
    mutestatus=commands.getoutput('amixer get \'Master\',0|grep "\[off\]"')
    #Following command toggle master volume mute on/off
    if mutestatus!='':
        commands.getoutput('amixer sset \'Master\',0 unmute')
        commands.getoutput('amixer sset \'Headphone\',0 unmute')
        commands.getoutput('amixer sset \'Speaker\',0 unmute')
        orca.speech.speak('Mute off.')
    else:
        commands.getoutput('amixer sset \'Master\',0 mute')
        commands.getoutput('amixer sset \'Headphone\',0 mute')
        commands.getoutput('amixer sset \'Speaker\',0 mute')
#End toggle volume function

#Set up sayBattery keys
sayBatteryHandler = orca.input_event.InputEventHandler(
    sayBattery,
    "Speaks and Brailles battery status.") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(
    "a",
    1 << orca.settings.MODIFIER_ORCA,
    1 << orca.settings.MODIFIER_ORCA,
    sayBatteryHandler)) # Sets Orca-a as the battery status key

#Set up readClipboard keys
readClipboardHandler = orca.input_event.InputEventHandler(
    readClipboard,
    "Speaks and Brailles clipboard contents.") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(
    "r",
    1 << orca.settings.MODIFIER_ORCA,
    1 << orca.settings.MODIFIER_ORCA,
    readClipboardHandler)) # Sets Orca-r as the read clipboard key

#Set up sayTime keys
sayTimeHandler = orca.input_event.InputEventHandler(
    sayTime,
    "Presents the time.") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(
    "t",
    1 << orca.settings.MODIFIER_ORCA,
    1 << orca.settings.MODIFIER_ORCA,
    sayTimeHandler)) # Sets the say time key

#add sayDate info
sayDateHandler = orca.input_event.InputEventHandler(
    sayDate,
    "Presents the date.") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(
    "d",
    1 << orca.settings.MODIFIER_ORCA,
    1 << orca.settings.MODIFIER_ORCA,
    sayDateHandler)) # Sets the say date key

#add sayWeather info
sayWeatherHandler = orca.input_event.InputEventHandler(
    sayWeather,
    "Get current temperature and conditions.") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(
    "w",
    1 << orca.settings.MODIFIER_ORCA,
    1 << orca.settings.MODIFIER_ORCA,
    sayWeatherHandler)) # Sets the say weather key

#add checkForUpdates info
checkForUpdatesHandler = orca.input_event.InputEventHandler(
    checkForUpdates,
    "Checks for new version of orca-customizations.py.") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(
    "c",
    1 << orca.settings.MODIFIER_ORCA,
    1 << orca.settings.MODIFIER_ORCA,
    checkForUpdatesHandler)) # Sets the check for upgrades key

#add importUpdates info
importUpdatesHandler = orca.input_event.InputEventHandler(
    importUpdates,
    "Imports new version of orca-customizations.py.") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(
    "c",
    1 << orca.settings.MODIFIER_ORCA,
    1 << orca.settings.MODIFIER_ORCA,
    importUpdatesHandler, 2)) # Sets the import upgrades key

#add sayForecast info
sayForecastHandler = orca.input_event.InputEventHandler(
    sayForecast,
    "Get extended weather information.") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(
    "w",
    1 << orca.settings.MODIFIER_ORCA,
    1 << orca.settings.MODIFIER_ORCA,
    sayForecastHandler, 2)) # Sets the say weather key

#Add increase volume info
increasevolumeHandler = orca.input_event.InputEventHandler(
    increasevolume,
    "Increasing master volume with 5 step, and spokening the new value") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(

    "Page_Up",
    orca.settings.ORCA_MODIFIER_MASK,
    orca.settings.ORCA_MODIFIER_MASK,
    increasevolumeHandler)) #Set Orca+PageUp key combination with increase volume function

#Add decrease volume info
decreasevolumeHandler = orca.input_event.InputEventHandler(
    decreasevolume,
    "Decreasing master volume with 5 step, and spokening the new value") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(

    "Page_Down",
    orca.settings.ORCA_MODIFIER_MASK,
    orca.settings.ORCA_MODIFIER_MASK,
    decreasevolumeHandler)) #Set Orca+PageDown key combination with decrease volume function

#Add toggle mute volume info
mutevolumeHandler = orca.input_event.InputEventHandler(
    togglevolumemute,
    "Toggle master volume mute on/off") # Shows the function of the key press in learn mode

myKeyBindings.add(orca.keybindings.KeyBinding(

    "End",
    orca.settings.ORCA_MODIFIER_MASK,
    orca.settings.ORCA_MODIFIER_MASK,
    mutevolumeHandler)) #Set Orca+End key combination with toggle volume mute function

orca.settings.keyBindingsMap["default"] = myKeyBindings
#end time, date, and weather code
#Following command execute the volume detect function with always script start.
#This function detects if master volume is 0, and increasing with 58% audible value.
volumedetect()

