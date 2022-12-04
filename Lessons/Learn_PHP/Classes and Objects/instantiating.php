<?php
class Beverage {
  public $temperature, $color, $opacity;
}

$tea = new Beverage("cold", "brown", "opaque");
$tea->temperature = "cold";
$tea->color = "brown";
$tea->opacity = "opaque";

echo $tea->temperature;

// \n is a newline character
echo "\n";
echo "\n";


$coffee = new Beverage("hot", "black", "opaque");
$coffee->temperature = "hot";
$coffee->color = "black";
$coffee->opacity = "opaque";

echo $coffee->temperature;
