import os
import random
import ctypes
import getpass

g_User = getpass.getuser()
g_Path = "C:\\Users\\" + g_User + "\\Downloads\\"

PHOTOS_PATH = "C:\\Users\\" + g_User + "\\Desktop\\pictures\\"
IMAGE_STATS = {}

IMAGE_EXTENSIONS = {
    ".mp4" : "video",
    ".avi" : "video",
    ".flv" : "video",
    ".wmv" : "video",
    ".mkv" : "video",
    ".png" : "image",
    ".jpg" : "image",
    ".jpeg" : "image",
    ".bmp" : "image",
}

PROCESSED_IMAGES = {}
IMAGE_SCORES = {}
NUM_ANALYZED = 0

def FocusWindow():
    ctypes.windll.user32.SetFocus(ctypes.windll.kernel32.GetConsoleWindow())

def outputConsole(text):
    os.system(str(text))

def randomNumber(number1, number2):
    return random.randint(number1, number2)

def loadImages():
    num = 0
    for fileName in os.listdir(PHOTOS_PATH):
        IMAGE_STATS[fileName] = num
        PROCESSED_IMAGES[num] = {}
        IMAGE_SCORES[fileName] = 0
        num += 1

def getImageID(image):
    return IMAGE_STATS[image]

def getImageFromID(id):
    for i, v in IMAGE_STATS.items():
        if v == id:
            return i
    return False

def getImageExtension(image):
    extension = image[-(len(image) - image.rfind(".")):].lower()
    return extension

def getImageType(image):
    extension = getImageExtension(image)
    if extension in IMAGE_EXTENSIONS:
        return IMAGE_EXTENSIONS[extension]
    return False

def getMaxCombinationNumber():
    num = 0
    indexer = len(IMAGE_STATS)
    for x in range(indexer):
        num += indexer - (x + 1)
    return num

def openImage(image):
    execute("start " + PHOTOS_PATH + image)

def initCmd():
    execute("@echo off")
    execute("color a")
    execute("cd " + PHOTOS_PATH)
    execute("title Analizator " + str(NUM_ANALYZED) + "/" + str(getMaxCombinationNumber()))
    execute("cls")

def execute(command):
    return os.system(command)

def detectConflict(number1, number2):
    if number2 in PROCESSED_IMAGES[number1]:
        return True
    if number1 in PROCESSED_IMAGES[number2]:
        return True
    return False

def killTasks():
    execute("taskkill /f /im vlc.exe")
    execute("taskkill /f /im dllhost.exe")

def updateTitle():
    execute("title Analyzer " + str(NUM_ANALYZED) + "/" + str(getMaxCombinationNumber()))

def getImageScore(image):
    return IMAGE_SCORES[image]

def getImageFromScore(score):
    for image, numScore in IMAGE_SCORES.items():
        if numScore == score:
            return image
    return False

def findWinner():
    winner = ""
    maxScore = 0
    for imageName, imageID in IMAGE_STATS.items():
        score = getImageScore(imageName)
        if score >= maxScore:
            winner = imageName
            maxScore = score
    return winner

def process():
    global NUM_ANALYZED
    print("Welcome to the picture contest. You will be voting for the best media file.\n")
    while(NUM_ANALYZED != getMaxCombinationNumber()):
        haventFoundCombination = True
        while(haventFoundCombination):
            number1 = randomNumber(0, len(IMAGE_STATS) - 1)
            number2 = randomNumber(0, len(IMAGE_STATS) - 1)
            if (number1 != number2) and (not detectConflict(number1, number2)):
                haventFoundCombination = False
        image1 = getImageFromID(number1)
        image2 = getImageFromID(number2)
        openImage(image1)
        openImage(image2)
        FocusWindow()
        betterPhoto = int(input("\nVote:\n[1]: " + image1 + "\n[2]: " + image2 + "\n"))
        PROCESSED_IMAGES[number1][number2] = number2
        NUM_ANALYZED += 1
        haventFoundCombination = True
        killTasks()
        updateTitle()
        winner = 0
        
        if betterPhoto == 1:
            winner = image1
        else:
            winner = image2

        IMAGE_SCORES[winner] += 1
    #finaleWinner = findWinner()
    execute("cls")
    print("======================================== RESULTS ========================================")
    data1 = reversed(sorted(IMAGE_SCORES.values()))
    top = 1
    for score in data1:
        photo = getImageFromScore(score)
        print("#" + str(top) + " (" + str(score) + "): " + photo)
        top += 1
    xxx = input("")
loadImages()
initCmd()
process()