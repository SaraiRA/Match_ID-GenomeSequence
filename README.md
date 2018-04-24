# Match_ID-GenomeSequence

Recover "correct" genome sequence of the db

The script take a list od sequence id from a "incorrect" fasta file. And afeter qieth thatlist search for the "correct" sequence in a fasta file 

1. Take the correct ID from the incorrect fasta file
2. Make a dictionary of the correct list -the fasta file data base-. ID:Sequence
3. Read each string of the list and search in the correct data base sequence. Match a subset of the ID name, not match the complete name, all word in the list ID but not all words in the dictionary ID.  
