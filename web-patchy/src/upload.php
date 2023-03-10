<?php

// Check if a zip file was uploaded
if(isset($_FILES['zipfile'])) {

    // Get the uploaded file details
    $file_name = $_FILES['zipfile']['name'];
    $file_size = $_FILES['zipfile']['size'];
    $file_tmp = $_FILES['zipfile']['tmp_name'];
    $file_type = $_FILES['zipfile']['type'];
    $file_error = $_FILES['zipfile']['error'];

    // Check if there were any errors with the upload
    if($file_error === 0) {

        // Create a directory for the extracted files
        $target_dir = "uploads/";
        if(!is_dir($target_dir)){
            mkdir($target_dir, 0777, true);
        }

        // Move the uploaded file to the target directory
        move_uploaded_file($file_tmp, $target_dir.$file_name);

        // Open the uploaded zip file
        $zip = new ZipArchive;
        $zip->open($target_dir.$file_name);

        // Extract the files to the uploads directory
        $zip->extractTo($target_dir);

        // Close the zip archive
        $zip->close();

        echo "File uploaded and extracted successfully!";
    }
    else {
        echo "Error uploading file. Error code: " . $file_error;
    }
}

?>

