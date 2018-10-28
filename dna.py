'''Project to carry out DNA analysis for a crime investigation'''
'''VT 28/10/2018'''

from time import sleep

#list of codons
sample = ['GTA','GGG','CAC']

#read dna file
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file,'r') as f:
    for line in f:
      dna_data += line
  return dna_data
      
#build dna codons
def dna_codons(dna):
  codons = []
  for i in range(0,len(dna),3):
    if (i + 3) < len(dna):
      codons.append(dna[i:i + 3])
  return codons
    
#match dna
def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
      print "Codon: %s" % codon 
  return matches
    
#determine if a suspect is the criminal
def is_criminal(dna_sample):
  print 'Searching dna for matches...'
  sleep(2)
  print
  
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  
  if num_matches >= 3:
    print 'Number of codon matches: %s. DNA profile matches.' % (num_matches)
    print 'The investigation should continue into this suspect'
    print '****************************************************'
    print
  else:
    print 'Matches = %s' % (num_matches)
    print 'The suspect can be freed'
    print '****************************************************'
    print
    
    
is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')


    
    
    
  
  
  
  
  
  
  
  
