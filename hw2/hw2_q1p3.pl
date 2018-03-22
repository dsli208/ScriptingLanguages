use strict;
use warnings;

my %groups = ();

open(my $input_file, "<", "passwd.txt") or die("Cannot open file.");
while(my $line = <$input_file>) {
    my @table_row = split(":", $line);
    my $group = @table_row[3];

    if (exists $groups{$group}) {
      $groups{$group} = $groups{$group} + 1;
    }
    else {
      $groups{$group} = 1;
    }
}

my @keys = keys %groups;
my @values = values %groups;

while (my ($key, $value) = each %groups) {
  print "group $key has $value users\n";
}

close($input_file);
