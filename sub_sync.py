import pysrt
import sys
import re
import os
from datetime import datetime, timedelta
import datetime

# stdoutOrigin = sys.stdout
# sys.stdout = open("data/test.srt", "w")
# sub = pysrt.open("data/video-example.srt")
# i = 0
# for increase in sub:
#     start_i = sub[i].start + 3000
#     end_i = sub[i].end + 3000
#     text_i = sub[i].text
#     i += 1
#     print(f'{i} \n{start_i} --> {end_i} \n{text_i}')
#     print()


help_cmd = """This is a program which shifts a subtitle file forwards or backwards, depending on the
entry value of the user. Next please enter the directory of the file and the name of the .srt file 
you want to edit and the seconds you want to offset. Can be negative or positive value. 
You can also add a name of a new output file (optional).

Format:
1. 'directory of file(example: D:/Movies/)' --> 'input_file.srt' --> 'seconds_shift' 
2. 'directory of file(example: D:/Movies/)' --> 'input_file.srt' --> 'seconds_shift' --> '--о' -->
--> 'output_file.srt'(optional)
"""
greets = """Greetings!
This is a simple program which shifts the subtitles of a file forwards or backwards by the 
amount of secs specified. For additional information type '--help' in the console. 
"""
# print()
# help_command = input("Press 'Enter' or type: '--help' for additional information:")
# print()
# if help_command == '--help':
#     print(help_cmd)
# print()
# file_input = input("Enter the name of the file to be edited:")
# print()
# file_input_path = "D:/programming/python/subsprob/data/" + file_input
# shift_sub = int(input('Please enter the seconds to be shifted. Accepts negative values:'))
# print()
# file_output = input('Enter the name of the new .srt file to be created:')
# file_output_path = "D:/programming/python/subsprob/data/" + file_output

# print(sys.argv[6])
# input_file = 'video-example.srt'
# output_file = 'test.srt'
# forward_shift = '3.0'
# backward_shift = '-3.0'
try:
    sys.argv[0].index('.py')
    if len(sys.argv) == 1:
        print(greets)
        sys.exit()
except ValueError:
    print("Wrong path. To read the instructions, type --help.")

if len(sys.argv) > 1 and '--help' in sys.argv[1]:
    print(help_cmd)
    sys.exit()

# if len(sys.argv) > 1 and input_file not in sys.argv[1] and '--help' not in sys.argv[1]:
#     print("""1. You have not chosen an existing .srt file to edit! To read the instructions,
# type --help, and start the program again.""")
#     sys.exit()
# try:
#     int(sys.argv[1]) is False
# except ValueError:
#     print("Wrong input format. Please type --help for more info.")
#     sys.exit()
# if len(sys.argv) == 2:
#     print("Wrong input format. Please type --help for more info.")
#     sys.exit()
try:
    sys.argv[1].index(':')
except ValueError:
    print("Wrong path. To read the instructions, type --help.")
    sys.exit()
try:
    sys.argv[1].index(':')
    sys.argv[2].index('.srt')
except ValueError:
    print("Wrong path. To read the instructions, type --help.")
    sys.exit()
try:
    sys.argv[2].index('.srt')
except ValueError:
    print("Wrong file format. Should end with .srt")
    sys.exit()
try:
    int(float(sys.argv[3]))
except ValueError:
    print("Wrong input format. Please type --help for more info.")
    sys.exit()

if len(sys.argv) > 1:
    input_file = sys.argv[2]
# if len(sys.argv) > 1 and forward_shift not in sys.argv and backward_shift \
# not in sys.argv and input_file in sys.argv[1]:
#     print("""2. You have not chosen a time offset! To read the instructions,
# type --help, and start the program again.""")
#     sys.exit()
if len(sys.argv) > 3:
    forward_shift = sys.argv[3]
if len(sys.argv) > 3 and int(float(sys.argv[3])) < 0:
    backward_shift = sys.argv[3]
# if len(sys.argv) > 1 and output_file in sys.argv:
#     if len(sys.argv) > 1 and output_file in sys.argv[3] and '--o' not in sys.argv and \
#     input_file in sys.argv[1] and sys.argv[2]:
#         print("""4. Add a prefix '--o' before the name of your output file!""")
#         sys.exit()

# if '--o' in sys.argv:
#     if len(sys.argv) > 1 and '--o' in sys.argv[3] and output_file not in sys.argv:
#         print("""4. You have not chosen a name for your output file! To read the instructions,
#     type --help, and start the program again.""")
#         sys.exit()

if len(sys.argv) == 6:
    if '--o' in sys.argv[4]:
        file_output_path = sys.argv[1] + sys.argv[5]
        print("Успешно създадохте файла.")
        stdoutOrigin = sys.stdout
        sys.stdout = open(file_output_path, "w")
    else:
        print("Wrong input format. Please use the --help command for more info.")
        sys.exit()
if len(sys.argv) == 5:
    print("Wrong input format. Please type --help for more info.")
    sys.exit()

if len(sys.argv) == 4:
    file_output_path = sys.argv[1] + sys.argv[2]
    print("Успешно редактирахте файла.")
    stdoutOrigin = sys.stdout
    sys.stdout = open(file_output_path, "r+")

pattern = r'(\d{2}:\d{2}:\d{2},d{3}$)|(\d{2}:\d{2}:\d{2})'
if len(sys.argv) > 2:
    file_input_path = sys.argv[1] + sys.argv[2]
    with open(file_input_path, 'r', encoding='utf-8') as f:
        text = f.readlines()
    for i in range(len(text)):
        if re.match(pattern, text[i]):
            s = text[i]

            numb = s[6] + s[7]
            numb2 = s[23] + s[24]
            numb3 = s[3] + s[4]
            numb4 = s[20] + s[21]
            numb5 = s[0] + s[1]
            numb6 = s[17] + s[18]
            millisecs = s[9] + s[10] + s[11]
            millisecs2 = s[26] + s[27] + s[28]
            mins = s[3] + s[4]
            mins2 = s[20] + s[21]
            hours = s[0] + s[1]
            hours2 = s[17] + s[18]
            kil = '000'
            if int(float(sys.argv[3])) < 0:
                shift_sub = int(float(sys.argv[3]))
                if int(numb) < abs(int(float(shift_sub))):
                    shift = '0'
                elif int(numb) - int(float(shift_sub)) < 0 and int(numb) > 3:
                    shift = '0'
                    if int(numb3) > 0:
                        shift = str(60 - (shift_sub - int(numb)))
                        mins = int(mins) - 1
                        if int(numb5) > 0 and int(mins) == 0:
                            mins = '59'
                            hours = int(hours) - 1

                else:
                    shift = int(numb) + shift_sub
                if int(numb2) < abs(int(float(shift_sub))):
                    shift2 = '0'
                elif int(numb2) - shift_sub < 0 and int(numb2) > 3:
                    shift2 = '00'
                    if int(numb4) > 0:
                        shift2 = str(60 - (shift_sub - int(numb2)))
                        mins2 = int(mins2) - 1
                        if int(numb6) > 0 and int(mins2) == 0:
                            mins2 = '59'
                            hours2 = int(hours2) - 1

                else:
                    shift2 = int(numb2) + shift_sub

                if len(str(mins)) < 2:
                    mins = '0' + str(mins)
                if len(str(mins2)) < 2:
                    mins2 = '0' + str(mins2)
                if len(str(hours)) < 2:
                    hours = '0' + str(hours)
                if len(str(hours2)) < 2:
                    hours2 = '0' + str(hours2)
                s = str(hours) + s[2] + str(mins) + s[5] + str(shift) + s[7 + 1:17] \
                    + str(hours2) + s[19] + str(mins2) + s[22] + str(shift2) + s[24 + 1:]

                if int(shift) < 10:
                    s = s[:5] + ':0' + s[(5+1):]
                if int(numb) == 0 or int(numb) + int(millisecs) / 1000 < abs(int(shift_sub)):
                    s = s[:9] + str(kil) + s[12:]
                if int(shift2) < 10:
                    s = s[:22] + ':0' + s[(22 + 1):]
                if int(numb2) == 0 or int(numb2) + int(millisecs2) / 1000 < abs(int(shift_sub)):
                    s = s[:26] + str(kil) + s[29:]
                print(s.strip())
            elif int(float(sys.argv[3])) > 0:
                shift_sub = int(float(sys.argv[3]))

                if int(float(numb)) + shift_sub >= 60:
                    shift = '0' + str(shift_sub + int(float(numb)) - 60)
                    mins = '0' + str(int(mins) + 1)
                    if int(mins) == 59:
                        mins = '00'
                        hours = int(hours) + 1
                    s = s[:6] + '0' + s[7:]
                else:
                    shift = str(int(float(numb)) + shift_sub)

                if int(float(numb2)) + shift_sub >= 60:
                    shift2 = '0' + str(shift_sub + int(float(numb2)) - 60)
                    mins2 = '0' + str(int(mins2) + 1)
                    if int(mins2) == 59:
                        mins2 = '00'
                        hours2 = int(hours2) + 1
                else:
                    shift2 = str(int(float(numb2)) + shift_sub)

                if int(float(numb2)) >= 60:
                    shift2 = int(shift) - 60
                s = str(hours) + s[2] + str(mins) + s[5] + str(shift) + s[7 + 1:17] \
                    + str(hours2) + s[19] + str(mins2) + s[22] + str(shift2) + s[24 + 1:]

                if len(shift) < 2:
                    s = s[:5] + ':0' + s[(5 + 1):]

                # if int(numb) + int(millisecs) / 1000 < int(shift_sub):
                #     s = s[:9] + str(kil) + s[12:]
                if len(shift2) < 2:
                    s = s[:22] + ':0' + s[(22 + 1):]
                # if int(numb2) + int(millisecs2) / 1000 < int(shift_sub):
                #     s = s[:26] + str(kil) + s[29:]
                print(s.strip())

        if not re.match(pattern, text[i]):
            s2 = text[i]
            print(s2.strip())




