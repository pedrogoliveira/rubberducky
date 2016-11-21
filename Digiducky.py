#!/usr/bin/python
import sys, getopt, datetime, time, re

kb_layout_dict = {
'PT':{'/':'\&','\&':'\^','-':'/','\(':'\*','\)':'\(','\=':'\)','\?':'\_','\+':'\[','\*':'\{','\\':'\`'},
'US':{'a':'a'},
'EN':{'a':'a'}
}

commandMap = {
    'ESCAPE':'KEY_LEFT_ESC',
    'ESC':'KEY_LEFT_ESC',
    'GUI':'MOD_GUI_LEFT',
    'WINDOWS':'MOD_GUI_LEFT',
    'COMMAND':'MOD_GUI_LEFT',
    'MENU':'229',
    'APP':'229',
    'END':'KEY_END',
    'SPACE':'\' \'',
    'TAB':'KEY_TAB',
    'PRINTSCREEN':'206',
    'ENTER':'KEY_ENTER',
    'RETURN':'KEY_ENTER',
    'UPARROW':'KEY_UP_ARROW',
    'DOWNARROW':'KEY_DOWN_ARROW',
    'LEFTARROW':'KEY_ARROW_LEFT',
    'RIGHTARROW':'KEY_RIGHT_ARROW',
    'UP':'KEY_UP_ARROW',
    'DOWN':'KEY_DOWN_ARROW',
    'LEFT':'KEY_ARROW_LEFT',
    'RIGHT':'KEY_RIGHT_ARROW',
    'CAPSLOCK':'KEY_CAPS_LOCK',
    'DELETE':'KEY_DELETE',
    'DEL':'KEY_DELETE',
    'F1':'KEY_F1',
    'F2':'KEY_F2',
    'F3':'KEY_F3',
    'F4':'KEY_F4',
    'F5':'KEY_F5',
    'F6':'KEY_F6',
    'F7':'KEY_F7',
    'F8':'KEY_F8',
    'F9':'KEY_F9',
    'F10':'KEY_F10',
    'F11':'KEY_F11',
    'F12':'KEY_F12',
    'PAGEUP':'KEY_PAGE_UP',
    'PAGEDOWN':'KEY_PAGE_DOWN'
    }
comboMap = {

    'ALT':'MOD_ALT_LEFT',
    'SHIFT':'MOD_SHIFT_LEFT',
    'CTRL':'MOD_CONTROL_LEFT',
    'CONTROL':'MOD_CONTROL_LEFT'
    }
keyMap = {
    'a':'a',
    'b':'b',
    'c':'c',
    'd':'d',
    'e':'e',
    'f':'f',
    'g':'g',
    'h':'h',
    'i':'i',
    'j':'j',
    'k':'k',
    'l':'l',
    'm':'m',
    'n':'n',
    'o':'o',
    'p':'p',
    'q':'q',
    'r':'r',
    's':'s',
    't':'t',
    'u':'u',
    'v':'v',
    'w':'w',
    'x':'x',
    'y':'y',
    'z':'z'
}

def translateString(s,kb_layout):
    d = kb_layout_dict[kb_layout]
    pattern = re.compile('|'.join(d.keys()))
    return pattern.sub(lambda x: d[x.group()], s)

def _parse(toParse,kb_layout):
    timerStart = int(round(time.time() * 1000))
    parsedScript = ''
    parsedOut = ''
    commandKnown = False
    releaseAll = False
    noNewline = False
    noDelay = False
    nextNoDelay = False
    '''
    Init default delay
    '''
    defaultDelay = 0
    '''
    Trim whitespaces and tabs
    '''
    toParse = toParse.strip(' \t')
    '''
    Cut the input in lines
    '''
    lineArray = toParse.split('\n')
    '''
    Loop every line
    '''
    i=0
    for line in lineArray:
        i=i+1
        if (line == '' or line == '\n'):
            print 'Info: Skipped line %d because was empty.' % i
        else:
            '''
            Reset line buffer
            '''
            parsedOut = ''
            '''
            Set to unknown command by default
            '''
            commandKnown = False
            '''
            releaseAll & noNewline & noDelay; *Line Modifiers*
            '''
            releaseAll = False
            noNewline = False
            noDelay = nextNoDelay
            nextNoDelay = False
            '''
            Cut every line in words & store the first word in a var
            '''
            wordArray = line.split(' ')
            wordOne = wordArray[0]
            '''
            Parse commands
            '''
            if wordOne == 'STRING':
                wordArray.pop(0)
                '''
                Make a string with escaped caracters for " and \
                '''
                textString = " ".join(wordArray)
                textString=textString.replace('\\','\\\\')
                textString.replace('"','\\"')
                if (textString != ''):
                    parsedOut = '    DigiKeyboard.print("' + translateString(textString, kb_layout) + '");\n'
                    commandKnown = True
                else:
                    print 'Error: at line: %d, STRING needs a text' % i
                    return None

            elif wordOne == 'DELAY':
                wordArray.pop(0)
                if(wordArray[0] is None or wordArray[0] == ''):
                    print 'Error: at line: %d, DELAY needs a time' % i
                    return None
                if wordArray[0] is not None:
                    parsedOut = '    delay(' + wordArray[0] + ');\n'
                    commandKnown = True
                    noDelay = True
                    nextNoDelay = True
                else:
                    return None

            elif wordOne == 'DEFAULT_DELAY':
                wordArray.pop(0)
                if(wordArray[0] is None or wordArray[0] == ''):
                    print 'Error: at line: %d, DEFAULT_DELAY needs a time' % i
                    return None
                if wordArray[0] is not None:
                    commandKnown = True
                    noNewline = True
                    noDelay = True
                else:
                    print 'Error: at line: %d, DEFAULT_DELAY only acceptes numbers' % i
                    return None


            elif wordOne == 'TYPE':
                wordArray.pop(0)
                if(wordArray[0] is None or wordArray[0] == ''):
                    print 'Error: at line: %d, DEFAULT_DELAY needs a key' % i
                    return None
                if wordArray[0] is not None:
                    commandKnown = True
                    parsedOut = "    typeKey(\'" + keyMap[wordArray[0]] + "\');\n"
                else:
                    print 'Error: Unknown letter \'' + wordArray[0] +'\' at line: %d' % i
                    return None

                lixo=1
            elif wordOne == 'REM':
                wordArray.pop(0)
                if len(wordArray) > 0 :
                    commandKnown = True
                    noDelay = True
                    parsedOut = '  // ' + " ".join(wordArray)
                    if (i == (len(lineArray) - 1)):
                        parsedOut = parsedOut + '\n'
                else:
                    print 'Error: at line: %d, REM needs a comment' % i
                    return None

            elif wordOne == 'REPEAT' or wordOne == 'REPLAY':
                wordArray.pop(0)
                if(wordArray[0] is None or wordArray[0] == ''):
                    print 'Error: at line: %d, REPEAT/REPLAY needs a loop count' % i
                    return None
                if lastLines is None:
                    print 'Error: at line: %d, nothing to repeat, this is the first line.' % i
                    return None
                if wordArray[0] is not None:
                    linesTmp = parsedScript.split('\n')
                    '''
                    TO DO
                    '''
                else:
                    print 'Error: at line: %d, REPEAT/REPLAY only acceptes numbers' % i
                    return None

            else:
                if (len(wordArray) == 1):
                    if wordArray[0] in comboMap:
                        commandKnown = True
                        parsedOut = '    typeKey(' + comboMap[wordArray[0]] + ');\n'
                    elif wordArray[0] in commandMap:
                        commandKnown = True
                        parsedOut = '    typeKey(' + commandMap[wordArray[0]] + ');\n'
                    else:
                        commandKnown = False
                    wordArray.pop(0)
                elif (len(wordArray) == 2) and wordArray[0] in comboMap:
                    parsedOut = '    DigiKeyboard.sendKeyStroke(' + commandMap[wordArray[1]] + ',' + comboMap[wordArray[0]] + ');\n'
                    wordArray.pop(0)
                    wordArray.pop(0)
                    commandKnown = True
                else:
                    for word in wordArray:
                        if wordArray[0] in comboMap:
                            commandKnown = True
                            releaseAll = True
                            parsedOut += '    DigiKeyboard.sendKeyPress(' + comboMap[wordArray[0]] + ');\n'
                        elif wordArray[0] in commandMap:
                            commandKnown = True
                            releaseAll = True
                            parsedOut += '    DigiKeyboard.sendKeyPress(' + commandMap[wordArray[0]] + ');\n'
                        elif wordArray[0] in keyMap:
                            commandKnown = True
                            releaseAll = True
                            parsedOut += '    DigiKeyboard.sendKeyPress(\'' + keyMap[wordArray[0]] + '\');\n'
                        else:
                            commandKnown = False

            if not commandKnown:
                print 'Error: Unknown command or key \'%s\' at line: %d.' % wordArray[0],(i + 1)

            '''
            If we need to release keys, we do
            '''
            if (releaseAll):
                parsedOut = parsedOut + '    DigiKeyboard.sendKeyPress(0);\n'
            '''
            If there is a default delay add it
            '''
            if (defaultDelay > 0 and not noDelay):
                parsedOut = '    delay(' + defaultDelay + ');\n\n' + parsedOut

            parsedScript = parsedScript + parsedOut

            if not noNewline:
                '''
                add a new line
                '''
                parsedScript = parsedScript + '\n'

    timerEnd = int(round(time.time() * 1000))
    timePassed = timerEnd - timerStart

    print 'Done parsed %d lines in %d ms' % (len(lineArray),timePassed)
    return parsedScript

def toArduino(inputCode,kb_layout):
    if inputCode == '' or inputCode is None:
        print 'Error: No ducky script was entered !'
        return False
    parsedDucky = _parse(inputCode,kb_layout)
    if parsedDucky == '' or parsedDucky is None:
        return False

    title = """
/******************************************************************************
* Generated with <3 by Dckuino.py, based on Dckuino,js an open source project !
*******************************************************************************

Translated to keyboard layout: """
    
    strHeader = """

*******************************************************************************/
#include "DigiKeyboard.h"

void typeKey(uint8_t key)
{
    DigiKeyboard.sendKeyPress(key);
    delay(50);
    DigiKeyboard.sendKeyPress(0);
}

/* ------------- */
/* Init function */
/* ------------- */

void setup()

{

    DigiKeyboard.update();

    delay(1000);

    DigiKeyboard.sendKeyStroke(0); // Clean any key state. Release all

    delay(100);

"""
    strFooter = """

    }
    
/* Unused endless loop */
void loop() {};
"""

    return title + kb_layout + strHeader + parsedDucky + strFooter

def main(argv):
    inputCode = ''
    parsedDucky = ''
    inputfile = 'payload.txt'
    outputfile = 'main.cpp'
    kb_layout='US'
    try:
        opts, args = getopt.getopt(argv,"hi:k:o:",["ifile=","keyboard=","ofile="])
    except getopt.GetoptError:
        print 'Digiducky.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Digiducky.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-k","--keyboard"):
            kb_layout = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is :', inputfile
    print 'Output file is :', outputfile
    print 'Keyboard layout is:', kb_layout
    with open(inputfile, 'r') as infile:
        fileData=infile.read()

    with open(outputfile, "w") as text_file:
        text_file.write(toArduino(fileData, kb_layout))
    """
    print toArduino(fileData)
    """

if __name__ == "__main__":
   main(sys.argv[1:])


def toArduino(inputCode,kb_layout):
    if not inputCode:
        sys.stderr.write('Error: No ducky script was entered !\n')
        sys.exit(2)
