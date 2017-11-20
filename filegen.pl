#Author Matthew Saum
#Copyright 2017 SURFsara BV
#Apache License 2.0


#---------------------------------------------------
#INSTRUCTIONS-
#Create this perl script and a test file named after
#the $o variable in your local directory where it
#will execute.

#NOTE:
#Down below, you can uncomment / comment control
#to use "fallocate" or "dd", depending on your needs.
#---------------------------------------------------
#When run, it will auto-index upwards towardsn
#the prompted value, creating a copy of the test
#in the current, semi-randomly, decided working
#directory. This will also empty a previous run
#and attempt to re-fill. If you want multiple copies,
#be sure to mv the top-level to a new name and start.
#----------------------------------------------------

#top-level direcotry and a copy of it for preservation
my $d = "FileGen";
my $do = $d;
#counter and counted test file
 $i = 0; #copy counter
 $l = 0; #directory counter
my $o = "$do/test$i.dat"; #original file to copy from
#welcome to the random directory names
my $wd = `pwd`;
chomp $wd;
#just gives our directories a bit more than an incremental number for a name. Sure they may be duplicated, but it makes reading things easier.
#Nothing special here, just used names of people I knew originally. Now it is places I have been, to not advertise folks' names.
my @dirs = qw(Berlin Amsterdam Utrecht Rome Maastricht Lisbon NewYork Frankfurt Budapest Marrakesh Vlissigen Koln Munich Venice Malaga Faro Porto London Prague Paris Madrid Dublin Glasgow LasVegas Denver Honolulu LosAngeles Chicago WashingtonDC Boston Copenhagen Brussels Liege Dusseldorf MazarESharif);


#Input prompt for size and copies
print "What size do you want to measure in (K,M,G,T)? [M]:";
$kmgt = <STDIN>;
chomp $kmgt;
if ($kmgt eq ""){
  $kmgt = "M";
}
print "How small do you want the minmum size to be (in $kmgt)? [1]:";
$smallie = <STDIN>;
chomp $smallie;
if($smallie eq ""){
  $smallie = "1"; #if null, 1
}
print "How large do you want the maximum size to be (in $kmgt)? [10]:";
$biggie = <STDIN>;
chomp $biggie;
if($biggie eq ""){
  $biggie = "10"; #if null, 1
}
print "How many copies of the file do you want? [100]:";
$copies = <STDIN>;
chomp $copies;
if($copies eq ""){
  $copies = 100; #if null, 100
}

#Scrub previous directory, create a new empty one.
print `rm -r $do`;
print `mkdir $do`;


while ( $i < ($copies)){
  #counters
  $i = $i + 1;    #copies
  #our rando-gen
  my $f = int(rand(100)) + 1;
  my $sizie = ($smallie + int(rand(($biggie + 1) - $smallie))).$kmgt;
  #creates a new dir in current location
  if($f >= 85){
    $l = $l + 1;
    $r = int(rand(35));
    print `mkdir $d/$l\_$dirs[$r]`;
    $d = $d."/".$l."_".$dirs[$r];
#   print "$f% was >= 85, created and moved into $d\n";
  }
  #Uses fallocate to build the files.
  print `fallocate -l $sizie $d/test$i.dat 2>>$do/FileGen.log`;
  #Uses DD to make files. Limit is 2.1ish GB (the 2billion 32bit limit i think it was)
#  print `dd if=/dev/zero of=$d/test$i.dat bs=$sizie count=1 2>>$do/FileGen.log`;
  print `clear`;
  print "Created $l sub-directories containing $i files.\n";

  #move to top-level if >= 95
  if($f >= 95){
    print `cd $do`;
    $d = $do;
#   print "$f% was >= 95%: Moved to top-level again.\n";
  }
}
print ` echo "Finished. Created $wd/FileGen/ with $l sub-directories containing $i files between $smallie $kmgt\B and $biggie $kmgt\B.\n" >> $do/FileGen.log`;
#print `tar -chlf $d.tar -C $d/ .`;
#print `rm $d/*`;
print `clear`;
print "Finished. Created $wd/FileGen/ with $l sub-directories containing $i files between $smallie $kmgt\B and $biggie $kmgt\B.\n";

