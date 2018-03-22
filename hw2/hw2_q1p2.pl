use strict;
use warnings;

my @lines = ();
open(my $input_file, "<", "passwd.txt") or die("Cannot open file.");
while(my $line = <$input_file>) {
    my @table_row = split(":", $line);
    push @lines, "$table_row[0], $table_row[2]\n";
}

my @reverse_lines = reverse(@lines);
print "@reverse_lines";

close($input_file);
