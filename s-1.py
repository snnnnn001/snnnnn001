# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time(0.0001)

nadya = LINE('Hongnapatxb@gmail.com','2HnapatB',appName="DESKTOPMAC\t5.21.3\tMAC\t10.15")

nadya.log("Auth Token : " + str(nadya.authToken))
channelToken = nadya.getChannelResult()
nadya.log("Channel Token : " + str(channelToken))



KAC = [nadya]

nadyaMID = nadya.profile.mid

Bots = [nadyaMID]
creator = [nadyaMID]
Owner = [nadyaMID]
admin = [nadyaMID]

nadyaProfile = nadya.getProfile()
lineSettings = nadya.getSettings()

oepoll = OEPoll(nadya)
responsename = nadya.getProfile().displayName

with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = nadyaProfile.displayName
myProfile["statusMessage"] = nadyaProfile.statusMessage
myProfile["pictureStatus"] = nadyaProfile.pictureStatus

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

#==============================================================================#

read = json.load(readOpen)
settings = json.load(settingsOpen)

def restartBot():

    backupData()
#    time.sleep(10)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    nadya.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        nadya.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = "╔"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "╔"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╔═"
    return helpTranslate
#==============================================================================#
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        


def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == 'help99':
                    helpMessage = helpmessage()
                    nadya.sendMessage(to, str(helpMessage))

                elif text.lower() == '600':
                        nadya.sendMessage(msg.to,"650")
                        time.sleep(0.0001)
                elif text.lower() == '600':
                        nadya.sendMessage(msg.to,"650")
                        time.sleep(0.0001)
                elif text.lower() == '700':
                        nadya.sendMessage(msg.to,"750")
                        time.sleep(0.0001)
                elif text.lower() == '800':
                        nadya.sendMessage(msg.to,"850")
                        time.sleep(0.0001)
                elif text.lower() == '900':
                        nadya.sendMessage(msg.to,"950")
                        time.sleep(0.0001)
                elif text.lower() == '1000':
                        nadya.sendMessage(msg.to,"1050")
                        time.sleep(0.0001)
                elif text.lower() == '1100':
                        nadya.sendMessage(msg.to,"1150")
                        time.sleep(0.0001)
                elif text.lower() == '1200':
                        nadya.sendMessage(msg.to,"1250")
                        time.sleep(0.0001)
                elif text.lower() == '1300':
                        nadya.sendMessage(msg.to,"1350")
                        time.sleep(0.0001)
                elif text.lower() == '1400':
                        nadya.sendMessage(msg.to,"1450")
                        time.sleep(0.0001)
                elif text.lower() == '1500':
                        nadya.sendMessage(msg.to,"1550")
                        time.sleep(0.0001)
                elif text.lower() == '1600':
                        nadya.sendMessage(msg.to,"1650")
                        time.sleep(0.0001)
                elif text.lower() == '1700':
                        nadya.sendMessage(msg.to,"1750")
                        time.sleep(0.0001)
                elif text.lower() == '1800':
                        nadya.sendMessage(msg.to,"1850")
                        time.sleep(0.0001)
                elif text.lower() == '1900':
                        nadya.sendMessage(msg.to,"1950")
                        time.sleep(0.0001)
                elif text.lower() == '2000':
                        nadya.sendMessage(msg.to,"2050")
                        time.sleep(0.0001)
                elif text.lower() == '2100':
                        nadya.sendMessage(msg.to,"2150")
                        time.sleep(0.0001)
                elif text.lower() == '2200':
                        nadya.sendMessage(msg.to,"2250")
                        time.sleep(0.0001)
                elif text.lower() == '2300':
                        nadya.sendMessage(msg.to,"2350")
                        time.sleep(0.0001)
                elif text.lower() == '2400':
                        nadya.sendMessage(msg.to,"2450")
                        time.sleep(0.0001)
                elif text.lower() == '2400':
                        nadya.sendMessage(msg.to,"2550")
                        time.sleep(0.0001)
                elif text.lower() == '2500':
                        nadya.sendMessage(msg.to,"2650")
                        time.sleep(0.0001)
                elif text.lower() == '2600':
                        nadya.sendMessage(msg.to,"2650")
                        time.sleep(0.0001)
                elif text.lower() == '2700':
                        nadya.sendMessage(msg.to,"2750")
                        time.sleep(0.0001)
                elif text.lower() == '2800':
                        nadya.sendMessage(msg.to,"2850")
                        time.sleep(0.0001)
                elif text.lower() == '2900':
                        nadya.sendMessage(msg.to,"2950")
                        time.sleep(0.0001)
                elif text.lower() == '3000':
                        nadya.sendMessage(msg.to,"3050")
                        time.sleep(0.0001)
                elif text.lower() == '3100':
                        nadya.sendMessage(msg.to,"3150")
                        time.sleep(0.0001)
                elif text.lower() == '3200':
                        nadya.sendMessage(msg.to,"3250")
                        time.sleep(0.0001)
                elif text.lower() == '3300':
                        nadya.sendMessage(msg.to,"3350")
                        time.sleep(0.0001)
                elif text.lower() == '3400':
                        nadya.sendMessage(msg.to,"3450")
                        time.sleep(0.0001)
                elif text.lower() == '3500':
                        nadya.sendMessage(msg.to,"3550")
                        time.sleep(0.0001)
                elif text.lower() == '3600':
                        nadya.sendMessage(msg.to,"3650")
                        time.sleep(0.0001)
                elif text.lower() == '3700':
                        nadya.sendMessage(msg.to,"3750")
                        time.sleep(0.0001)
                elif text.lower() == '3800':
                        nadya.sendMessage(msg.to,"3850")
                        time.sleep(0.0001)
                elif text.lower() == '3900':
                        nadya.sendMessage(msg.to,"3950")
                        time.sleep(0.0001)
                elif text.lower() == '4000':
                        nadya.sendMessage(msg.to,"4050")
                        time.sleep(0.0001)
                elif text.lower() == '4100':
                        nadya.sendMessage(msg.to,"4150")
                        time.sleep(0.0001)
                elif text.lower() == '4200':
                        nadya.sendMessage(msg.to,"4250")
                        time.sleep(0.0001)
                elif text.lower() == '4300':
                        nadya.sendMessage(msg.to,"4350")
                        time.sleep(0.0001)
                elif text.lower() == '4400':
                        nadya.sendMessage(msg.to,"4450")
                        time.sleep(0.0001)
                elif text.lower() == '4500':
                        nadya.sendMessage(msg.to,"4550")
                        time.sleep(0.0001)
                elif text.lower() == '4600':
                        nadya.sendMessage(msg.to,"4650")
                        time.sleep(0.0001)
                elif text.lower() == '4700':
                        nadya.sendMessage(msg.to,"4750")
                        time.sleep(0.0001)
                elif text.lower() == '4800':
                        nadya.sendMessage(msg.to,"4850")
                        time.sleep(0.0001)
                elif text.lower() == '4900':
                        nadya.sendMessage(msg.to,"4950")
                        time.sleep(0.0001)
                elif text.lower() == '5000':
                        nadya.sendMessage(msg.to,"5050")
                        time.sleep(0.0001)
                elif text.lower() == '5100':
                        nadya.sendMessage(msg.to,"5150")
                        time.sleep(0.0001)
                elif text.lower() == '5200':
                        nadya.sendMessage(msg.to,"5250")
                        time.sleep(0.0001)
                elif text.lower() == '5300':
                        nadya.sendMessage(msg.to,"5350")
                        time.sleep(0.0001)
                elif text.lower() == '5400':
                        nadya.sendMessage(msg.to,"5450")
                        time.sleep(0.0001)
                elif text.lower() == '5500':
                        nadya.sendMessage(msg.to,"5550")
                        time.sleep(0.0001)
                elif text.lower() == '5600':
                        nadya.sendMessage(msg.to,"5650")
                        time.sleep(0.0001)
                elif text.lower() == '5700':
                        nadya.sendMessage(msg.to,"5750")
                        time.sleep(0.0001)
                elif text.lower() == '5800':
                        nadya.sendMessage(msg.to,"5850")
                        time.sleep(0.0001)
                elif text.lower() == '5900':
                        nadya.sendMessage(msg.to,"5950")
                        time.sleep(0.0001)
                elif text.lower() == '6000':
                        nadya.sendMessage(msg.to,"6050")
                        time.sleep(0.0001)
                elif text.lower() == '6100':
                        nadya.sendMessage(msg.to,"6150")
                        time.sleep(0.0001)
                elif text.lower() == '6200':
                        nadya.sendMessage(msg.to,"6250")
                        time.sleep(0.0001)
                elif text.lower() == '6300':
                        nadya.sendMessage(msg.to,"6350")
                        time.sleep(0.0001)
                elif text.lower() == '6400':
                        nadya.sendMessage(msg.to,"6450")
                        time.sleep(0.0001)
                elif text.lower() == '6500':
                        nadya.sendMessage(msg.to,"6550")
                        time.sleep(0.0001)
                elif text.lower() == '6600':
                        nadya.sendMessage(msg.to,"6650")
                        time.sleep(0.0001)
                elif text.lower() == '6700':
                        nadya.sendMessage(msg.to,"6750")
                        time.sleep(0.0001)
                elif text.lower() == '6800':
                        nadya.sendMessage(msg.to,"6850")
                        time.sleep(0.0001)
                elif text.lower() == '6900':
                        nadya.sendMessage(msg.to,"6950")
                        time.sleep(0.0001)
                elif text.lower() == '7000':
                        nadya.sendMessage(msg.to,"7050")
                        time.sleep(0.0001)
                elif text.lower() == '7100':
                        nadya.sendMessage(msg.to,"7150")
                        time.sleep(0.0001)
                elif text.lower() == '7200':
                        nadya.sendMessage(msg.to,"7250")
                        time.sleep(0.0001)
                elif text.lower() == '7300':
                        nadya.sendMessage(msg.to,"7350")
                        time.sleep(0.0001)
                elif text.lower() == '7400':
                        nadya.sendMessage(msg.to,"7450")
                        time.sleep(0.0001)
                elif text.lower() == '7500':
                        nadya.sendMessage(msg.to,"7550")
                        time.sleep(0.0001)
                elif text.lower() == '7600':
                        nadya.sendMessage(msg.to,"7650")
                        time.sleep(0.0001)
                elif text.lower() == '7700':
                        nadya.sendMessage(msg.to,"7750")
                        time.sleep(0.0001)
                elif text.lower() == '7800':
                        nadya.sendMessage(msg.to,"7850")
                        time.sleep(0.0001)
                elif text.lower() == '7900':
                        nadya.sendMessage(msg.to,"7950")
                        time.sleep(0.0001)
                elif text.lower() == '8000':
                        nadya.sendMessage(msg.to,"8050")
                        time.sleep(0.0001)
                elif text.lower() == '8100':
                        nadya.sendMessage(msg.to,"8150")
                        time.sleep(0.0001)
                elif text.lower() == '8200':
                        nadya.sendMessage(msg.to,"8250")
                        time.sleep(0.0001)
                elif text.lower() == '8300':
                        nadya.sendMessage(msg.to,"8350")
                        time.sleep(0.0001)
                elif text.lower() == '8400':
                        nadya.sendMessage(msg.to,"8450")
                        time.sleep(0.0001)
                elif text.lower() == '8500':
                        nadya.sendMessage(msg.to,"8550")
                        time.sleep(0.0001)
                elif text.lower() == '8600':
                        nadya.sendMessage(msg.to,"8650")
                        time.sleep(0.0001)
                elif text.lower() == '8700':
                        nadya.sendMessage(msg.to,"8750")
                        time.sleep(0.0001)
                elif text.lower() == '8800':
                        nadya.sendMessage(msg.to,"8850")
                        time.sleep(0.0001)
                elif text.lower() == '8900':
                        nadya.sendMessage(msg.to,"8950")
                        time.sleep(0.0001)
                elif text.lower() == '9000':
                        nadya.sendMessage(msg.to,"9050")
                        time.sleep(0.0001)
                elif text.lower() == '9100':
                        nadya.sendMessage(msg.to,"9150")
                        time.sleep(0.0001)
                elif text.lower() == '9200':
                        nadya.sendMessage(msg.to,"9250")
                        time.sleep(0.0001)
                elif text.lower() == '9300':
                        nadya.sendMessage(msg.to,"9350")
                        time.sleep(0.0001)
                elif text.lower() == '9400':
                        nadya.sendMessage(msg.to,"9450")
                        time.sleep(0.0001)
                elif text.lower() == '9500':
                        nadya.sendMessage(msg.to,"9550")
                        time.sleep(0.0001)
                elif text.lower() == '9600':
                        nadya.sendMessage(msg.to,"9650")
                        time.sleep(0.0001)
                elif text.lower() == '9700':
                        nadya.sendMessage(msg.to,"9750")
                        time.sleep(0.0001)
                elif text.lower() == '9800':
                        nadya.sendMessage(msg.to,"9850")
                        time.sleep(0.0001)
                elif text.lower() == '9900':
                        nadya.sendMessage(msg.to,"9950")
                        time.sleep(0.0001)
                elif text.lower() == '10000':
                        nadya.sendMessage(msg.to,"10050")
                        time.sleep(0.0001)
                elif text.lower() == '10100':
                        nadya.sendMessage(msg.to,"10150")
                        time.sleep(0.0001)
                elif text.lower() == '10200':
                        nadya.sendMessage(msg.to,"10250")
                        time.sleep(0.0001)
                elif text.lower() == '10300':
                        nadya.sendMessage(msg.to,"10350")
                        time.sleep(0.0001)
                elif text.lower() == '10400':
                        nadya.sendMessage(msg.to,"10450")
                        time.sleep(0.0001)
                elif text.lower() == '10500':
                        nadya.sendMessage(msg.to,"10550")
                        time.sleep(0.0001)
                elif text.lower() == '10600':
                        nadya.sendMessage(msg.to,"10650")
                        time.sleep(0.0001)
                elif text.lower() == '10700':
                        nadya.sendMessage(msg.to,"10750")
                        time.sleep(0.0001)
                elif text.lower() == '10800':
                        nadya.sendMessage(msg.to,"10850")
                        time.sleep(0.0001)
                elif text.lower() == '10900':
                        nadya.sendMessage(msg.to,"10950")
                        time.sleep(0.0001)
                elif text.lower() == '20000':
                        nadya.sendMessage(msg.to,"20050")
                        time.sleep(0.0001)
                elif text.lower() == '20100':
                        nadya.sendMessage(msg.to,"20150")
                        time.sleep(0.0001)
                elif text.lower() == '20200':
                        nadya.sendMessage(msg.to,"20250")
                        time.sleep(0.0001)
                elif text.lower() == '20300':
                        nadya.sendMessage(msg.to,"20350")
                        time.sleep(0.0001)
                elif text.lower() == '20400':
                        nadya.sendMessage(msg.to,"20450")
                        time.sleep(0.0001)
                elif text.lower() == '20500':
                        nadya.sendMessage(msg.to,"20550")
                        time.sleep(0.0001)
                elif text.lower() == '20600':
                        nadya.sendMessage(msg.to,"20650")
                        time.sleep(0.0001)
                elif text.lower() == '20700':
                        nadya.sendMessage(msg.to,"20750")
                        time.sleep(0.0001)
                elif text.lower() == '20800':
                        nadya.sendMessage(msg.to,"20850")
                        time.sleep(0.0001)
                elif text.lower() == '20900':
                        nadya.sendMessage(msg.to,"20950")
                        time.sleep(0.0001)
                elif text.lower() == '21000':
                        nadya.sendMessage(msg.to,"21050")
                        time.sleep(0.0001)
                elif text.lower() == '22000':
                        nadya.sendMessage(msg.to,"22050")
                        time.sleep(0.0001)
                elif text.lower() == '23000':
                        nadya.sendMessage(msg.to,"23050")
                        time.sleep(0.0001)
                elif text.lower() == '24000':
                        nadya.sendMessage(msg.to,"24050")
                        time.sleep(0.0001)
                elif text.lower() == '25000':
                        nadya.sendMessage(msg.to,"25050")
                        time.sleep(0.0001)
                elif text.lower() == '26000':
                        nadya.sendMessage(msg.to,"26050")
                        time.sleep(0.0001)
                elif text.lower() == '27000':
                        nadya.sendMessage(msg.to,"27050")
                        time.sleep(0.0001)
                elif text.lower() == '28000':
                        nadya.sendMessage(msg.to,"28050")
                        time.sleep(0.0001)
                elif text.lower() == '29000':
                        nadya.sendMessage(msg.to,"29050")
                        time.sleep(0.0001)
                elif text.lower() == '30000':
                        nadya.sendMessage(msg.to,"30050")
                        time.sleep(0.0001)
                elif text.lower() == '30100':
                        nadya.sendMessage(msg.to,"30250")
                        time.sleep(0.0001)
                elif text.lower() == '30300':
                        nadya.sendMessage(msg.to,"30350")
                        time.sleep(0.0001)
                elif text.lower() == '30400':
                        nadya.sendMessage(msg.to,"30450")
                        time.sleep(0.0001)
                elif text.lower() == '30500':
                        nadya.sendMessage(msg.to,"30550")
                        time.sleep(0.0001)


    except Exception as error:
        logError(error)
#==============================================================================#


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)       
