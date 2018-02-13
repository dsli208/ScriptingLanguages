#!/usr/bin/perl
use strict;
use warnings;
use 5.010;

my $a;
my $b;
my $c;

$a = 5;
$b = 10;
$c = $a + $b;
print $c;

my $apple_variety; # Value undefined
$apple_variety = "Red Delicious"; # Defined
$apple_vareity = "Granny Smith"; # Error
my $apple_color = "red"; # Declared and defined

my @fibonacci = (1, 1, 2, 3, 5, 8, 11);# Numbers
my @fruits = ("apples", "bananas", "cherries");
# Strings
my @grade_synonyms= (100,"A++","Perfect"); #Both

my @fruits = ("apples", "bananas", "cherries");
print "Fruit flies like $fruits[1].\n"; # bananas
print "Life is like a bowl of $fruits[$#fruits].\n"; # cherries
print "We need more $fruits[-3] to make the pie.\n"; #apples

my @prime_numbers = (2, 3, 5, 7, 11, 13); # Comma-separated
@composite_numbers = (4, 6, 8..10, 12, 14..16); # Numeric ranges
@fruits = ("apples", "bananas", "cherries");
@fruits = qw(apples bananas cherries);
@veggies = qw(radishes spinach);
@grocery_list = (@fruits, @veggies, "milk");
print "@grocery_list\n";

@fruits = qw(apples bananas cherries oranges);
my @yummy = @fruits[1,3];
print "My favorite fruits are: @yummy\n";
my @berries = @fruits[2];
push @berries, "cranberries";
print "These fruits are berries: @berries\n";
