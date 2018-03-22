my @fruits; # Undefined
@fruits = qw(apples bananas cherries); # Assigned 
@fruits = (@fruits, "dates"); # Lengthen
@fruits = ();
# Empty
unshift @fruits, "acorn";
my $nut = shift @fruits;
print "Well, a squirrel would think an $nut was a fruit.\n";
push @fruits, "mango"; # Add an item to the end my 
$food = pop @fruits; # Remove from the end 
print "My, that was a yummy $food!\n";
