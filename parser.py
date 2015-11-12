import xml.etree.ElementTree as tree
print " "
print "Schema Details"
LRG_file_tree = tree.parse('LRG_517.xml')
root=LRG_file_tree.getroot()
id=root[0][0].text
hgnc_id=root[0][1].text
print" "
print "Schema Version:", root.attrib['schema_version']
print "Schema ID:",  id
print "Schema HGNC ID:", hgnc_id
#print "list of moons"
#for element  in planets_tree.iter(tag='moon'):
#    print element.attrib


