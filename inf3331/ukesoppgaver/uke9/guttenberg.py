#Task 9.4 - Arnab Kumar Datta (arnabkd)
import sys
from collections import Counter
try:
    file = open(sys.argv[1], 'r')
except:
    print "File not found"

content = []
for line in file:
    for word in line.split(' '):
        content.append(word.strip(',\n.\r\t\s').lower())
file.close()

count = Counter(content)
print count

Runtime example
"""
arnab@arnab-ThinkPad-Z61t:~/uni/inf3331/inf3331/ukesoppgaver/uke9$ more task-desc.txt 
9.4 Literary Analysis
Description
Your English teacher has just asked you to write a paper comparing two of the works from the free, online literature library at Project Guten
berg. Since you are a computer scientist, you decide to put your skills to use. You plan to compare your two favorite works of classic litera
ture in terms of the vocabulary used in each. Since this a bit outside the scope of the assignment as described by your English teacher, you 
ask for permission before you proceed. Intruiged by your proposal, your English teacher agrees and you are ready to go.

You plan to write a program that will take a text file as input and return a report listing alphabetically all the words in the file and the 
number of occurances of each.

This exercise is copied from openbookproject.net under the GNU Free Documentation License.
arnab@arnab-ThinkPad-Z61t:~/uni/inf3331/inf3331/ukesoppgaver/uke9$ python guttenberg.py task-desc.txt 
Counter({'the': 9, 'you': 8, 'a': 8, 'to': 6, 'of': 6, 'your': 6, 'teacher': 3, 'and': 3, 'in': 3, 'english': 3, '': 2, 'each': 2, 'are': 2, 'since': 2, 'free': 2, 'by': 2, 'from': 2, 'two': 2, 'work': 2, 'file': 2, 'write': 2, 'literature': 2, 'plan': 2, 'thi': 2, 'all': 1, 'just': 1, 'text': 1, 'paper': 1, 'kill': 1, 'go': 1, 'before': 1, 'literary': 1, 'program': 1, 'listing': 1, 'input': 1, 'return': 1, 'permission': 1, 'decide': 1, 'report': 1, 'bit': 1, 'term': 1, 'occurance': 1, 'library': 1, 'computer': 1, 'project': 1, 'openbookproject.net': 1, 'for': 1, 'outside': 1, 'cientist': 1, 'exercise': 1, 'alphabetically': 1, 'ask': 1, 'described': 1, 'license': 1, 'favorite': 1, 'asked': 1, 'number': 1, 'put': 1, 'use': 1, 'proceed': 1, 'comparing': 1, '9.4': 1, 'proposal': 1, 'analysi': 1, 'cope': 1, 'under': 1, 'ha': 1, 'copied': 1, 'word': 1, 'gnu': 1, 'will': 1, 'agree': 1, 'compare': 1, 'classic': 1, 'at': 1, 'ready': 1, 'that': 1, 'take': 1, 'online': 1, 'intruiged': 1, 'description': 1, 'vocabulary': 1, 'assignment': 1, 'gutenberg': 1, 'i': 1, 'documentation': 1, 'used': 1})
arnab@arnab-ThinkPad-Z61t:~/uni/inf3331/inf3331/ukesoppgaver/uke9$ 
"""
            


