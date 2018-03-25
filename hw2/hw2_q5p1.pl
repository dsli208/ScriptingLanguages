use strict;
use warnings;

my $very = "very"; my $cat = "cat";
my $regex1 = m/$very+ $cat/;


my $no_match1 = "cat";
my $no_match2;
my $no_match3;
my $no_match4;
my $no_match5;

# MATCH CASES
print "1: $string\n" if "$string" =~ regex1;
