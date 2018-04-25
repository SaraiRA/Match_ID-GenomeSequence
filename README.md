# Match_ID-GenomeSequence

Recover genome sequence of the db

The script take a list of sequence id from a fasta file. And after it search for the sequence in another fasta file 

1. Take the correct ID from one fasta file
2. Make a dictionary of the fasta file data base. ID:Sequence
3. Read each string of the list and search in the data base sequence. Match a subset of the ID name, not match the complete name, all word in the list ID but not all words in the dictionary ID.  
