import xml.etree.ElementTree as tree
LRG_file_tree = tree.parse('LRG_517.xml')
root=LRG_file_tree.getroot()

print " "
print "Schema Details"
print" "
print "Schema Version:", root.attrib['schema_version']
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
lrg_num=root.find('fixed_annotation/id').text

exons=[]
for elem in root.findall('fixed_annotation/transcript/exon'):
	for cords in elem.findall('coordinates'):
			a = cords.attrib
	a['exon']=elem.attrib['label']     #adding exon number to dictionary
	exons.append(a)
