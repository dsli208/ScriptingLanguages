=pod
 David S. Li
 110328771
 CSE 337 HW#2
=cut

use strict;
use warnings;

# this subroutine uses TWO arguments, first is input and second is output
sub sortTextByLength {
my $input_dir = $_[0];
my $output_dir = $_[1];
my %lines = ();

open(my $input_file, "<", $input_dir) or die("Cannot open input file.");

# Assemble a HASH of the lines (key) and their length (value)
while(my $line = <$input_file>) {
    #print "$line\n";
    chomp($line);
    my $len = length($line);
    $lines{$line} = $len;
    #print "$lines{$line}\n";
}

close($input_file);

open(my $output_file, ">", $output_dir) or die("Cannot open output file.");

# Now, sort the hash

while (keys %lines > 0) {
  # Look for the key with the LEAST VALUES
  my $shortest_line = (keys %lines)[0];
  my $min_len = $lines{$shortest_line};
  while (my ($line, $len) = each (%lines)) {
    if ($len < $min_len) {
        $shortest_line = $line;
        $min_len = $len;
    }
  }

  # Now, having obtained our key, write it to output before deleting it from the HASH
  #print "$min_len\n";
  print $output_file "$shortest_line\n";
  delete $lines{$shortest_line};
}

close($output_file);
}

sortTextByLength("sample_input_q2.txt", "output_q2p1.txt");
