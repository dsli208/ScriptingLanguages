use strict;
use warnings;

my $dir = "./test_dir/";
mkdir $dir;

open (my $backup_file, ">", "$dir/backup.txt") or die("Cannot open backup file.");
close($backup_file);
