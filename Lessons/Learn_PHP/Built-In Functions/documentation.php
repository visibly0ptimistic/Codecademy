<?php
namespace Codecademy;

$a = 29;
$b = "You did it!";
$c = STR_PAD_BOTH;
$d = "*~*";

// Write your code below:
echo str_pad($b, $a, $d, $c);

/*
https://www.php.net/manual/en/function.str-pad.php

str_pad — Pad a string to a certain length with another string

Description ¶
This function returns the string string padded on the left, the right, or both sides to the specified padding length. If the optional argument pad_string is not supplied, the string is padded with spaces, otherwise it is padded with characters from pad_string up to the limit.
*/