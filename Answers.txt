# Bash_Answers

### Question 1
 ps |wc -l
 4 processes

### Question 2
invoke.sh script which has commands indicating time, date, uptime and users.
    date && time && uptime && who > updates.log

### Question 3
 "touch" command in creation of empty file in current directory.
 touch empty.txt

### Question 4
 mkdir -p ./Work/mini-project/RNA-seq/

### Question 5
 mv seqs.txt sequence.fasta
 Rename it by using the "mv" command.
 That is, "mv seqs.txt sequences.fasta". 
 Yes, it will overwrite the sequences.fasta file if it already existed.

### Question 6
  nano universal_greeting.txt
By using nano text editor. When you type nano in the terminal followed by the filename which is universal_greeting.txt,
the file you've created will be displayed from nano text editor where you can input the words "Hello world!",  save and exit.

### Question 7
    nano universal greeting.txt ; results in two files universal and greeting.txt
If the filename has a space between its words, it will use the space between the words and create two different files in the case of two words separated
by a space. Thus when using nano text editor two files will be created,as universal file and greeting.txt file.

### Question 8
  wget https://raw.githubusercontent.com/Fnyasimi/my-first-repo/main/directory1/test.fa
using wget (webget) command directly downloads the raw file.

### Question 9
  wc -l test.fa
One can count the number of lines present in the test.fa file using the wc command with the -l flag to specify line count.
  grep -c "^>" test.fa
For the number of sequences: grep -c "^>" test.fa ; using the grep command with the -c option to count lines that start with the "greater than" sign "^>" which indicate the start of a different sequence.

### Question 10
  grep -E "^>" test.fa > indentifiers.txt
Identifiers start with this > giving a brief metadata of its sequence.
Using the grep command with an E flag indicating an extended pattern, then followed by the specified pattern in quotes ^ this indicates the start of the line hence finding lines which start with this sign > in the test.fa file then redirecting(>) them to the identifiers.txt file.


### Question 11
  sed -i 's/A/a/g' test.fa

### Question 12
   grep -E "^>" test.fa

### Question 13
   species.sh script
  (grep ">" test.fa | sort > identities.txt && sed -i "s/PREDICTED: //g" identities.txt && cut -d ' ' -f 2,3 identities.txt)

### Question 14
bash species.sh test.fa | sort| uniq -c

### Question 15
for int in {0..30..1}
  do
    echo $int
   done

### Question 16
  for trial in {1..20}
  do
    touch "trial${trial}"
    mv trial${trial} trial${trial}.data
  done

### Question 17
 expr 1/0 on the commandline results to 1/0.
 This is because the syntax of the expr command isn't followed since spaces are missing between the arguments and the operator.

 ### Question 18
 echo output 1> stdout.log && echo error 2> stderr.log
The 1st command will redirect the standard output to a file known as stdout.log and the 2nd command will redirect the standard error to stderr.log

### Question 19

 ### Question 20
 You go back two directories back to icipe then Fun_stuff
  cd ../../Fun_stuff/
