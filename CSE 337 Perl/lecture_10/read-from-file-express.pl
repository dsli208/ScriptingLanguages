# Perl supports a convenient way to read input files for processing. 
# You can simply add file names at the command line, perl will 
# automatically concatenate these files together, and the <> 
# operator automatically reads it rather than from STDIN 
#
# To try with this script, type: 
# 	perl thisscript.pl file1 file2 file3
# 
# see Slide 4-3 for the meanings of $. and $_
#
use strict;
use warnings;

while (<>) {
      print "$.: $_";      
}

print "\n$. lines in total\n\n";

