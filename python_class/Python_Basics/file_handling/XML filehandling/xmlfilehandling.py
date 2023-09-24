"XML - Extensible Markup Language"

"To read XML string"
# data = '''\
# <?xml version="1.0" encoding="UTF-8"?>
# <metadata>
# <food>
#     <item name="breafast">idily</item>
#     <price>$2.5</price>
#     <description>
#     two idyly's with chatney
#     </description>
#     <calories>553</calories>
# </food>
# <food>
#     <item name="breafast">Dosha</item>
#     <price>$1.5</price>
#     <description>
#     Dosha with vada
#     </description>
#     <calories>700</calories>
# </food>
# </metadata>'''
# import xml.etree.ElementTree as a
# e = a.fromstring(data)
# print(e)
# print(e.tag)
# print(e[0].tag)
# print(e[1].tag)
# print(e[0][1].tag)
# print(e[1][2].tag)
".........................................................................................................."
"To read XML files"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# print(e)
# print(e.tag)
# print(e[0].tag)
# print(e[1].tag)
# print(e[0][1].tag)
# print(e[1][2].tag)
".........................................................................................................."
"To prints tags using loop"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# for i in e[0]:
#     print(i.tag)
".........................................................................................................."
"To view attributes of a tag"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# for i in e:
#     print(i.tag,i.attrib)
".........................................................................................................."
"To view attributes of a tag inside tag"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# for i in e[0]:
#     print(i.tag,i.attrib)
".........................................................................................................."
"To view content text in a xml tag"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# for i in e.findall('book'):
#     print(f"{i.find('author').text},{i.find('title').text}")
".........................................................................................................."
"To add a new text into xml files"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# for i in e.iter('description'):
#     c = str(i.text+"\n\t\tNew data has been added")
#     i.text = c
# a.write('editting_sample.xml')
".........................................................................................................."
"To add a new text in a single into xml files"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# for i in e[0].iter('description'):
#     c = str(i.text+"\n\t\tindex 0 description updated")
#     i.text = c
# a.write('editting_sample.xml')
".........................................................................................................."
"To add tags into an xml file"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# b.SubElement(e[0],'addedtag')
# for i in e[0].iter('addedtag'):
#     c = str("this is an added tag")
#     i.text = c
# a.write('addingtags.xml')
".........................................................................................................."
"To create a tag under every indices"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# for i in e:
#     b.SubElement(i,'addedtag')
# for i in e.iter('addedtag'):
#     c = str("this is an added tag")
#     i.text = c
# a.write('addingtags2.xml')
".........................................................................................................."
"To remove attribute from an xml tag"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# e[0][0].attrib.pop('id')
# a.write('removedattribute.xml')
".........................................................................................................."
"To clear an entire section or tag"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# e[0].clear()
# a.write('cleared.xml')
".........................................................................................................."
"To get output from xml file  to terminal"
# import xml.etree.ElementTree as b 
# a = b.parse('sample.xml')
# e = a.getroot()
# b.dump(e)
".........................................................................................................."