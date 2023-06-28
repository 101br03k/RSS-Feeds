import fileinput
import sys
import os
import shutil

def copytobackup():
    os.makedirs("temp")
    # open both files
    with open('rss-feeds.opml','r') as firstfile, open('temp/rss-feeds copy.opml','a') as secondfile:
      
    # read content from first file
        for line in firstfile:
               
             # append content to second file
             secondfile.write(line)

def remove1stline(): # removes 1st line
    for line_number, line in enumerate(fileinput.input('temp/rss-feeds copy.opml', inplace=1)):
        if line_number == 0:
            continue
        else:
            sys.stdout.write(line)

def removelastline(): # remove last line from file
    fd=open("temp/rss-feeds copy.opml","r")
    d=fd.read()
    fd.close()
    m=d.split("\n")
    s="\n".join(m[:-1])
    fd=open("temp/rss-feeds copy.opml","w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()

def replace1():
    #input file
    fin = open("temp/rss-feeds copy.opml", "rt")
    #output file to write the result to
    fout = open("temp/out.md", "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        fout.write(line.replace('<outline text="', ''))
    #close input and output files
    fin.close()
    fout.close()

    #input file
    fin = open("temp/out.md", "rt")
    #output file to write the result to
    fout = open("temp/out1.md", "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        fout.write(line.replace('" type="rss" xmlUrl="', ' '))
    #close input and output files
    fin.close()
    fout.close()
    
    #input file
    fin = open("temp/out1.md", "rt")
    #output file to write the result to
    fout = open("readme.md", "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        fout.write(line.replace('"/>', '<br />' ))
    #close input and output files
    fin.close()
    fout.close()
    shutil.rmtree("temp") 

copytobackup()

#remove headers
h = 8 #amount of times
counth = 0 #start point
while counth in range(h):
    remove1stline()
    counth += 1

#remove footers
f = 2 #amount of times
countf = 0 #start point
while countf in range(f):
    removelastline()
    countf += 1

replace1()