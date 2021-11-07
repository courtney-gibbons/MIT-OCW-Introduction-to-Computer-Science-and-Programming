#Problem Set 3d
#Name: Courtney Gibbons
#Time: 1:00
#
import string

def subStringMatchExact(target,key):
    '''Lists the indexes where the key string is in the target string'''
    tuple = ()
    startPos = 0
    #print string.rfind(target,key)
    while startPos < string.rfind(target,key):
        pos = string.find(target,key,startPos)
        tuple = tuple + (pos,)
        startPos = pos + 1
    #print tuple
    return tuple

def constrainedMatchPair(firstMatch,secondMatch,length):
    tuple = ()
    for start1 in range(0, len(firstMatch)):
        for start2 in range(0, len(secondMatch)):
            if firstMatch[start1] + length + 1 == secondMatch[start2]:
                tuple = tuple + (firstMatch[start1],)
                #print tuple
    return tuple

def subStringMatchOneSub(target,key):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        #miss picks location for missing element
        #key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        #print 'breaking key',key,'into',key1,key2
        #match1 and match2 are tuples of locations of start of matches
        #for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        #when we get here, we have two tuples of start points
        #need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        #print 'match1',match1
        #print 'match2',match2
        #print 'possible matches for',key1,key2,'start at',filtered
    listAns = list(allAnswers)
    listAns = list(dict.fromkeys(listAns))
    listAns = sorted(listAns)
    allAnswers = tuple(listAns)
    return allAnswers

def subStringMatchExactlyOneSub(target,key):
    tuple = ()
    exact = subStringMatchExact(target,key)
    oneSubAndExact = subStringMatchOneSub(target,key)
    print exact
    print oneSubAndExact
    for indexes in oneSubAndExact:
        if indexes not in exact:
            tuple = tuple + (indexes,)
    return tuple
            
print subStringMatchExactlyOneSub('atgacatgcacaagtatgcat','atg')

#target strings

#target1 = 'atgacatgcacaagtatgcat'
#target2 = 'atgaatgcatggatgtaaatgcag'

#key strings

#key10 = 'a'
#key11 = 'atg'
#key12 = 'atgc'
#key13 = 'atgca'
