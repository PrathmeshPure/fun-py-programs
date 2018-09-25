'''
by-Prathmesh Pure
A simple program to download multiple files on terminal.
Simply put your multiple download links separated by enter
in input.txt file and run the program.
I wrote this program to download youtube playlist, I had
download links generated from various sites that generats
download link for each video in playlist.
Problem on linux was that I do not had IDM like download manager
to download so I just copied link in file and wrote program
for my problem.
'''
import os


def main(filename):
    file = open(filename)
    contents = file.read()
    singlelinks = contents.splitlines()
    linklist = []
    total = len(singlelinks)

    for index in range(0, total):
        link = singlelinks[index]
        link = '"' + link + '"'
        linklist.append(['wget --content-disposition', link])
        commannd = ' '.join(linklist[index])
        print('"' * 60, '\n\t\t\t\t', total - index, " remaining\n", '"' * 60)
        os.system(commannd)


if __name__ == '__main__':
    filename = "input.txt"
    main(filename)
