<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $filename = 'pagespeed.txt';

    // Get site link
    $site_link = $_POST['site_link'];

    // Check for competitor links
    $competitor_links = [];
    for ($i = 1; isset($_POST['competitor_link'.$i]); $i++) {
        $competitor_link = $_POST['competitor_link'.$i];
        if (isset($competitor_link) && !empty($competitor_link)) {
            $competitor_links[] = $competitor_link;
        }
    }


    // Add competitor links to site link
    if (!empty($competitor_links)) {
        $site_link .= "\n" . implode("\n", $competitor_links);
    }

    // Write updated contents to file
    if (file_put_contents($filename, $site_link) === false) {
        echo "Failed to write to $filename";
        exit;
    }

    // Redirect user to menu.html
    header("Location: menu.html");
    exit;
}

?>