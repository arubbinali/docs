#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10

// Function to generate random numbers in an array
void generateRandomNumbers(int *arr, int size) {
    srand(time(0)); // Seed random number generator
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 100; // Random number between 0 and 99
    }
}

// Function to display the array
void displayArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to find the largest number in an array
int findMax(int *arr, int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

// Function to swap two numbers using pointers
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to sort an array using Bubble Sort
void bubbleSort(int *arr, int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

// Recursive function to find the factorial of a number
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// Function to reverse a string
void reverseString(char *str) {
    int length = 0, i;
    char temp;
    
    while (str[length] != '\0') {
        length++;
    }
    
    for (i = 0; i < length / 2; i++) {
        temp = str[i];
        str[i] = str[length - i - 1];
        str[length - i - 1] = temp;
    }
}

// Function to check if a number is prime
int isPrime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i <= n / 2; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    // Array operations
    int arr[SIZE];
    generateRandomNumbers(arr, SIZE);
    
    printf("Original array: ");
    displayArray(arr, SIZE);
    
    int max = findMax(arr, SIZE);
    printf("Maximum value in array: %d\n", max);
    
    bubbleSort(arr, SIZE);
    printf("Sorted array: ");
    displayArray(arr, SIZE);

    // String operations
    char str[] = "Hello, World!";
    printf("Original string: %s\n", str);
    
    reverseString(str);
    printf("Reversed string: %s\n", str);
    
    // Factorial calculation
    int num = 5;
    printf("Factorial of %d is %d\n", num, factorial(num));
    
    // Prime number check
    int primeCheck = 29;
    if (isPrime(primeCheck)) {
        printf("%d is a prime number\n", primeCheck);
    } else {
        printf("%d is not a prime number\n", primeCheck);
    }

    // Pointer demo
    int a = 10, b = 20;
    printf("Before swap: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("After swap: a = %d, b = %d\n", a, b);
    
    return 0;
}
