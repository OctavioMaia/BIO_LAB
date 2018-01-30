# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 00:46:15 2018

@author: Diana
"""

from Bio.Blast import NCBIXML
from Bio import Entrez
from Bio import SeqIO



for b in range(1,2):
    file='blast'+str(b)+'.xml'
    resultado=open(file,'r')
    records=NCBIXML.parse(resultado)
    item=next(records)
    
    nome=[]
    query=[]
    for align in item.alignments:
        nome.append(align.hit_id)
        for hsp in align.hsps:
            query.append(hsp.query)
    
    acession=[]
    org=[]
    for elemento in nome[0:10]:
        nn=[str(x) for x in elemento.split('|')]
        acession.append(nn[-2])
        org.append(nn[-1])
    
    
    resultado=open('hit_blast'+str(b)+'.fasta', 'w')
    nome='sequence'+str(b)+'.gb'
    original=SeqIO.read(nome, 'genbank')
    organism=original.annotations["organism"]
    seq=''
    for feat in original.features:
        if feat.type=='CDS': seq=str(feat.qualifiers["translation"])
    resultado.write('>'+organism+'\n'+seq[2:(len(seq)-2)]+'\n')
      
    for num in acession:
        print(num)
        seq_name=num+'.gb'
        Entrez.email = "a71369@alunos.uminho.pt"
        handle = Entrez.efetch(db="protein", rettype="gb", retmode="text", id=num)
        seq_record = SeqIO.read(handle, "gb")
        SeqIO.write(seq_record, seq_name, "genbank")
        handle.close()
        
        file=SeqIO.read(seq_name, 'genbank')
        organismo=file.annotations["organism"]
        seq=str(file.seq)
        
        resultado.write('>'+organismo+'\n'+seq+'\n')
    
    resultado.close()
    print('Done!')
        
        
        
        
    


    
        

        
        




    