=pod
 David S. Li
 110328771
 CSE 337 HW#2
=cut

use strict;
use warnings;

sub addUser {
  my $input_dir = $_[0];
  my $username = $_[1];
  my $name = $_[2];
  my $dir = $_[3];
  my $shell = $_[4];
  open(my $input_file, "+<", $input_dir) or die("Cannot open file.");

  # Getting hash table of group ideas, and finding the max id with each iteration
  my %groups = ();
  my $max_user_id = -100;

  while(my $line = <$input_file>) {

      my @table_row = split(":", $line);
      my $user_id = $table_row[2];
      my $group = $table_row[3];

      if ($user_id > $max_user_id) {
        $max_user_id = $user_id;
      }

      if (exists $groups{$group}) {
        $groups{$group} = $groups{$group} + 1;
      }
      else {
        $groups{$group} = 1;
      }
  }

  my $group_id = $groups{(keys %groups)[int(rand(keys %groups))]}; # FIGURE OUT HOW TO ASSIGN A RANDOM ONE
  $max_user_id += 1;
  my $new_user = "$username:$max_user_id:$group_id:$name:$dir:$shell\n";

  print $input_file "$new_user";

  close($input_file);
}

addUser("passwd.txt", "David S. Li", "DSLIGROUP", "/var/dsli", "/usr/bin/dsli/");
