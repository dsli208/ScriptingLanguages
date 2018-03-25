=pod
 David S. Li
 110328771
 CSE 337 HW#2
=cut

use strict;
use warnings;

sub reverseAndSort {
my $input_dir = $_[0];
my $num_lines = 0; my $num_words = 0; my $num_chars = 0;
my @lines = ();
open(my $input_file, "<", $input_dir) or die("Cannot open file.");
while(my $line = <$input_file>) {
    $num_lines += 1;
    my @words = split(" ", $line);
    $num_words += @words;
    $num_chars += length($line);
    push @lines, "$line";
}

close($input_file);

print "lines: $num_lines, words: $num_words, chars: $num_chars\n";
my @reverse_lines = reverse(@lines);
foreach my $line (@reverse_lines) {
  my $reverse_line = reverse($line);
  print "$reverse_line";
}
}

reverseAndSort("input21.txt");
