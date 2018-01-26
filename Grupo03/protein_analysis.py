import requests
import re

from Bio import SwissProt
from Bio import SeqIO
from io import StringIO
from urllib.request import urlopen

#obtain protein data
def getDataFromProt(protid):
    url = "http://www.uniprot.org/uniprot/" + protid + ".txt"
    txt = urlopen(url).read()
    
    f = open((protid+".dat"), "w")
    f.write(txt.decode('utf-8'))
    f.close()
    handle = open((protid+".dat"))

    parsed = SwissProt.read(handle)
    status, locale, fmol, bio, name, id, function, length, ec = getInfoTxt(parsed)
    return name, id, locale, status, fmol, bio, function, length, ec

#get relevant data
def getInfoTxt(parsed):
    status = str(parsed.data_class)
    locale = ""
    aux = parsed.description
    d = { match.group(1): match.group(2)
            for match in re.finditer(r"([^=]+)=(\S+)\s*", aux)
        }
    ec = "-"
    for key, value in d.items():   # iter on both keys and values
        if key.endswith('EC'):
            ec = value
    aux = aux.split("=")
    aux = aux[1].split("{")
    name = aux[0]
    fmol = []
    function = ""
    bio = []
    id = str(parsed.entry_name)
    for cr in parsed.cross_references:
        if cr[0] == "GO":
            (type, ids, cl, pis) = cr
            if type == "GO":
                cls = str(cl).split(":")
                if cls[0] == 'F':
                    fmol.append(cls[1])
                if cls[0] == 'P':
                    bio.append(cls[1])
                if cls[0] == 'C':
                    locale = cls[1]
    for cr in parsed.comments:
        cr = str(cr).split(":")
        if cr[0] == "FUNCTION":
            function = cr[1].split("{")[0]
    if function == "":
        function = "Unavailable"
    length = str(parsed.sequence_length)
    return status, locale, fmol, bio, name, id, function, length, ec

#print data
def printProteinAnalysisAll():
    ids = []
    temp = "Unavailable"
    
    for i in range(1,4):
        sequence = ""
        sequence += ("sequence")
        sequence += str(i)
        sequence += (".gb")
        seq_record = SeqIO.read(sequence, 'genbank')
        for feat in seq_record.features:
            if feat.type == 'CDS':
                ID_prot = feat.qualifiers["protein_id"][0]
                ids.append(ID_prot)
        file = open("protein_analysis_all.txt", "w")
        for protid in ids:
            params = {"query": protid, "format": "fasta"}
            frecord = requests.get("http://www.uniprot.org/uniprot/", params)
            for record in SeqIO.parse(StringIO(frecord.text), "fasta"):
                aux = record.id
                print(aux)
                idfasta = str(aux).split("|")[1]
                print(idfasta)
            name, id, locale, status, fmol, bio, function,length,ec = getDataFromProt(idfasta)
            file.write("\nProtein Name : " + name)
            file.write("\nProtein ID : " + id)
            if locale == "":
                aux = temp
            else:
                aux = locale
            file.write("\nCellular Locale : " + aux)
            file.write("\nStatus : " + status)
            if str(bio) == "[]":
                aux = temp
            else:
                aux = str(bio)
            file.write("\nBiological Process : " + aux)
            if str(fmol) == "[]":
                aux = temp
            else:
                aux = str(fmol)
            file.write("\nMolecular Function : " + aux)
            file.write("\nFunction : " + function)
            file.write("\n")
        file.close()

dic = dict()
dic[0] = ('G8UTL3_LEGPN')
dic[1] = ('Q5ZV33')
dic[2] = ('Q5ZTZ3')
dic[3] = ('Q5ZTG6')

printProteinAnalysisAll()