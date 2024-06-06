<?php
$initial = '555';
// convert to decimal from octal
$a = octdec($initial);
echo $a;
echo "\n";

// Convert to radians from degrees
$b = deg2rad($a);
echo $b;
echo "\n";

// Take the cosine of b
$c = cos($b);
echo $c;
echo "\n";

// Round c to 3 decimal places
$d = round($c, 3);
echo $d;
echo "\n";

// Take the natural log of d
$e = log($d);
echo $e;
echo "\n";

// Take the absolute value of e
$f = abs($e);
echo $f;
echo "\n";

// Take the inverse cosine of f
$g = acos($f);
echo $g;
echo "\n";

// Convert g to degrees
$h = rad2deg($g);
echo $h;
echo "\n";

// Round h down to the nearest integer
$i = floor($h);
echo $i;
echo "\n";

// Subtract 47
$j = $i - 47;
echo $j;
echo "\n";

