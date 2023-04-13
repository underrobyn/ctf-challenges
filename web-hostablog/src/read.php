<?php

$page = 'index.md';
if (!empty($_GET['page'])) {
	$page = $_GET['page'];
}

// TODO: FINISH LIST BLOG FUNCTIONALITY
if (!file_exists($page)) {
	http_response_code(404);
	die();
}

$fc = file_get_contents('blog' . DIRECTORY_SEPARATOR . $page);

?>
<!DOCTYPE HTML>
<html lang="en">
	<head>
		<title>Blog Reader 1.0</title>
		<?php include('includes/head.php'); ?>
	</head>
	<body>
		<header class="bg-white shadow">
			<div class="container mx-auto px-4">
				<nav class="flex justify-between items-center py-4">
					<div>
						<a href="/" class="font-bold text-gray-800">My Blog</a>
					</div>
					<div>
						<a href="#" class="px-4 py-2 text-gray-700 rounded hover:bg-gray-200">Home</a>
						<a href="#" class="px-4 py-2 text-gray-700 rounded hover:bg-gray-200">About</a>
						<a href="#" class="px-4 py-2 text-gray-700 rounded hover:bg-gray-200">Contact</a>
					</div>
				</nav>
			</div>
		</header>
		<main class="container mx-auto px-4 py-8">
			<h1 class="text-2xl font-bold mb-4">Welcome to my blog</h1>
			<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
				<div class="bg-white rounded shadow p-4">
					<h2 class="text-xl font-bold mb-2">Post title</h2>
					<p class="text-gray-700">Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit sint placeat, ipsam eos saepe quo animi ullam, tenetur perspiciatis mollitia corrupti in ea error labore nesciunt! Earum, dolores ad? Fugit.</p>
					<a href="#" class="block mt-4 text-blue-500 hover:text-blue-600">Read more</a>
				</div>
				<div class="bg-white rounded shadow p-4">
					<h2 class="text-xl font-bold mb-2">Post title</h2>
					<p class="text-gray-700">Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit sint placeat, ipsam eos saepe quo animi ullam, tenetur perspiciatis mollitia corrupti in ea error labore nesciunt! Earum, dolores ad? Fugit.</p>
					<a href="#" class="block mt-4 text-blue-500 hover:text-blue-600">Read more</a>
				</div>
				<div class="bg-white rounded shadow p-4">
					<h2 class="text-xl font-bold mb-2">Post title</h2>
					<p class="text-gray-700">Lorem ipsum dolor sit ametmollitia corrupti in ea error labore nesciunt! Earum, dolores ad? Fugit.</p>
					<a href="#" class="block mt-4 text-blue-500 hover:text-blue-600">Read more</a>
				</div>
				<div class="bg-white rounded shadow p-4">
					<h2 class="text-xl font-bold mb-2">Post title</h2>
					<p class="text-gray-700">Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit sint placeat, ipsam eos saepe quo animi ullam, tenetur perspiciatis mollitia corrupti in ea error labore nesciunt! Earum, dolores ad? Fugit.</p>
					<a href="#" class="block mt-4 text-blue-500 hover:text-blue-600">Read more</a>
				</div>
			</div>
		</main>
		<footer class="bg-white shadow">
			<div class="container mx-auto px-4 py-4 text-center">
				<p class="text-gray-700">© 2023 My Blog. All rights reserved.</p>
			</div>
		</footer>

        <pre id="content"></pre>

		<?php include('includes/footer.php'); ?>
		<script defer>
			console.log("No clues here, hehe, maybe look at the pages")

			document.getElementById('content').innerHTML =
				marked.parse(`<?php echo $fc; ?>`);
		</script>
	</body>
</html>
