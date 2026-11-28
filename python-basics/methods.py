name = "Reihaneh mohammadi"
print(name.title())
print(name.upper())
name_upper="REIHANEH MOHAMMADI"
print(upper_name.lower())
text_1="I am a coder"
text_2=text_1.replace('coder' , 'pythonist'))
print(text_1,text_2)
#or
text_1 +'\n'+ text_2
--------------------------
#DNA-->mRNA
dna_seq='CGTTT'
mRNA_seq=dna_seq.replace('T','U')
-------------------------
#%GC
dna_seq='AACTGGGTACT'
C=dna_seq.count('C')
G=dna_seq.count('G')
A=dna_seq.count('A')
T=dna_seq.count('T')
GC_content=(G+C)/len(dna_seq)*100
print(GC_content)
---------------------------
my-protein='MKSLFSP'
Ser_count=my_protein.count('S')/len(my_protein)*100
print(Ser_count)
