#Problem Set 3b
#Name: Courtney Gibbons
#Time: 15
#
import string

def subStringMatchExact(target,key):
    '''Counts the number of times the key string is in the target string'''
    tuple = ()
    startPos = 0
    #print string.rfind(target,key)
    while startPos < string.rfind(target,key):
        pos = string.find(target,key,startPos)
        tuple = tuple + (pos,)
        startPos = pos + 1
    print tuple

print subStringMatchExact("atgacatgcacaagtatgcat","atgc")

#target strings

#target1 = 'atgacatgcacaagtatgcat'
#target2 = 'atgaatgcatggatgtaaatgcag'

#key strings

#key10 = 'a'
#key11 = 'atg'
#key12 = 'atgc'
#key13 = 'atgca'

#the following procedure you will use in Problem 3

#def subStringMatchOneSub(key,target):
#    """search for all locations of key in target, with one substitution"""
#    allAnswers = ()
#    for miss in range(0,len(key)):
#        #miss picks location for missing element
#        #key1 and key2 are substrings to match
#        key1 = key[:miss]
#        key2 = key[miss+1:]
#        print 'breaking key',key,'into',key1,key2
#        #match1 and match2 are tuples of locations of start of matches
#        #for each substring in target
#        match1 = subStringMatchExact(target,key1)
#        match2 = subStringMatchExact(target,key2)
#        #when we get here, we have two tuples of start points
#        #need to filter pairs to decide which are correct
#        filtered = constrainedMatchPair(match1,match2,len(key1))
#        allAnswers = allAnswers + filtered
#        print 'match1',match1
#        print 'match2',match2
#        print 'possible matches for',key1,key2,'start at',filtered
#    return allAnswers
