from Bio import SeqIO

out_cds = []
out_gene=[]
out_other=[]
CDS_proteinID =[]
CDS_geneID =[]
CDS_function= []

for k in range(0,4):
    filename = "sequence"+str(k+1)+".gb"
    record = SeqIO.read(filename, "genbank")
    for i in range(1,len(record.features)): 
        if(record.features[i].type == "CDS"): 
            out_cds.append(i)
        elif (record.features[i].type == "gene"):
            out_gene.append(i)
        else:
            out_other.append(i)
        i=+1
        #get CDS info
        for j in record.features:
            if j.type == "CDS":
                CDS_proteinID.append(j.qualifiers["protein_id"][0])
                CDS_geneID.append(j.qualifiers["db_xref"][0].strip("GeneID:"))

print(set(CDS_proteinID))

#table processing
f = open("ProteinTable.txt", 'r')
table=[]
for line in f.readlines():
    table.append(line.split('\t'))
f.close()

#validation
# flag = True
# for j in range (1,len(table)):
#     if table[j][5] != CDS_geneID[j-1] or table[j][8] != CDS_proteinID[j-1]:
#         flag=False

# print(flag)

print("=======Feature analysis=======")
print("Number of CDS: " + str(len(out_cds)))
print("CDS: " + str(out_cds)) 
print("\nNumber of genes: " + str(len(out_gene)))
print("GENES: " + str(out_gene))
print("\nNumber of other features: " + str(len(out_other)))
print("OTHER: " + str(out_other))
# print ("\n" + "Validation")
# if flag:
#     print ("Valid!")
# else:
#     print ("Invalid!")