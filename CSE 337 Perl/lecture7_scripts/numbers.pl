# Accept a number from the user print "maximum: ";
$maximum = <STDIN>;
# Make an array of numbers @numbers = (2..$maximum);
# Iterate through that array
while ($prime = shift @numbers) {
print $prime; # Print the next prime # Remove multiples of that prime 
@numbers = grep {$_ % $prime} @numbers;
}
print "\n";
