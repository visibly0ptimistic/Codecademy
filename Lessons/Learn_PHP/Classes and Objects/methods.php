<?php
class Beverage {
  public $temperature, $color, $opacity;
  function getInfo() {
    return "This beverage is $this->temperature and $this->color.";
  }
}

$soda = new Beverage("cold", "orange", "opaque");
$soda->color = "orange";
$soda->temperature = "cold";
echo $soda->getInfo();