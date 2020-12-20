from lxml import etree

tree = etree.parse("web_page.html") #parsing the html file
print(etree.tostring(tree)) #prints the entire tree

title_element = tree.find('head/title') #finding the head tag then the title tag
print(title_element.text)

body_ele = tree.find('body/p') #finding the body tag then the paragraph tag
print(body_ele.text)

list_items = tree.findall('body/ul/li')#finding the ul tag > then li tags in the tree
print(list_items) #only prints the content in the list tag, doesn't check for anchor tag

for li in list_items: #see how it doesn't care about the anchor tag in the second list
    print(li.text)

# we right a for loop to iterate through the list item 
for li in list_items:
    a = li.find('a')
    if a is not None: #this cond checks the presence of any anchor tags
        print(f"{li.text.strip()} {a.text}") #if yes, prints the anchor tag
    else:
        print(li.text)
        
#The above model is inefficient coz, we have to specify the entire path of the object we want to extract

#using the XPATH instead of find
tree = etree.parse("web_page.html")

title_ele = tree.xpath("//title")[0] #directly calling the title tag, instead of specifying it's parent tag
#xpath returns the objects as lists, have to use indexing to retrieve the results.
print(title_ele.text)        

#calling the text function in the xpath itself
title_ele_alt = tree.xpath("//title/text()")[0]
print(title_ele_alt)

#retreiving the paragraph tag using xpath
para_ele = tree.xpath("//p/text()")[0]
print(para_ele)

list_items = tree.xpath("//li")

for i in list_items:
    print(i.xpath(".//text()")) #The o/p is 2 list objs with incorrect formatting
    #has new lines \n in it. let's clean up the o/p
#['Web Scraping with Python using Requests, LXML and Splash']
# ['Created by:', 'Ahmed Rafik', '']

for i in list_items:
    text = ''.join(map(str.strip, i.xpath(".//text()")))
    print(text)
# Web Scraping with Python using Requests, LXML and Splash
# Created by:Ahmed Rafik


#Using CSS Selectors to extract the elements from html

title_ele_css = tree.cssselect("title")[0]
print(title_ele_css.text) #gives AttributeError: 'lxml.etree._ElementTree' object has no attribute 'cssselect'
# css selector don't work with etree element objects, they work with html

#converting the tree obj to html obj
html = tree.getroot()

title_ele_css = html.cssselect("title")[0]
print(title_ele_css.text)

para_css = html.cssselect("p")[0]
print(para_css.text)

list_items_css = html.cssselect("li")

for li in list_items_css:
    a = li.cssselect("a")
    # a returns the following:
# []
# [<Element a at 0x154e97e5340>]
    #Extracting the anchor tag and list elements using the if-else cond".
    if len(a) == 0:
        print(li.text)
    else:
        print(f"{li.text.strip()} {a[0].text}")