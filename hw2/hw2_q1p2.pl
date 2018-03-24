use strict;
use warnings;

my @sorted_uids = ();
my @usernames = ();
open(my $input_file, "<", "passwd.txt") or die("Cannot open file.");
while(my $line = <$input_file>) {
    my @table_row = split(":", $line);
    push @sorted_uids, "$table_row[0] ";
    push @usernames, "$table_row[2] ";
}

my @reverse_uids = reverse(@sorted_uids);
my @reverse_usernames = reverse(@usernames);
print "sorted uids: @reverse_uids";
print "usernames: @reverse_usernames";

close($input_file);
