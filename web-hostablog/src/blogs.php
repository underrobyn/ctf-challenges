<?php

$pages_in_my_blog = glob('blog' . DIRECTORY_SEPARATOR . '*');
$link_template = '<a href="{URL}" title="Page on my blog">Read {URL}</a><br />';

$fc = '';
foreach ($pages_in_my_blog as $item) {
    $fc .= str_replace($link_template, '{URL}', $item);
}

?>
<!DOCTYPE HTML>
<html lang="en">
    <head>
        <title>Blog Reader 1.0</title>
    </head>
    <body>
        <pre id="content"></pre>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.3.0/marked.min.js"
                integrity="sha512-zAs8dHhwlTbfcVGRX1x0EZAH/L99NjAFzX6muwOcOJc7dbGFNaW4O7b9QOyCMRYBNjO+E0Kx6yLDsiPQhhWm7g=="
                crossorigin="anonymous"
                referrerpolicy="no-referrer"></script>

        <?php echo $fc; ?>
        <script defer>
            console.log("No clues here, hehe, maybe look at the pages")

            document.getElementById('content').innerHTML =
                marked.parse(`<?php echo $fc; ?>`);
        </script>
    </body>
</html>
