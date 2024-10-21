# we have norway text in old style formatting
# re-write the same text as:
# #1 string with format() call
# #2 f-string

norway_text = 'Automatisering akselererer %syeblikket da roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
print(norway_text)
