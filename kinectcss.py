from scipy import ndimage
from time import *

name = raw_input("Enter full name of file (in same directory as this file): ")

res = raw_input("Enter Resolution (recommended >20):")
res=int(res)

raid = raw_input("Enter border-radius in percent (recommended 0-50): ")

sprd = raw_input("how spread out do you want the pixels? (recommended 1.00-2.00):")
sprd=float(sprd)

counter1 = 1
counter2 = 1
counter3 = 1;

rgb=ndimage.imread(name);

r=rgb[::]
rlist = r.tolist()

print "width: " + str(len(rlist))
print "height: " + str(len(rlist[1]))
print "total pixels in css: " + str(len(rlist)*len(rlist[1])/(res*res))
var2 = raw_input("are you sure you want to continue? (y/n)")

if(var2=='y'):
	print "starting..."
	filename = "photo-res "+str(res)+"-radius-"+str(raid)+'-spread-'+str(sprd)
	fhtml = open(filename+'.html', 'w')
	fcss = open(filename+'.css', 'w')

	while(counter1 < len(rlist)):
		while(counter2 < len(rlist[1])):
			fcss.write('#circle' + str(counter3) + '{position:absolute;left:' + str(counter2*sprd) +'px;top:' 
				+ str(counter1*sprd) + 'px;border-radius:' + raid +'%;width:' + str(res) + 'px;height:' + str(res) + 'px;background:rgb(' 
				+ str(rlist[counter1][counter2][0]) + ',' + str(rlist[counter1][counter2][1]) + ',' + str(rlist[counter1][counter2][2]) + ')}\n')
			fcss.write(' ')
			counter3 = counter3+1
			counter2 = counter2+1
		counter2=1
		counter1 = counter1+res

	fhtml.write('<!DOCTYPE html>\n')
	fhtml.write('<html lang="en">\n')
	fhtml.write('    <head>\n')

	fhtml.write('        <link rel="stylesheet" href="./'+filename+'.css" />\n')
	fhtml.write('        <title> image to css v0.03 </title>\n')
	fhtml.write('    </head>\n')
	fhtml.write('    <body>\n')

	counter1=1
	counter2=1

	while(counter1 < len(rlist)*len(rlist[1])):
		fhtml.write("        <div id=\"circle" + str(counter1) + "\"></div>\n")
		counter1 = counter1 + res

	fhtml.write('    </body>\n')
	fhtml.write('</html>\n')

	fcss.close()
	fhtml.close()
	print "done."
	sleep(2)
else:
	print "aborting."
	sleep(2)

