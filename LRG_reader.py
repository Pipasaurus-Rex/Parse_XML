import xml.etree.ElementTree as tree
LRG_file_tree = tree.parse('LRG_517.xml')
root=LRG_file_tree.getroot()

print " "
print "Schema Details"
print" "
print "Schema Version:", root.attrib['schema_version']
assert root.attrib['schema_version'] == '1.9' , 'wrong schema version'
print "Schema ID:", root.find('fixed_annotation/id').text
print "Schema HGNC ID:", root.find('fixed_annotation/hgnc_id').text
print "Organism:", root.find('fixed_annotation/organism').text
elem = root.find('fixed_annotation/source/contact')
name = elem.find('name').text
address = elem.find('address').text
email= elem.find('email').text
print "Source Name:", name
print "Source Address:", address
print "Source E-mail:", email
print "Creatation Date:", root.find('fixed_annotation/creation_date').text
print" "
tran = root.find('fixed_annotation/transcript')
print "Transcript Name:", tran.attrib['name']
for element in root.findall('fixed_annotation/transcript/coordinates'):
    print "Co-ordinate system:", element.attrib['coord_system']			#nood this for loop since more than one transcript

sequence=root.find('fixed_annotation/sequence').text
sequence=sequence.upper()
lrg_num=root.find('fixed_annotation/id').text

exons=[]
for elem in root.findall('fixed_annotation/transcript/exon'):
	for cords in elem.findall('coordinates'):
		if cords.attrib['coord_system']==lrg_num:
			a = cords.attrib
	a['exon']=elem.attrib['label']     #adding exon number to dictionary
	exons.append(a)

total_length=root.find('fixed_annotation/transcript/coordinates').attrib['end']
assert len(sequence)==(int(total_length)+2000) , 'Length of sequence wrong'

for i in sequence:
	a=['A', 'T', 'C', 'G']
	assert i in a , "not atcg"

introns=[]
for i in range(len(exons)+1):
	if i==0:
		introns.append({'intron_number':i, 'start':0, 'end':5000})
	elif i<len(exons):
		introns.append({'intron_number':i, 'start':(int(exons[i-1]['end'])+1), 'end':(int(exons[i]['start'])-1)})
	else:
		introns.append({'intron_number':i, 'start':(int(exons[i-1]['end'])+1), 'end':len(sequence)})

for i in introns:
	print i

intron_sequences=[]
for i in range(len(introns)):
	intron_sequences.append(sequence[introns[i]['start']:introns[i]['end']])

print (intron_sequences[0])
