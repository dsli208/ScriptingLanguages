=pod
 David S. Li
 110328771
 CSE 337 HW#2
=cut
use strict;
use warnings;

open(my $input_file, "<", "passwd.txt") or die("Cannot open file.");

while(my $line = <$input_file>) {
    my @table_row = split(":", $line);
    if (@table_row[2] % 2 == 0) {
      print "@table_row[0], @table_row[2]\n";
    }
}

close($input_file);
