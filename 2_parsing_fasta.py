
import urllib2  # to read file from url
from StringIO import StringIO # to convert string to 'handle'
from Bio import SeqIO # to parse Seq data

# get 'file'
url = "http://biopython.org/DIST/docs/tutorial/examples/ls_orchid.fasta"
data = urllib2.urlopen(url)
str = data.read() # convert contents to string

# convert to handle (behaves like open file),
# necessary for SeqIO
handle = StringIO(str)
print handle

num = 1
# loop through all sequence records in the file
for seq_record in SeqIO.parse(handle, "fasta"):
    print "sequence #", num
    print "===================================="
    print seq_record
    print "===================================="
    print
    print "ID = ", seq_record.id
    print seq_record.seq
    print "seq length = ", len(seq_record)
    print
    num = num + 1

