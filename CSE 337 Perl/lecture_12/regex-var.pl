$string = "The food is in the salad bar"; 
$string =~ m/foo/;
print "Before: '$`'\n";
print "Matched: '$&'\n";
print "After: '$''\n";
