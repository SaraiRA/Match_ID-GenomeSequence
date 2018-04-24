import sys
from Bio import SeqIO

incorrectSequence="Effectors.fasta"
correctSequence="DBGrasses.fasta"

# Recover the element of the ID from the fasta file 
listID = []
with open(incorrectSequence) as fastaFile:
    for line in fastaFile:
        #removes all whitespace at the start and end
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            line=line.split("_")
            line.pop(0)
            listID.append(line)
            
# Fasta sequence in a dictionary 
fastaSequence = open(correctSequence)
dictFasta = SeqIO.to_dict(SeqIO.parse(fastaSequence, "fasta"))

correctFastaFile = open("CorrectGenomicSequence.fasta", "w")
for i in range(len(listID)):
    for key,value in dictFasta.items():
        #make lower all the elements in the list 
        shortlistID_lower=[name_listID.lower() for name_listID in listID[i]]
        longName_lower=key.lower()
        if all(name in longName_lower for name in shortlistID_lower):
            #split to take only the first element 
            longName_lower=longName_lower.split()[0]
            # replace _ to - only for avoid next syntasis problems in future programmes, like the script in R
            longName_lower=longName_lower.replace(r'_', '-')

            #writing the new fasta file             
            correctFastaFile.write(">" + list_name[i] + "\n" +list_seq[i] + "\n" + dictFasta[key].seq)
correctFastaFile.close()
