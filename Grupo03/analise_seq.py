from Bio import Entrez
from Bio import SeqIO

#NCBI handle (NC_002942.5 = id #52840256)
Entrez.email = 'octaviojmaia@gmail.com'
handle = Entrez.efetch(db='nucleotide', rettype='gbwithparts', retmode='text',id='52840256')
seq_record = SeqIO.read(handle, 'gb')

#Write file
SeqIO.write(seq_record, 'sequence.gb', 'genbank') #Exporta ficheiro. Auxilio do Grupo 1.
handle.close()

#Debug print
record = SeqIO.read('sequence.gb', 'genbank')
print(record) 