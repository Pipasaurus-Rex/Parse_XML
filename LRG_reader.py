import xml.etree.ElementTree as tree

LRG_file_tree = tree.parse('LRG_517.xml')
root=LRG_file_tree.getroot()

sequence=root.find('fixed_annotation/sequence').text
lrg_num=root.find('fixed_annotation/id').text


exons=[]
for elem in root.findall('fixed_annotation/transcript/exon'):
	for cords in elem.findall('coordinates'):
			a = cords.attrib
	a['exon']=elem.attrib['label']     #adding exon number to dictionary
	exons.append(a)
