 for num1 in range(1,6):
                i += 1
#                print(h)
                length = len(h)
                url1 = "http://www.glassdoor.com" + h[0:length - 4] + "_P" + str(num1) + ".htm"
                print(url1)
                content1 = urllib2.urlopen(url1).read()
                filename = str(i)
                file = open(filename,"w")
                file.write(content1)
                file.close()