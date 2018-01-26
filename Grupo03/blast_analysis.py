from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Blast import NCBIWWW



for i in range(1,4):
	sequence = ""
	sequence += ("sequence")
	sequence += str(i)
	sequence += (".gb")
	seq_record = SeqIO.read(sequence, 'gb')
	proteins = []
	for feature in seq_record.features:
	    if feature.type == "CDS":
	        seq_protein = Seq(str(feature.qualifiers['translation']), IUPAC.extended_protein)
	        protein_record = SeqRecord(seq_protein)
	        proteins.append(protein_record)
	blast = ""
	blast += ("blast")
	blast +=str(i)
	blast +=(".xml")
	save_file = open(blast, 'w')
	for protein in proteins:
	    result_handle = NCBIWWW.qblast('blastp', 'swissprot', protein.format('gb'))
	    save_file.write(result_handle.read())
	    save_file.write('\n')
	save_file.close()
	result_handle.close()