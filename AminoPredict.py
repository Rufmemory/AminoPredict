#Readme included below.
def translate_seq():
    known_nuc = []
    input_seq = list(input())
    seq_len = len(input_seq)
    dna_typed = []
    rna_typed = []
    dna_match = []
    reader = 0
    while reader < seq_len:
        for chars in input_seq:
            if input_seq[reader] == 'a':
                dna_typed.append('a')
                dna_match.append('t')
                rna_typed.append('a')
                reader += 1
                pass
            elif input_seq[reader] == 't':
                dna_typed.append('t')
                dna_match.append('a')
                rna_typed.append('u')
                reader += 1
                pass
            elif input_seq[reader] == 'g':
                dna_typed.append('g')
                dna_match.append('c')
                rna_typed.append('g')
                reader += 1
                pass
            elif input_seq[reader] == 'c':
                dna_typed.append('c')
                dna_match.append('g')
                rna_typed.append('c')
                reader += 1
                pass
            elif input_seq[reader] == 'u':
                dna_typed.append('t')
                dna_match.append('a')
                rna_typed.append('u')
                reader += 1
                pass
            else:
                break
    amino_chars = []
    amino_letter = []
    aareader = 0
    while aareader < seq_len-2:
        codon_char = dna_typed[aareader:aareader+3]
        if codon_char == ['a','t','g']:
            amino_chars.append('Met')
            amino_letter.append('M')
            aareader += 3
            pass
        elif codon_char == ['t','t','a'] or codon_char == ['t','t','g'] or codon_char == ['c','t','t'] or codon_char == ['c','t','c'] or codon_char == ['c','t','a'] or codon_char == ['c','t','g']:
            amino_chars.append('Leu')
            amino_letter.append('L')
            aareader += 3
            pass
        elif codon_char == ['t','t','t'] or codon_char == ['t','t','c']:
            amino_chars.append('Phe')
            amino_letter.append('F')
            aareader += 3
            pass
        elif codon_char ==  ['t','c','t'] or codon_char == ['t','c','c'] or codon_char == ['t','c','a'] or codon_char == ['t','c','g'] or codon_char == ['a','g','c'] or codon_char == ['a','g','t']:
            amino_chars.append('Ser')
            amino_letter.append('S')
            aareader += 3
            pass
        elif codon_char == ['t','a','t'] or codon_char == ['t','a','c']:
            amino_chars.append('Tyr')
            amino_letter.append('T')
            aareader += 3
            pass
        elif codon_char == ['t','g','t'] or codon_char == ['t','g','c']:
            amino_chars.append('Cys')
            amino_letter.append('C')
            aareader += 3
            pass
        elif codon_char == ['t','g','g']:
            amino_chars.append('Trp')
            amino_letter.append('W')
            aareader += 3
            pass
        elif codon_char == ['c','c','c'] or codon_char == ['c','c','a'] or codon_char == ['c','c','t'] or codon_char == ['c','c','g']:
            amino_chars.append('Pro')
            amino_letter.append('P')
            aareader += 3
            pass
        elif codon_char == ['c','a','t'] or codon_char == ['c','a','c']:
            amino_chars.append('His')
            amino_letter.append('H')
            aareader += 3
            pass
        elif codon_char == ['c','a','a'] or codon_char == ['c','a','g']:
            amino_chars.append('Gln')
            amino_letter.append('Q')
            aareader += 3
            pass
        elif codon_char == ['c','g','g'] or codon_char == ['c','g','t'] or codon_char == ['c','g','c'] or codon_char == ['c','g','a'] or codon_char == ['a','g','g'] or codon_char == ['a','g','a']:
            amino_chars.append('Arg')
            amino_letter.append('R')
            aareader += 3
            pass
        elif codon_char == ['a','t','t'] or codon_char == ['a','t','c'] or codon_char == ['a','t','a']:
            amino_chars.append('Ile')
            amino_letter.append('I')
            aareader += 3
            pass
        elif codon_char == ['g','t','g'] or codon_char == ['g','t','t'] or codon_char == ['g','t','c'] or codon_char == ['g','t','a']:
            amino_chars.append('Val')
            amino_letter.append('V')
            aareader += 3
            pass
        elif codon_char == ['a','c','a'] or codon_char == ['a','c','c'] or codon_char == ['a','c','t'] or codon_char == ['a','c','g']:
            amino_chars.append('Thr')
            amino_letter.append('T')
            aareader += 3
            pass
        elif codon_char == ['g','c','g'] or codon_char == ['g','c','c'] or codon_char == ['g','c','t'] or codon_char == ['g','c','a']:
            amino_chars.append('Ala')
            amino_letter.append('A')
            aareader += 3
            pass
        elif codon_char == ['a','a','t'] or codon_char == ['a','a','c']:
            amino_chars.append('Asn')
            amino_letter.append('N')
            aareader += 3
            pass
        elif codon_char == ['a','a','a'] or codon_char == ['a','a','g']:
            amino_chars.append('Lys')
            amino_letter.append('K')
            aareader += 3
            pass
        elif codon_char == ['g','a','a'] or codon_char == ['g','a','g']:
            amino_chars.append('Glu')
            amino_letter.append('E')
            aareader += 3
            pass
        elif codon_char == ['g','a','t'] or codon_char == ['g','a','c']:
            amino_chars.append('Asp')
            amino_letter.append('D')
            aareader += 3
            pass
        elif codon_char == ['g','g','g'] or codon_char == ['g','g','a'] or codon_char == ['g','g','c'] or codon_char == ['g','g','t']:                
            amino_chars.append('Gly')
            amino_letter.append('G')
            aareader += 3
            pass
        elif codon_char == ['t','a','a']:
            amino_chars.append('(Ochre)')
            amino_letter.append('(Ochre)')
            aareader += 3
            pass
        elif codon_char == ['t','a','g']:
            amino_chars.append('(Amber)')
            amino_letter.append('(Amber)')
            aareader += 3
            pass
        elif codon_char == ['t','g','a']:
            amino_chars.append('(Opal)')
            amino_letter.append('(Opal)')
            aareader += 3
            pass
        else:
            break
    print("*DNA*:{}".format(''.join(dna_typed)))
    print("Match:{}".format(''.join(dna_match)))
    print("~RNA~:{}".format(''.join(rna_typed)))
    print("Amino 3 char: \n{}".format(''.join(amino_chars)))
    print("Amino 1 char: \n{}".format(''.join(amino_letter)))
    print("DNA len:{}".format(len(dna_typed)))
    print("Amino len:{}".format(len(amino_letter)))
translate_seq()
#Basic tool for amino acid / protein translation, 
#yet AminoPredict accepts both RNA and DNA as input and, 
#can predict their entire possible chronological sequence. 
#More refinements should hopefully be coming soon!
#such as:
#- Incorporating and initialising all methods through classes
#- Reverse list prediction 
#- Accounting for each stop and start codons.
#- Generating all specific peptides
#- Calculating allignment scores
#- Folding 
#- Three dimentional illustration of the folding simulation (With GridMod)
#Ruf.
