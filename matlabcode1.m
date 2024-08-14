% read mickey-1 image greyscale image
%img = imread('C:/Users/Victor/Documents/420 Assignment 5/mickey-1.png');
img = imread('mickey-1.png');

% specify the target size
% targetSize = [256, 256];
targetSize = [75, 75];
% resize the image
img2 = imresize(img, targetSize);

% Reshape the image into a 1D array
img_1d = reshape(img2, 1, []); % was reading img not imag

% write the data to the file
dlmwrite('input.txt', img_1d, 'delimiter', ' ');

% currentDirectory = pwd;
% disp(['The current working directory is: ' currentDirectory]);
