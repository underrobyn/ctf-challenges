<?php

const DISALLOWED_FILES = array(
    'index.md',
    'contact.md'
);

function get_preview($file) {
    $file_contents = file_get_contents($file);
    $lines = explode("\n", $file_contents);
    $preview = '';

    foreach ($lines as $line) {
        // Ignore lines that start with a non-alphabetical character to prevent markdown stuff
        if (preg_match('/^[^a-zA-Z]/', $line)) {
            continue;
        }

        $preview .= $line;

        if (strlen($preview) >= 150) {
            break;
        }
    }

    return $preview . '...';
}

function generate_blog_previews($folder_path) {
    if ($handle = opendir($folder_path)) {
        while (false !== ($file = readdir($handle))) {
            // Ignore hidden files and directories
            if ($file[0] == '.') continue;

            // Ignore specific blog files
            if (in_array($file, DISALLOWED_FILES)) continue;

            // Read the first 120 characters of the file as a preview
            $file_contents = file_get_contents($folder_path . '/' . $file);
            $preview = get_preview($folder_path . '/' . $file);

            // Replace hyphens with spaces in the file name
            $file_name = str_replace('-', ' ', $file);
            $file_name = str_replace('.md', '', $file_name);

            // Generate the link to the read.php file
            $link = 'read.php?page=' . urlencode($file);

            // Generate the HTML output for this file
            echo '<div class="bg-white rounded shadow p-4">';
            echo '<h2 class="text-xl font-bold mb-2">' . $file_name . '</h2>';
            echo '<p class="text-gray-700">' . $preview . '</p>';
            echo '<a href="' . $link . '" class="block mt-4 text-blue-500 hover:text-blue-600">Read more</a>';
            echo '</div>';
        }

        closedir($handle);
    }
}

?>
<!DOCTYPE HTML>
<html lang="en">
    <head>
        <title>Blog Reader 1.0</title>
        <?php include('includes/head.php'); ?>
    </head>
    <body>
        <?php include('includes/nav.php'); ?>
        <main class="container mx-auto px-4 py-8">
            <h1 class="text-2xl font-bold mb-4">Welcome to my blog</h1>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <?php generate_blog_previews('blog'); ?>
            </div>
        </main>
    </body>
</html>
