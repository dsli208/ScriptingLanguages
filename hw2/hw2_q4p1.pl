use strict;
use warnings;

my $backup_dir = "./backup/backup.txt";

print "Enter file name: \n";
# INVALID FILE CASE?
my $file_dir = <STDIN>;
chomp($file_dir);

if (-e $file_dir) {
  print "$file_dir already exists.  Checking backup directory ... ";
  if (-e $backup_dir) {
    print "already exists";
  }
  else {
    mkdir($backup_dir);
    print "backup directory created";
  }

  open(my $input_file, "+<", $file_dir) or die("Cannot open file.");
  my $lines = 0;
  while(my $line = <$input_file>) {
      $lines += 1;
  }

  if ($lines > 10) {
    print "$input_file has more than 10 lines.  What to do next? \n Enter ’c’ to backup the first 10 lines, ’o’ to overwrite without creating a backup\n";
    my $c_o_choice = lc(<STDIN>);
    while ($c_o_choice ne "c" and $c_o_choice ne "o") {
      print "$input_file has more than 10 lines.  What to do next? \n Enter ’c’ to backup the first 10 lines, ’o’ to overwrite without creating a backup\n";
      $c_o_choice = lc(<STDIN>);
    }
    if (my $c_o_choice eq "c") {
      my @first_10_lines = backup_first_10_lines($input_file);
      for my $line (@first_10_lines) {
        print $backup_dir "$line\n";
      }
      print "OK, old file backed up under backup directory\n";
    }
    print $file_dir "Perl is cool!";
    close($input_file);
  }
  else {
    print $file_dir "Perl is cool!";
    close($input_file);
  }
}
else {
  open(my $input_file, "+<", $file_dir) or die("Cannot open file.");
  print $file_dir "Perl is cool!";
  close($input_file);
}

sub backup_first_10_lines {
  my $input_file = $_[0];
  my @first_10_lines = ();
  my $lines = 0;
  while(my $line = <$input_file> and $lines < 10) {
      $lines += 1;
      push @first_10_lines, $line;
  }
  return @first_10_lines;
}
