# Tyson Spoelma
# Self Learning
# This program works with Python 2.7


import re, urllib
# http://www.broadinstitute.org/mpr/lung/
# http://textfiles.com/
textfile = file('depth_1.txt','wt')
print "Enter the URL you wish to crawl.."
print 'Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes'
myurl = input("@> ")
a = [".txt"]
#a = [".csv",".tar",".gz",".txt",".xls"]
b = ["http://","www"]
index = 0
parenturl = '/'.join(myurl.split("/")[:-2])
print parenturl
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
        print i
        if any(x in i for x in a):
            if "../" in i:
                #for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(parenturl+"/"+i[3:]).read(), re.I):
                #    print ee
                    downloadurl = parenturl+"/"+i[3:]
                    print downloadurl
                    response = urllib.urlopen(downloadurl)
                    csv = response.read()
                    csvstr = str(csv).strip("b'")
                    lines = csvstr.split("\\n")
                    f = open("webcrawler"+str(index)+".csv", "w")
                    index = index + 1
                    for line in lines:
                        f.write(line + "\n")
                    f.close()
                    #textfile.write(ee+'\n')
                    textfile.write(downloadurl+'\n')
                    #textfile.close()
            elif "/" in i[0:1]:
                #for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(parenturl+i[1:]).read(), re.I):
                #    print ee
                    downloadurl = parenturl+i[1:]
                    print downloadurl
                    response = urllib.urlopen(downloadurl)
                    csv = response.read()
                    csvstr = str(csv).strip("b'")
                    lines = csvstr.split("\\n")
                    f = open("webcrawler"+str(index)+".csv", "w")
                    index = index + 1
                    for line in lines:
                        f.write(line + "\n")
                    f.close()
                    #textfile.write(ee+'\n')
                    textfile.write(downloadurl+'\n')
                    #textfile.close()
            else:
                #for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                #    print ee
                try:
                        downloadurl = i
                        print downloadurl
                        response = urllib.urlopen(downloadurl)
                        csv = response.read()
                        csvstr = str(csv).strip("b'")
                        lines = csvstr.split("\\n")
                        f = open("webcrawler"+str(index)+".csv", "w")
                        index = index + 1
                        for line in lines:
                            f.write(line + "\n")
                        f.close()
                        #textfile.write(ee+'\n')
                        textfile.write(downloadurl+'\n')
                        #textfile.close()
                except:
                        downloadurl = myurl + i
                        print downloadurl
                        response = urllib.urlopen(downloadurl)
                        csv = response.read()
                        csvstr = str(csv).strip("b'")
                        lines = csvstr.split("\\n")
                        f = open("webcrawler"+str(index)+".csv", "w")
                        index = index + 1
                        for line in lines:
                            f.write(line + "\n")
                        f.close()
                        #textfile.write(ee+'\n')
                        textfile.write(downloadurl+'\n')
                        #textfile.close()
        else:
           if any(x in i for x in b):
              for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                 print ee
                 textfile.write(ee+'\n')
                 
textfile.close()
##
##from urllib import request
##
### Retrieve the webpage as a string
##response = request.urlopen("http://ichart.finance.yahoo.com/table.csv?s=AAPL&amp;d=1&amp;e=1&amp;f=2014&amp;g=d&amp;a=8&amp;b=7&amp;c=1984&amp;ignore=.csv")
##csv = response.read()
##
### Save the string to a file
##csvstr = str(csv).strip("b'")
##
##lines = csvstr.split("\\n")
##f = open("historical.csv", "w")
##for line in lines:
##   f.write(line + "\n")
##f.close()
