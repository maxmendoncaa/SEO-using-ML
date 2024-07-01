<?php
$file = 'pagespeed.txt';

if (file_exists($file)) {
    unlink($file);
    echo "File $file deleted successfully";
} else {
    echo "File $file does not exist";
}
?>
