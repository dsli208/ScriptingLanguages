use strict;
use warnings;

# INITIALIZE A HASH
my %sounds = (cow   => "moooo",
              duck  => "quack",
              horse => "whinny",
              sheep => "baa",
              hen   => "cluck",
              pig   => "oink");


# HASH SLICING
my @barnyard_sounds = @sounds{"horse", "hen", "pig"};
print "I heard the following in the barnyard: @barnyard_sounds\n";


# GET HASH KEYS AND VALUES. NOTE THE "s" IN VARIABLE NAMES
# Note we go back to the whole hash here
my @animals = keys %sounds;
my @noises = values %sounds;
print "\n@animals";
print "\n@noises\n\n";


# ITERATING A HASH USING EACH. USE DIFFERENT VARIABLES FROM ABOVE
while (my ($animal, $noise) = each %sounds) {
    print "Old MacDonald had a $animal.";
    print "\tWith a $noise! $noise! here...\n";
}
