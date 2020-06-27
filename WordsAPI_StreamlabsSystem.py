# -*- coding: utf-8 -*-

#---------------------------------------
# Script Import Libraries
#---------------------------------------
import clr, codecs, json, os, re, sys

clr.AddReference("IronPython.Modules.dll")

#---------------------------------------
# Script Information
#---------------------------------------
ScriptName = "WordsAPI Parameter"
Website = "http://www.twitch.tv/EncryptedThoughts"
Description = "Adds a $wordsapi parameter that gets word info from WordApi."
Creator = "EncryptedThoughts"
Version = "1.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")
ReadMe = os.path.join(os.path.dirname(__file__), "README.md")

#---------------------------------------
# Classes
#---------------------------------------
class Settings(object):
    def __init__(self, settingsfile=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        except:
            self.EnableDebug = False
            self.EnableLengthLimit = True
            self.LengthLimit = 400
            self.WordsAPIKey = None

    def Reload(self, jsondata):
        self.__dict__ = json.loads(jsondata, encoding="utf-8")

    def Save(self, SettingsFile):
        try:
            with codecs.open(SettingsFile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, encoding="utf-8")
            with codecs.open(SettingsFile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8')))
        except:
            Parent.Log(ScriptName, "Failed to save settings to file.")
        return

#---------------------------------------
# Settings functions
#---------------------------------------

def ReloadSettings(jsondata):
    ScriptSettings.Reload(jsondata)

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    global ScriptSettings
    ScriptSettings = Settings(SettingsFile)
    ScriptSettings.Save(SettingsFile)
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
#---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):

    if parseString == None:
        return

    parseString = ParseWordsAPI(parseString) # $wordsapi(string of any letters from any language,format string)

    return parseString

#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return

#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return

#---------------------------
#   ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ParseWordsAPI(parseString):

    regex = r"\$wordsapi\(\s*\p{L}+\s*\,.*\)" # $wordsapi(string of any letters from any language,format string)

    item = re.search(regex, parseString)
    if item is None:
        return parseString

    if ScriptSettings.EnableDebug:
        Parent.Log(ScriptName, "WordsAPI request detected, guess we're about to learn once I parse this:  " + item.group())

    rawArguments = item.group().strip()[10:][:-1]
    args = rawArguments.split(",")
        
    word = args[0]
    formatStr = args[1]

    if ScriptSettings.EnableDebug:
        Parent.Log(ScriptName, "Beseeching WordAPI for information on: " + word)

    headers = {
        "x-rapidapi-host": "wordsapiv1.p.rapidapi.com",
	    "x-rapidapi-key": ScriptSettings.WordsAPIKey,
	    "useQueryString": True
    }

    raw = json.loads(Parent.GetRequest("https://wordsapiv1.p.rapidapi.com/words/" + word, headers))
    if ScriptSettings.EnableDebug:
        Parent.Log(ScriptName, str(raw))
    
    try:
        response = json.loads(raw["response"])

        pronunciation = ""
        if type(response["pronunciation"]) is str:
            pronunciation = response["pronunciation"]
        else:
            pronunciation = response["pronunciation"][response["pronunciation"].keys()[0]]

        definitions = []
        alldefinitions = ""
        count = 1
        for result in response["results"]:
            definition = result["partOfSpeech"] + " / " + result["definition"]
            alldefinitions += str(count) + ") " + definition + " "
            definitions.append(definition)
            count += 1

        formatStr = formatStr.replace("{word}", response["word"])
        formatStr = formatStr.replace("{pronunciation}", pronunciation)
        formatStr = formatStr.replace("{definitions}", alldefinitions)
    
        if ScriptSettings.EnableLengthLimit:
            formatStr = formatStr[:ScriptSettings.LengthLimit]
        parseString = parseString.replace(item.group(), formatStr)
    except:
        parseString = parseString.replace(item.group(), "Word not found.")

    return parseString



def openreadme():
    os.startfile(ReadMe)