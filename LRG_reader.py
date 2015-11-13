import xml.etree.ElementTree as tree
LRG_file_tree = tree.parse('LRG_517.xml')
root=LRG_file_tree.getroot()

# variables
root_id = root.find('fixed_annotation/id').text
root_hgnc = root.find('fixed_annotation/hgnc_id').text
root_organism = root.find('fixed_annotation/organism').text
root_creation_date = root.find('fixed_annotation/creation_date').text
root_source = root.find('fixed_annotation/source/contact')
root_source_name = root_source.find('name').text
root_source_address = root_source.find('address').text
root_source_email= root_source.find('email').text

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
q	elif i<len(exons):
		introns.append({'intron_number':i, 'start':(int(exons[i-1]['end'])+1), 'end':(int(exons[i]['start'])-1)})
	else:
		introns.append({'intron_number':i, 'start':(int(exons[i-1]['end'])+1), 'end':len(sequence)})

for i in introns:
	print i

intron_sequences=[]
for i in range(len(introns)):
	intron_sequences.append(sequence[introns[i]['start']:introns[i]['end']])

print (intron_sequences[0])


# Export intron information to an XML file

# establish root and child
output = tree.Element("lrg_introns", schema_version = root.attrib['schema_version'])
schema_details = tree.SubElement(output, "schema_details")

# schema details
tree.SubElement(schema_details, "id").text = root_id
tree.SubElement(schema_details, "hgnc_id").text = root_hgnc
tree.SubElement(schema_details, "organism").text = root_organism

# new subelement
source = tree.SubElement(schema_details, "source")
contact_details = tree.SubElement(source, "contact_details")

if root_source_name != None:
	tree.SubElement(contact_details, "name").text = root_source_name
	tree.SubElement(contact_details, "name").text = root_source_address
	tree.SubElement(contact_details, "name").text = root_source_email
	
 

# export xml
tree = tree.ElementTree(output)
tree.write("alex_test_file.xml")
