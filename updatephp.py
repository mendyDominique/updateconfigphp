# -*-coding:Latin-1 -*-
import os.path


def updateConf(**configDict):
    response = configDict['response']
    #nom du fichier
    NomFichier = 'MonFichier.php'
    f = open(NomFichier, 'w')
    f.write("<?php header(\"content-type: text/xml\"); echo \"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\";?>" + "\n")
    if response is None:
        f.write("")
    else:
        f.write("<Response>" + "\n" + "\t")
        say = configDict['response']['say']
        if say is None:
            f.write("" + "\n")
        else:
            voice = configDict['response']['say']['voice']
            language = configDict['response']['say']['language']
            sentence = configDict['response']['say']['sentence']
            f.write("<Say voice=\"" + voice + "\" language=\"" + language + "\"> " + sentence + " </Say>" + "\n")
        Dial = configDict['response']['Dial']
        if Dial is None:
            f.write("")
        else:
            action = configDict['response']['Dial']['action']
            timeout = configDict['response']['Dial']['timeout']

            if timeout is None:
                f.write("\t" + "<Dial action= \"" + str(action) + "\" method=\"GET\" >" + "\n")
            elif action is None:
                f.write("\t" + "<Dial timeout=\"" + str(timeout) + "\" method=\"GET\" >" + "\n")
            elif action is None and timeout is None:
                f.write("\t" + "<Dial method=\"GET\" >" + "\n")
            else:
                f.write("\t" + "<Dial action= \"" + str(action) + "\" timeout=\"" + str(
                    timeout) + "\" method=\"GET\" >" + "\n")
            if configDict['response']['Dial']['Number'] is None:
                f.write("")
            else:
                for number in configDict['response']['Dial']['Number']:
                    f.write("\t" + "\t" + "<Number>" + str(number) + "</Number>" + "\n")
            if configDict['response']['Dial']['sip'] is None:
                f.write("")
            else:
                for sip in configDict['response']['Dial']['sip']:
                    f.write("\t" + "\t" + "<Sip>" + str(sip) + "</Sip>" + "\n")
            f.write("\t" + "</Dial>")
        f.write("\n" + "</Response>")
    f.close()

#pour faire les teste appel de fonction
updateConf(**configDict)
os.system("pause")
