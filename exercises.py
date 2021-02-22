## Codes to Python questions

```
trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'
```

```
A_count=trna.count('A')
C_count=trna.count('C')
G_count=trna.count('G')
T_count=trna.count('T')
print(A_count)
print(T_count)
print(G_count)
print(C_count)
GC_content = ((G_count+C_count)/len(trna))*100
print(GC_content)
len(trna)
AT_content = ((A_count+T_count)/len(trna))*100
print(AT_content)
```
The code above outputs the %GC ad %AT content.

Given the following amino acid sequence (MNKMDLVADVAEKTDLSKAKATEVIDAVFA), find the first, last and the 5th amino acids in the sequence.

```
aa_seq = 'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'
print(aa_seq[0], aa_seq[-1], aa_seq[4])
```

The above amino acid is a bacterial restriction enzyme that recognizes "TCCGGA". Find the first restriction site in the following sequence: AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA

```
restriction_enzyme = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
print(restriction_enzyme.find('TCCGGA'))
```
