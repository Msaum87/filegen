#Python version of FileGen, created so that I can learn some python
#Have built it better up than the perl one, now that I have had a few months of experience with it.
import os
import random

#This is the % chance to create and use a new directory.
#Between 1-100, if it is >= newd, it creates a new directory.
#For the same randomized int, if it is >= topd, we return to our top-level directory of file generation

#our new directory chance
#set to 101 to disable, set to 0 to force every item to get a new directory.
newd=85
#this is the chance to return to the top level of file creation. 
#set to 101 to disable, set to 0 to force it every time.
topd=95

#WARNINGS:
#If topd is ever lower than newd, you will end up with a lot of one-deep subdirectories across the toplevel specified. 
#The larger this difference between the two, the more it occurs.

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

print "\nClearing out any old FileGen directories already existing."
#deletes existing dir with matching naem as the toplevel "d"
os.system('rm -rf '+d)
#makes the new directory
os.system('mkdir '+d)



#asks for data size type
kmgt=raw_input("\nPlease enter the size you want to measure by (K, M, G, T) for KB, MB, GB, TB respectively [M]: ")
if (kmgt==""):
 kmgt="M"
#if
#asks for minmum size
smallie=raw_input("\nPlease enter the minimum size [1]: ")
if (smallie==""):
 smallie=1
#if

#asks for maximum size
biggie=raw_input("\nPlease enter the maximum size [10]: ")
if (biggie==""):
 biggie=10
#if

#asks for how many copys to make
copies=raw_input("\nPlease enter the number of files you would like to create [100]: ")
if (copies==""):
 copies=100
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
 if (x >= newd):
  l=l+1
  #c is our new directory name, with a counter number and randomly selected name
  c=d+"/"+str(l)+"_"+dirs[random.randint(0, len(dirs)-1)]
  #creates our new directory
  os.system('mkdir '+c)
  #changes our current working directory variable to the newly created one.
  d=c
 #if
 #This is my command that creates the test files.
 #syntax for fallocate is: "fallocate -l 10M test1.dat"
 #these are all pulled from variabels and randomization and counters.
 os.system('fallocate -l '+str(sizie)+kmgt+' '+d+'/test'+str(i)+'.dat')
 #This is our chance to return to toplevel creation, so that it is not a linear subdirectory tree
 if (x >= topd):
  d=do
 #if
#while
print "\nFinished. Created "+str(l)+" subdirectories containing "+str(copies)+" files between "+str(smallie)+kmgt+"B and "+str(biggie)+kmgt+"B."
