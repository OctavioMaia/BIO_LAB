import os
from Bio import Entrez
from Bio import SeqIO

dic = dict()
dic[0] = (1694217,1695287)
dic[1] = (1755653,1817098)
dic[2] = (2255112,2255900)
dic[3] = (2478431,2479402)

for k in range(0,len(dic)):
    seq_s = dic[k][0]
    seq_e = dic[k][1]
    pre = "sequence"
    ext = ".gb"
    seq_name = pre+ext
    print("START: {} STOP: {}".format(seq_s,seq_e))

    seq_name=pre+str(k+1)+ext

    Entrez.email = "a71369@alunos.uminho.pt"
    handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="NC_002942.5", seq_start=seq_s, seq_stop=seq_e)
    seq_record = SeqIO.read(handle, "gb")
    SeqIO.write(seq_record, seq_name, "genbank")
    handle.close()

print("Finished")