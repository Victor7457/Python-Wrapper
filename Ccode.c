#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Variable declarations
    // const int arraySize = 1000;
    const int arraySize = 80000;
    int *arrayPtr = (int *)malloc(arraySize * sizeof(int));
    int *convertedArray = (int *)malloc(arraySize * sizeof(int));

    // Check if at least one argument is provided
    if (argc < 2) {
        printf("\nFile path not specified on command line!\n\n");
        exit(1);
    }

    // Open the input file for reading
    FILE *inputFile = fopen(argv[1], "r");
    if (inputFile == NULL) {
        printf("Error opening input file!\n");
        exit(1);
    }

    // Read values from the input file and convert them
    int value;
    int index = 0;
    while (fscanf(inputFile, "%d", &value) == 1 && index < arraySize) {
        // Assign either 255 or 0 based on the condition
        convertedArray[index] = (value >= 170) ? 255 : 0;
        arrayPtr[index++] = value;
    }

    // Close the input file
    fclose(inputFile);

    // Open the output file for writing
    FILE *outputFile = fopen("c_output.txt", "w");
    if (outputFile == NULL) {
        printf("Error opening output file!\n");
        exit(1);
    }

    // Save the converted values to the output file
    for (int i = 0; i < index; i++) {
        fprintf(outputFile, "%d ", convertedArray[i]);
    }
    fprintf(outputFile, "\n");

    // Close the output file
    fclose(outputFile);

    // Free dynamically allocated memory
    free(arrayPtr);
    free(convertedArray);

    // End of program
    return 0;
}
