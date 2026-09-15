# 9]  Explain the following code: d = {'person': 2, 'cat': 4, 'spider': 8} for animal in d: legs = d[animal] print('A %s has %d legs' % (animal, legs)) '''

"""d is a dictionary containing animals (keys) and their number of legs (values).
for animal in d: loops through each key in the dictionary.
legs = d[animal] retrieves the corresponding value (number of legs).
print('A %s has %d legs' % (animal, legs)) prints the animal and its number of legs using string formatting.
%s → string
%d → integer
Output
A person has 2 legs
A cat has 4 legs
A spider has 8 legs """