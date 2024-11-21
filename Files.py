import 'dart:io';

void main() async {
  // File paths (change these paths as needed)
  String inputFilePath = 'input.txt';  // The input file
  String outputFilePath = 'output.txt';  // The output file

  try {
    // Reading the content of the input file
    File inputFile = File(inputFilePath);
    String content = await inputFile.readAsString();

    // Modify the content (for demonstration, we convert the content to uppercase)
    String modifiedContent = content.toUpperCase();

    // Writing the modified content to the output file
    File outputFile = File(outputFilePath);
    await outputFile.writeAsString(modifiedContent);

    print('File has been successfully modified and saved to $outputFilePath');
  } catch (e) {
    // Handle any errors (file not found, permission denied, etc.)
    print('An error occurred: $e');
  }
}


// Error Handling Lab

import 'dart:io';

void main() async {
  // Prompt user to enter the filename
  print('Please enter the filename to read:');
  String fileName = stdin.readLineSync()!;

  try {
    // Attempt to open and read the file
    File file = File(fileName);
    String content = await file.readAsString();

    // Display the content of the file
    print('File content:\n$content');
  } catch (e) {
    // Handle different errors
    if (e is FileSystemException) {
      print('Error: The file "$fileName" could not be found or opened.');
    } else {
      print('An unexpected error occurred: $e');
    }
  }
}
