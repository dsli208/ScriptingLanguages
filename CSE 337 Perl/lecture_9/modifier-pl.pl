use strict;
use warnings;

my $default = 9;

# $a DECLARED AND DEFINED
my $a=10;

# $b AND $c DECLARED BUT NOT DEFINED
my ($b, $c);

# USE OF UNLESS MODIFIER
$a = $default unless defined $a;   # $a intact at 10
$b = $default unless defined $b;   # $b = 9 
$c = $default unless defined $c;   # $b = 9
print "$a $b $c\n\n";


my $balance = 2000;
my $deposit = 1000;
my $withdrawal = 800;
 
# AFTER RE_ORDERING, CAN SAVE TYPING OF BRACES. 
# ALSO CAN OMIT THE PARENTHESES IN IF STATEMENT
$balance += $deposit
   if $deposit;

# PARANTHESES IN THE IF STATEMENT CAN BE OMITTED 
$balance -= $withdrawal
   if $withdrawal and $withdrawal <= $balance;
print "balance is $balance\n";
