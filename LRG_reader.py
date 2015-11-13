import xml.etree.ElementTree as tree
import re
file_name=raw_input('Please enter file name:')
LRG_file_tree = tree.parse(file_name)
root=LRG_file_tree.getroot()

# variables
root_schema_version = root.attrib['schema_version']
root_id = root.find('fixed_annotation/id').text
root_hgnc = root.find('fixed_annotation/hgnc_id').text
root_organism = root.find('fixed_annotation/organism').text
root_creation_date = root.find('fixed_annotation/creation_date').text
root_source = root.find('fixed_annotation/source/contact')
root_source_name = root_source.find('name').text
root_source_address = root_source.find('address').text
root_source_email= root_source.find('email').text
sequence=root.find('fixed_annotation/sequence').text
sequence=sequence.upper()


# assert correct schema verison
assert root.attrib['schema_version'] == '1.9' , 'wrong schema version'


def exons(transcript, exon_num):		#this function returns the exon information for a given transcript/exon number
	exon_list=[]
	a='fixed_annotation/transcript[@name="'+transcript+'"]/exon'	#creating serach string for findall function
	for elem in root.findall(a):				#finds all exons in transcript
		for cords in elem.findall('coordinates'):
			if cords.attrib['coord_system']==root_id:		#ensures right transcript sequence selected, not protein or coding
				b = cords.attrib
		if elem.attrib['label'].isdigit():
			b['exon']=elem.attrib['label']
		else:
			b['exon']=re.sub("\D", "",elem.attrib['label'])
		exon_list.append(b)	
	assert exon_list[exon_num-1]['exon']==str(exon_num) , 'exon number in label does not match exon number requested'+ transcript + ' ' + str(exon_num)
	return exon_list[exon_num-1]


total_length=root.find('fixed_annotation/transcript/coordinates').attrib['end']
assert len(sequence)==(int(total_length)+2000) , 'Length of sequence wrong'

for i in sequence:
	a=['A', 'T', 'C', 'G']
	assert i in a , "not atcg"

def introns(transcript, intron_num):
	a='fixed_annotation/transcript[@name="'+transcript+'"]/exon'
	if intron_num ==0:
		return {'intron': 0, 'start':0, 'end': 5000}
	elif intron_num < len(root.findall(a)):
		return {'intron': intron_num, 'start':int(exons(transcript, intron_num)['end'])+1, 'end':int(exons(transcript, intron_num+1)['start'])-1}
	elif intron_num == len(root.findall(a)):
		return {'intron':intron_num, 'start':int(exons(transcript, intron_num)['end'])+1, 'end':int(exons(transcript, intron_num)['end'])+2000}

def intron_sequence(transcript, intron_num ):
	assert len(sequence[introns(transcript, intron_num)['start']:introns(transcript, intron_num)['end']])==introns(transcript, intron_num)['end']-introns(transcript, intron_num)['start'] , 'intron length wrong'
	return sequence[introns(transcript, intron_num)['start']:introns(transcript, intron_num)['end']]



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
	
 
transcripts=[]
for i in root.findall('fixed_annotation/transcript'):
	x=i.attrib['name']
	transcripts.append(x)

for i in transcripts:
	intron_details = tree.SubElement(output, "intron_details", transcript=i)
	for j in range(len(root.findall('fixed_annotation/transcript[@name="'+i+'"]/exon'))):
		intron = tree.SubElement(intron_details, "intron", number=str(j), start=str(introns(i,j)['start']), end=str(introns(i,j)['end'])).text=intron_sequence(i,j)
		
# export xml
tree = tree.ElementTree(output)
#tree.write("alex_test_file2.xml")
tree.write("introns_" + root_id + ".xml")
