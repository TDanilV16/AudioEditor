from email.mime import audio
import ffmpeg
import sys

from pandas import cut

base_dir = r'C:\Program Files\ffmpeg-master-latest-win64-gpl\bin'

sys.path.append(base_dir)

operations = list("iv", "dv", "cut", "splice")
greetingsText = "Hi Beavis!!!"
heplpText = "Help me..."

# example: cut music.mp3 1:20 1:30 makes a cut of music.mp3 from 1:20 to 1:30
# example: iv music.mp3 50 increases volume by 50%
# example: dv music.mp3 50 decreases volume by 50%
# example: splice music1.mp3 music2.mp3 makes a new file

def main():
    return None

def greetings():
    return greetingsText

def requestInstruction():
    instruction = input("Give an instruction \n>>> ")


def checkInstruction(instruction):
    operation = instruction.split()[0]
    audio = instruction.split()[1]
    if not checkOperation(operation):
        pass
    else:
        checkCasesAndDo(operation)
    return None

def checkOperation(operation):
    return operation == any(operations)

def checkFileForExistance(path, fileName):
    return None

def checkCasesAndDo(operation, instruction):
    if operation == any(["iv", "dv"]):
        changeVolume()
    elif operation == "splice":
        spliceAudio()
    elif operation == "cut":
        cutAudio()
    return None

def changeVolume(instruction):
    audio = instruction.split()[1]
    number = instruction.split()[2]
    return None

def spliceAudio(instruction):
    audio1 = instruction.split()[1]
    audio2 = instruction.split()[2]
    return None

def cutAudio(instruction):
    audio = instruction.split()[1]
    start = instruction.split()[2]
    end = instruction.split()[3]
    return None
# stream = ffmpeg.input('test.mp4')
# stream = stream.trim(start=5, duration=5).filter('setpts', 'PTS-STARTPTS')
# stream = stream.filter('fps', fps=5, round='up').filter('scale', w=128, h=128).filter('volume', volume=1.5)

# stream = ffmpeg.output(stream, 'out.mp4')

# ffmpeg.run(stream)  