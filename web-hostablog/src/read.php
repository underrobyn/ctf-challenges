<?php

$page = 'index.md';
if (!empty($_GET['page'])) {
	$page = $_GET['page'];
}

$path = 'blog' . DIRECTORY_SEPARATOR . $page;

if (!file_exists($path)) {
	http_response_code(404);
	die();
}

$fc = file_get_contents($path);

// Replace hyphens with spaces in the file name
$file_name = str_replace('-', ' ', $path);
$file_name = str_replace('.md', '', $file_name);

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
			<h1 class="text-2xl font-bold mb-4"><?php echo $file_name; ?></h1>
			<pre id="content">Loading...</pre>
		</main>

		<?php include('includes/footer.php'); ?>
		<script defer>
			console.log("No clues here, hehe, maybe look at the pages")

			document.getElementById('content').innerHTML =
				marked.parse(`<?php echo $fc; ?>`);
		</script>
	</body>
</html>
