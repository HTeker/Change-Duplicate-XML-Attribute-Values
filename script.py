import codecs

# CONSTANTS
ATTRIBUTES = {
    "FIRST ATTR NAME",
    "SECOND ATTR NAME"
}
REPLACE_ATTR = "ATTR NAME THAT NEEDS TO BE CHANGED"
REPLACE_WITH = "NEW VALUE FOR THE CHANGED ATTR"
PATH_TO_XML_FILE = ("YOUR PATH TO THE XML FILE").replace("\\", "/")
# CONSTANTS

def getValueOfAttribute(line, attr):
    if attr in line:
        return line.split(attr + '="')[-1].split('"')[0]
    else:
        return False

f = codecs.open(PATH_TO_XML_FILE, "r", encoding="utf8")
n = codecs.open(PATH_TO_XML_FILE.replace(".xml", " REPLACED.xml"), "w", encoding="utf8")

for line in f.readlines():
    firstAttr = ""
    secondAttr = ""

    for attr in ATTRIBUTES:
        if attr + '="' in line:
            if(firstAttr == ""):
                firstAttr = getValueOfAttribute(line, attr)
            else:
                secondAttr = getValueOfAttribute(line, attr)

    if(firstAttr == secondAttr and getValueOfAttribute(line, REPLACE_ATTR)):
        print("Replacing value of " + REPLACE_ATTR + ": " + getValueOfAttribute(line, REPLACE_ATTR) + " -> " + REPLACE_WITH)
        line = line.replace(REPLACE_ATTR + '="' + getValueOfAttribute(line, REPLACE_ATTR), REPLACE_ATTR + '="' + REPLACE_WITH)

    n.write(line)
    firstAttr = ""