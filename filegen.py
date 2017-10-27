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


newd=raw_input("\nWhat chance (1-100)% do you want to stay in the current directory?\n0 will create a new subdirectory every time.\n100 will never create a new subdirectory [85]: ")
if ( newd==""):
 newd=85
#if

topd=raw_input("\nWhat chance do you want to build deeper directory trees?\n0 will return to the top-level every time.\n100 will never, creating a linear subdirectory tree.\nWARNING: If this is lower than the chance to create a new directory,\nyou may end up with a shallow, wide directory structure [95]: ")
if ( topd==""):
 topd=95
#if
#------------------------------------
#This is the generation of files
#------------------------------------
while ( i < copies):
 #couter up
 i=i+1
 #size randomizer between two inputs
 sizie=random.randint(int(smallie), int(biggie))
 x=random.randint(1, 100)
 #This is the small loop that creates a new directory.
 if (x > newd):
  l=l+1
  #c is our new directory name, with a counter number and randomly selected name
  c=d+"/"+str(l)+"_"+dirs[random.randint(0, len(dirs)-1)]
  #creates our new directory
  os.system('mkdir '+c+' 2>>'+do+'/FileGen.log')
  #changes our current working directory variable to the newly created one.
  d=c
 #if
 #This is my command that creates the test files.
 #syntax for fallocate is: "fallocate -l 10M test1.dat"
 #these are all pulled from variabels and randomization and counters.
 os.system('fallocate -l '+str(sizie)+kmgt+' '+d+'/test'+str(i)+'.dat 2>>'+do+'/FileGen.log')
 #This is our chance to return to toplevel creation, so that it is not a linear subdirectory tree
 if (x > topd):
  d=do
 #if
#while
os.system('clear 2>>'+do+'/FileGen.log')
print "\nFinished. Created "+str(l)+" subdirectories containing "+str(copies)+" files between "+str(smallie)+kmgt+"B and "+str(biggie)+kmgt+"B."
os.system('echo \"'+time.ctime()+'::FileGen(Python) finished.\" >>'+do+'/FileGen.log')
os.system('echo \"'+time.ctime()+':: Created '+str(l)+' subdirectories containing '+str(copies)+' files between '+str(smallie)+kmgt+'B and '+str(biggie)+kmgt+'B\" >>'+do+'/FileGen.log')
