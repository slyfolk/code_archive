def practice():	
	"""code practice"""
	a = ["a","b", "c", "d", "e"]
	b = ("a","b", "c", "d", "e")
	c = {"a","b", "c", "d", "e"}
	d = "abcde"
	e = ":".join(b)
	print(type(e))
	print(":".join(a))
	print(":".join(b))
	print(":".join(c))
	print(":".join(d))

	for i in a:
		print ("list item {}".format(i)) # ordered
	print()

	for i in b:
		print ("tuple item {}".format(i)) # ordered
	print()
	for i in c:
		print ("set item {}".format(i)) # unordered
	print()

	for i in d:
		print ("string item {}".format(i)) # ordered
	print()
	print()
	print('list length {}'.format(len (a)))
	print()
	print('tuple length {}'.format(len (b)))
	print()
	print('set length {}'.format(len (c)))
	print()
	print('string length {}'.format(len (d)))
	"""len() FUNCTION"""
	'''The len() function works with strings, lists, sets and tuples'''
	"""DOT COUNT FUNCTION"""
	"""dotcount function works on strings, lists, and tuples...but not set and dictionaries"""
	print ("list count {}".format(a.count("a")))
	print()
	print ("tuple count {}".format(b.count("a")))
	print()
	print ("string count {}".format(a.count("a")))
	print()

	"""DOT REPLACE FUNCTION"""
	"""dotreplace for strings only. Returns attribute error with sets, lists and tuples"""
	print (d.replace("a", str(5)))  #replace item in string(IMMUTABLE)
	print (d)
	print()

	'''index reassignment for lists only. Returns TYPE ERROR with sets, strings and tuples '''
	a[0] = 5 
	print("for list: {}".format(a)) #replaced item in list(MUTABLE)
	print()


	"""indexing for strings, lists and tuples only...Items accessed via indexing. Return ATTRIBUTE ERROR with sets."""
	print("for tuple: {}".format(b[0])) # print tuple item (IMMUTABLE)
	print
	print("for string: {}".format(d[0])) #print string character(IMMUTABLE)
	print
	print("for list: {}".format(a[0])) #print list item (MUTABLE)
	print

	'''DOT INDEX FUNCTION'''
	'''dotindex function works with lists, strings and tuplesonly but not sets and tuples'''
	print("for string: {}".format(d.index("a", 0, 3))) #prints string index
	print ()
	print("for list: {}".format(a.index(5, 0, 3))) #prints list index
	print ()
	print("for tuple: {}".format(b.index("a", 0, 4))) #prints tuple index
	print()

	'''FUNCTIONS WORKING WITH STRINGS'''
	'''
	s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
	s.strip() -- returns a string with whitespace removed from the start and end
	s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
	s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
	s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
	s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'

	s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is
	not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a
	convenient special case s.split() (with no arguments) splits on all whitespace chars.

	SLICE FUNCTION slice s[start:end]
	s[1:4] is 'ell' -- chars starting at index 1 and extending up to but not including index 4
	s[1:] is 'ello' -- omitting either index defaults to the start or end of the string
	s[:] is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic
	way to copy a sequence like a string or list)
	s[1:100] is 'ello' -- an index that is too big is truncated down to the string length

	ENCODING AND DECODING STRINGS
	a = 'I am blessed' #unicode code
	print (a.encode('utf-8'))#(encode) to bytecode
	b=a.encode('utf-8') #bytecode
	print (b.decode('utf-8'))#(decode) to unicode
	t = unicode(b, 'utf-8') #(decode) to unicode
	'''

	a = 'I am blessed' #unicode code
	print(a.split())
	print (a.encode('utf-8'))#(encode) to bytecode
	b=a.encode('utf-8') #bytecode
	print (b.decode('utf-8'))#(decode) to unicode

	"""LIST METHODS/FUNCTIONS"""
	'''
	Here are some other common list methods.
	list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
	list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
	list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
	list.index(elem) -- searches for the given element from the start of the list and returns its
	index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
	list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
	list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
	list.reverse() -- reverses the list in place (does not return it)
	list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

	s.join(list) -- opposite of split(), joins the elements in the given list together using the string
	as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
	'''
	a = ["a","b", "c", "d", "e"]
	print (':'.join(a))

if __name__ == '__main__':
	practice()
		


