
import urllib2  # to read file from url
from StringIO import StringIO # to convert string to 'handle'
from Bio import SeqIO # to parse Seq data

# get 'file'
url = "http://biopython.org/DIST/docs/tutorial/examples/ls_orchid.gbk"
data = urllib2.urlopen(url)
str = data.read() # convert contents to string

# convert to handle (behaves like open file), necessary for SeqIO
handle = StringIO(str)
print handle

## gets an iterator that allows you to go through each
## entry
iter = SeqIO.parse(handle, "genbank")

# gets next sequence (which is the 1st one here)
seq_record = next(iter)

print "===================================="
print seq_record
print "===================================="
print
print "ID = ", seq_record.id
print seq_record.seq
print "seq length = ", len(seq_record)
print

## look at the features
print seq_record.features
print

# look at first feature
f = seq_record.features[1]
print "type = ", f.type
print "location = ", f.location
print

# we can get the 'start' and 'end' of a location, which
# corresponds to seq[start:end],
# i.e., start is starting index and
# end is end index + 1
start = f.location.start
end = f.location.end
print "sequence of feature: ", seq_record.seq[start:end]



