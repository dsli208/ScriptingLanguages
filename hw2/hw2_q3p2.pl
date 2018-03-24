use strict;
use warnings;

# CURRENCY CONVERSIONS
#$EUR = 0.81; $CAD = 1.29; $INR= 65.2; $JPY = 105.75; $VND = 22750; $KRW = 1079.43; $BTC = 0.000088;
our %currency_conversions = ("USD" => 1, "EUR" => 0.81, "CAD" => 1.29, "INR" => 65.2, "JPY" => 105.75, "VND" => 22750, "KRW" => 1079.43, "BTC" => 0.000088);

my $start_curr = "";
my $start_value = -2;

# START CURRENCY
print "Enter your start currency: ";
$start_curr = uc(<STDIN>);
$start_value = searchHash($start_curr);
while ($start_value < 0) {
  print "We do not trade $start_curr!\nReenter your start currency: ";
  $start_curr = uc(<STDIN>);
  $start_value = searchHash($start_curr);
}

# TARGET CURRENCY
my $target_curr = "";
my $target_value = -2;

print "Enter your target currency: ";
$target_curr = uc(<STDIN>);
$target_value = searchHash($target_curr);
print "$target_value\n";
while ($target_value < 0) {
  print "We do not trade $target_curr!\nReenter your start currency: ";
  $target_curr = uc(<STDIN>);
  $target_value = searchHash($target_curr);
}

# DO CONVERSIONS
print "Enter the amount: ";
my $amount = <STDIN>;

# target amount = (start amount * target curr value) / start curr value
my $converted_amount = ($amount * $target_value) / $start_value;
print "$amount $start_curr is $converted_amount $target_curr\n";

sub searchHash {
  my $currency = $_[0];
  chomp($currency);
  while ((my ($currency_type, $value)) = each(%currency_conversions)) {
    if ($currency eq $currency_type) {
      return $value;
    }
  }
  return -1;
}
