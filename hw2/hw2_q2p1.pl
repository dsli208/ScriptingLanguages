use strict;
use warnings;

my %lines = ();

open(my $input_file, "<", "sample_input_q2.txt") or die("Cannot open input file.");

# Assemble a HASH of the lines (key) and their length (value)
while(my $line = <$input_file>) {
    #print "$line\n";
    my $len = length($line);
    $lines{$line} = $len;
    #print "$lines{$line}\n";
}

close($input_file);

open(my $output_file, ">", "output_q2p1.txt") or die("Cannot open output file.");

# Now, sort the hash

while (keys %lines > 0) {
  # Look for the key with the LEAST VALUES
  my $shortest_line = (keys %lines)[0];
  print "Shortest line: $shortest_line $lines{$shortest_line}\n";
  foreach (my ($line, $len) = each (%lines)) {
    print "$line ($lines{$line}) vs. $shortest_line ($lines{$shortest_line})";
    if ($len < length($shortest_line)) {
        $shortest_line = $line;
    }
  }

  # Now, having obtained our key, write it to output before deleting it from the HASH
  print $output_file "$shortest_line\n";
  delete $lines{$shortest_line};
}

close($output_file);
