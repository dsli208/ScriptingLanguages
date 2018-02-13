my @fruits = qw(apples bananas cherries oranges);
my @yummy = @fruits[1,3]; # [bananas oranges]
print "My favorite fruits are: @yummy\n";
my @berries = @fruits[2]; # [cherries]
push @berries, "cranberries"; # [cherries cranberries]
print "These fruits are berries: @berries\n";
