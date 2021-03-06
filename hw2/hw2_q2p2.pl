=pod
 David S. Li
 110328771
 CSE 337 HW#2
=cut

use strict;
use warnings;

# INCOMPLETE
sub formatMaxLine {
  my $max_length = $_[0];
  my $input_dir = $_[1];
  my $output_dir = $_[2];

  open(my $input_file, "<", $input_dir) or die("Cannot open input file.");
  open(my $output_file, ">", $output_dir) or die("Cannot open output file.");

  my $substr = "";
  my $n = 0;
  while (my $line = <$input_file>) {
    chomp($line);
    my @words = split(" ", $line);
    foreach my $word(@words) {
      my $len = length($word);
      if ($n + $len > $max_length) {
        print $output_file "$substr\n";
        $substr = "";
        $n = 0;
      }
      $substr .= "$word ";
      $n += $len + 1;
    }
  }
  print $output_file "$substr\n";
  close($input_file); close($output_file);
}

formatMaxLine(18, "sample_input_q2.txt", "sample_output_q2.txt");
