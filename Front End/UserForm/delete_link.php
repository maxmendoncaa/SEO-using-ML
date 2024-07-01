<?php
$link_id = $_POST['competitor-links'];
$file_contents = file_get_contents('pagespeed.txt');
$file_contents = str_replace("$link_id
", '', $file_contents);
file_put_contents('pagespeed.txt', $file_contents);
?>
