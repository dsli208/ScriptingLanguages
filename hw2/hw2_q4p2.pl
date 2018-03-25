use strict;
use warnings;

print "What string do you want to search for?\n";
my $input = <STDIN>;
chomp($input);

opendir(my $dir, ".");

while (readdir $dir) {
  open(my $file, "<", $_) or next;
  while(my $line = <$file>) {
    if (index($line, $input) >= 0) {
      print "Found $input in file $_ .......... ";
      if (-e $file) {
        print "e";
      }
      if (-r $file) {
        print "r";
      }
      if (-w $file) {
        print "w";
      }
      if (-x $file) {
        print "x";
      }
      if (-T $file) {
        print "T";
      }
      print "\n";
      last;
    }
  }

}
