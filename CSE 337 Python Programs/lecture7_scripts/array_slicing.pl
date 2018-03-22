my @fruits = qw(apples bananas cherries oranges);
my @yummy = @fruits[1,3];
print "My favorite fruits are: @yummy\n";
my @berries = @fruits[2];
push @berries, "cranberries";
print "These fruits are berries: @berries\n";

