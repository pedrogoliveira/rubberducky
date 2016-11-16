#!/usr/bin/python
import sys, getopt, datetime, time, re

commandMap = {
    'ESCAPE':'KEY_LEFT_ESC',
    'ESC':'KEY_LEFT_ESC',
    'GUI':'KEY_LEFT_GUI',
    'WINDOWS':'KEY_LEFT_GUI',
    'COMMAND':'KEY_LEFT_GUI',
    'MENU':'229',
    'APP':'229',
    'END':'KEY_END',
    'SPACE':'\' \'',
    'TAB':'KEY_TAB',
    'PRINTSCREEN':'206',
    'ENTER':'KEY_RETURN',
    'RETURN':'KEY_RETURN',
    'UPARROW':'KEY_UP_ARROW',
    'DOWNARROW':'KEY_DOWN_ARROW',
    'LEFTARROW':'KEY_LEFT_ARROW',
    'RIGHTARROW':'KEY_RIGHT_ARROW',
    'UP':'KEY_UP_ARROW',
    'DOWN':'KEY_DOWN_ARROW',
    'LEFT':'KEY_LEFT_ARROW',
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

    'ALT':'KEY_LEFT_ALT',
    'SHIFT':'KEY_LEFT_SHIFT',
    'CTRL':'KEY_LEFT_CTRL',
    'CONTROL':'KEY_LEFT_CTRL'
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


def _parse(toParse):
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
                    parsedOut = '    Keyboard.print("' + textString + '");\n'
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
                for word in wordArray:
                    if wordArray[0] in comboMap:
                        commandKnown = True
                        releaseAll = True
                        parsedOut += '    Keyboard.press(' + comboMap[wordArray[0]] + ');\n'
                    elif wordArray[0] in commandMap:
                        commandKnown = True
                        releaseAll = True
                        parsedOut += '    Keyboard.press(' + commandMap[wordArray[0]] + ');\n'
                    elif wordArray[0] in keyMap:
                        commandKnown = True
                        releaseAll = True
                        parsedOut += '    Keyboard.press(\'' + keyMap[wordArray[0]] + '\');\n'
                    else:
                        commandKnown = False

            if not commandKnown:
                print 'Error: Unknown command or key \'%s\' at line: %d.' % wordArray[0],(i + 1)

            '''
            If we need to release keys, we do
            '''
            if (releaseAll):
                parsedOut = parsedOut + '    Keyboard.releaseAll();\n'
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

def toArduino(inputCode):
    if inputCode == '' or inputCode is None:
        print 'Error: No ducky script was entered !'
        return False
    parsedDucky = _parse(inputCode)
    if parsedDucky == '' or parsedDucky is None:
        return False

    strHeader = """
/******************************************************************************
* Generated with <3 by Dckuino.py, based on Dckuino,js an open source project !
*******************************************************************************/

#include "Keyboard.h"

void typeKey(uint8_t key)
{
    Keyboard.press(key);

    delay(50);

    Keyboard.release(key);
}

/* ------------- */
/* Init function */
/* ------------- */

void setup()
{
    // Begining the Keyboard stream
    Keyboard.begin();

    // Wait 500ms
    delay(500);

"""
    strFooter = """
    // Ending stream
    Keyboard.end();

    }\n\n'

/* Unused endless loop */
void loop() {}';
"""

    return strHeader + parsedDucky + strFooter

def main(argv):
    inputCode = ''
    parsedDucky = ''
    inputfile = 'payload.txt'
    outputfile = 'main.cpp'
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'Dckuino.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Dckuino.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is :', inputfile
    print 'Output file is :', outputfile
    with open(inputfile, 'r') as infile:
        fileData=infile.read()

    with open(outputfile, "w") as text_file:
        text_file.write(toArduino(fileData))
    """
    print toArduino(fileData)
    """

if __name__ == "__main__":
   main(sys.argv[1:])


def toArduino(inputCode):
    if not inputCode:
        sys.stderr.write('Error: No ducky script was entered !\n')
        sys.exit(2)
