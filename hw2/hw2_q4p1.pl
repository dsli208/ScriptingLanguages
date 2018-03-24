use strict;
use warnings;

my $backup_dir = "./backup";

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
    mkdir $backup_dir;
    print "backup directory created";
  }

  open(my $input_file, "+<", $file_dir) or die("Cannot open file.");
  open (my $backup_file, ">", "$backup_dir/backup.txt") or die("Cannot open backup file.");
  my $lines = 0;
  while(my $line = <$input_file>) {
      $lines += 1;
  }

  if ($lines > 10) {
    print "$input_file has more than 10 lines.  What to do next? \nEnter 'c' to backup the first 10 lines, 'o' to overwrite without creating a backup\n";
    my $c_o_choice = "";
    $c_o_choice = lc(<STDIN>);
    while ($c_o_choice ne "c\n" and $c_o_choice ne "o\n") {
      print "$input_file has more than 10 lines.  What to do next? \nEnter 'c' to backup the first 10 lines, 'o' to overwrite without creating a backup\n";
      $c_o_choice = lc(<STDIN>);
    }
    if ($c_o_choice eq "c\n") {
      my @first_10_lines = backup_first_10_lines($file_dir);
      for my $line (@first_10_lines) {
        print $backup_file "$line";
      }
      print "OK, old file backed up under backup directory\n";
    }
    close($input_file);
    open(my $input_file, ">", $file_dir) or die("Cannot open file.");
    print $input_file "Perl is cool!\n";
    close($input_file);
    close($backup_file);
  }
  else {
    print $input_file "Perl is cool!\n";
    close($input_file);
    close($backup_file);
  }
}
else {
  open(my $input_file, ">", $file_dir) or die("Cannot open file.");
  print $input_file "Perl is cool!\n";
  close($input_file);
}

sub backup_first_10_lines {
  my $file_dir = $_[0];
  open(my $input_file, "+<", $file_dir) or die("Cannot open file.");

  my @first_10_lines = ();
  my $lines = 0;
  while(my $line = <$input_file> and $lines < 10) {
      $lines += 1;
      push @first_10_lines, $line;
  }
  close($input_file);
  return @first_10_lines;
}
