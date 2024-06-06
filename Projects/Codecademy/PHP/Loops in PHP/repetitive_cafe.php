<?php
$drinks = [
    "Cafe au Lait" => 3.50,
    "Cappuccino" => 4.00,
    "Espresso" => 2.50,
    "Latte" => 3.75,
    "Macchiato" => 3.25,
    "Mocha" => 3.75,
    "Tea" => 2.50
];

$pastries = [
    "Croissant",
    "Danish",
    "Donut"
];
?>

<h1>Welcome to the Repetitive Cafe</h1>

<h3>Drinks!</h3>
<ul>
    <?php foreach ($drinks as $drink => $price) : ?>
        <li><?= $drink ?> - $<?= $price ?></li>
    <?php endforeach; ?>
</ul>

<h3>Pastries! ($2 each)</h3>
<ul>
    <?php foreach ($pastries as $pastry) : ?>
        <li><?= $pastry ?></li>
    <?php endforeach; ?>
</ul>
