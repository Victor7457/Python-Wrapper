% Read the output variable from the file
output_variableOriginal = fileread('input.txt');
output_variableC = fileread('c_output.txt');
output_variableHS = fileread('haskell_output.txt');
output_variableProlog = fileread("prolog_output.txt");

% convert the string to a numeric array
% convert the numeric array to unsigned char
output_arrayOriginal = uint8(str2num(output_variableOriginal));
output_arrayC = uint8(str2num(output_variableC));
output_arrayHS = uint8(str2num(output_variableHS));
output_arrayProlog = uint8(str2num(output_variableProlog));

% Resize to a original size (adjust based on your data format)
resized_matrixOriginal = reshape(output_arrayOriginal, 75, 75);
resized_matrixC = reshape(output_arrayC, 75, 75);
resized_matrixHS = reshape(output_arrayHS, 75, 75);
resized_matrixProlog = reshape(output_arrayProlog, 75, 75);

% Create a single figure with subplots
figure;

% Display the resized image Original
subplot(2, 2, 1);
imshow(resized_matrixOriginal);
title('Original Image of Mickey');

% Display the resized image C
subplot(2, 2, 2);
imshow(resized_matrixC);
title('Black & White Image from C');

% Display the resized image Haskell
subplot(2, 2, 3);
imshow(resized_matrixHS);
title('Inverted Color Image from Haskell');

% Display the resized image Prolog
subplot(2, 2, 4);
imshow(resized_matrixProlog);
title('Rotated Image from Prolog');