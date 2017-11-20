#Author Matthew Saum
#Copyright 2017 SURFsara BV
#Apache License 2.0


#Python version of FileGen, created so that I can learn some python
import os
import random
import time

#This is the % chance to create and use a new directory.
#Between 1-100, if it is >= newd, it creates a new directory.
#For the same randomized int, if it is >= topd, we return to our top-level directory of file generation


#dirs is our randomized list of directory names.
dirs= ('Berlin', 'Amsterdam', 'Utrecht', 'Rome', 'Maastricht', 'Lisbon', 'NewYork', 'Frankfurt', 'Budapest', 'Marrakesh', 'Vlissigen', 'Koln', 'Munich', 'Venice', 'Malaga', 'Faro', 'Porto', 'London', 'Prague', 'Paris', 'Madrid', 'Dublin', 'Glasgow', 'LasVegas', 'Denver', 'Honolulu', 'LosAngeles', 'Chicago', 'WashingtonDC', 'Boston', 'Copenhagen', 'Brussels', 'Liege', 'Dusseldorf', 'MazarESharif')
i=0 #copy counter
l=0 #directory counter



os.system('clear')


#asks for the directory to begin working
d=raw_input("Please enter the directory to create FileGen test files [./]: ")
if (d==""):
 d="./FileGen"
#if
else:
 d=d+"/FileGen"
#else
do=d

#creating logs


print "\nClearing out any old FileGen directories already existing."
#deletes existing dir with matching naem as the toplevel "d"
os.system('rm -rf '+d)
#makes the new directory
os.system('mkdir '+d)
os.system('echo \"'+time.ctime()+'::FileGen(Python) started.\" >'+do+'/FileGen.log')

#asks for data size type
kmgt=raw_input("Please enter the size you want to measure by (K, M, G, T) for KB, MB, GB, TB respectively [M]: ")
if (kmgt==""):
 kmgt="M"
#if
#asks for minmum size
smallie=raw_input("Please enter the minimum size [1]: ")
if (smallie==""):
 smallie=1
#if

#asks for maximum size
biggie=raw_input("Please enter the maximum size [10]: ")
if (biggie==""):
 biggie=10
#if

#asks for how many copys to make
copies=raw_input("Please enter the number of files you would like to create [100]: ")
if (copies==""):
 copies=100
#if


newd=raw_input("\nWhat chance (1-100)% do you want to create a new directory?\n0 will never do this.\n100 will create a new directory for each file [25]: ")
if ( newd==""):
 newd=25
#if

topd=raw_input("\nWhat chance do you want to return to a higher directory?\n0 will never, creating a linear subdirectory tree.\n100 will return to the top-level every time.\nNOTE: This value is subtracted from the previous value to determine the chance to\nchange up a single directory [7]: ")
if ( topd==""):
 topd=7
#if
elsd=100-(int(newd)-int(topd))
topd=100-int(topd)
newd=100-int(newd)
os.system('echo \"'+time.ctime()+'::Destination::'+d+'\" >>'+do+'/FileGen.log')
os.system('echo \"'+time.ctime()+'::Variables Input\" >>'+do+'/FileGen.log')
os.system('echo \"'+time.ctime()+'::Size Scale::'+kmgt+'B\" >>'+do+'/FileGen.log')
os.system('echo \"'+time.ctime()+'::Min Size::'+str(smallie)+kmgt+'B\" >>'+do+'/FileGen.log')
os.system('echo \"'+time.ctime()+'::Max Size::'+str(biggie)+kmgt+'B\" >>'+do+'/FileGen.log')
os.system('echo \"'+time.ctime()+'::Total Copies::'+str(copies)+'\" >>'+do+'/FileGen.log')
os.system('echo \"'+time.ctime()+'::Directory Chance::'+str(newd)+'%\" >>'+do+'/FileGen.log')
os.system('echo \"'+time.ctime()+'::Top-Level Chance::'+str(topd)+'%\" >>'+do+'/FileGen.log')


#------------------------------------
#This is the generation of files
#------------------------------------
while ( i < int(copies)):
 #couter up
 i=i+1
 #size randomizer between two inputs
 sizie=random.randint(int(smallie), int(biggie))
 x=random.randint(1, 100)
 #This is the small loop that creates a new directory.
 if (x > int(newd)):
  #directory counter, prevents duplciate naming
  l=l+1

  #d is our new directory name, with a counter number and randomly selected name
  d=d+"/"+str(l)+"_"+dirs[random.randint(0, len(dirs)-1)]
  
  #This logs a new directory creation
  os.system('echo \"'+time.ctime()+'::Directory Created::'+d+'\" >> '+do+'/FileGen.log')
  
  #creates our new directory
  os.system('mkdir '+d+' 2>>'+do+'/FileGen.log')
 #if
 #This is my command that creates the test files.
 #syntax for fallocate is: "fallocate -l 10M test1.dat"
 #these are all pulled from variabels and randomization and counters.
 os.system('fallocate -l '+str(sizie)+kmgt+' '+d+'/test'+str(i)+'.dat 2>>'+do+'/FileGen.log')
 
 #This line will load a log entry for each file created.
 os.system('echo \"'+time.ctime()+'::File Created::'+str(sizie)+kmgt+'B::'+d+'/test'+str(i)+'.dat\" >> '+do+'/FileGen.log')
 #This line here, if uncommented, will give a scrolling feedback of each file creation.
 #os.system('echo \"'+time.ctime()+'::File Created::'+str(sizie)+kmgt+'B::'+d+'/test'+str(i)+'.dat\"')
 
 #This is our chance to return to toplevel creation, so that it is not a linear subdirectory tree
 if (x > int(topd)):
  #This logs the return to top-level
  os.system('echo \"'+time.ctime()+'::Top-Level Return::'+do+'.\" >> '+do+'/FileGen.log')
  #resets us to our original top-level for file creation.
  d=do
 elif ( (x >  int(elsd)) & (d != do)):
  y=str.split(d, '/')
  del y[len(y)-1]
  d='/'.join(y)
  os.system('echo \"'+time.ctime()+'::One-Level-Up Return::'+d+'.\" >> '+do+'/FileGen.log')
  
 #if
#while
os.system('clear 2>>'+do+'/FileGen.log')
print "\nFinished. Created "+str(l)+" subdirectories containing "+str(copies)+" files between "+str(smallie)+kmgt+"B and "+str(biggie)+kmgt+"B."
os.system('echo \"'+time.ctime()+'::FileGen(Python) finished.\" >>'+do+'/FileGen.log')
os.system('echo \"'+time.ctime()+'::Created '+str(l)+' subdirectories containing '+str(copies)+' files between '+str(smallie)+kmgt+'B and '+str(biggie)+kmgt+'B in '+do+'.\" >>'+do+'/FileGen.log')
