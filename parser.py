import xml.etree.ElementTree as tree
print " "
print "Schema Version"
LRG_file_tree = tree.parse('LRG_517.xml')
root=LRG_file_tree.getroot()
print root.attrib['schema_version']

