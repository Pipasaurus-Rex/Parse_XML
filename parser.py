import xml.etree.ElementTree as tree
print " "
print "Schema Details"
LRG_file_tree = tree.parse('LRG_517.xml')
root=LRG_file_tree.getroot()
print" "
print "Schema Version:", root.attrib['schema_version']
for element  in LRG_file_tree.iter(tag='id'):
    print "Schema ID:", element.text
for element in LRG_file_tree.iter(tag='hgnc_id'):
    print "Schema HGNC ID:", element.text
for element in LRG_file_tree.iter(tag='organism'):
    print "Organism:", element.text
elem = root.find('fixed_annotation/source/contact')
name = elem.find('name').text
address = elem.find('address').text
email= elem.find('email').text
print "Source Name:", name
print "Source Address:", address
print "source E-mail:", email
for element  in LRG_file_tree.iter(tag='creation_date'):
    print "Creatation Date:", element.text
    

