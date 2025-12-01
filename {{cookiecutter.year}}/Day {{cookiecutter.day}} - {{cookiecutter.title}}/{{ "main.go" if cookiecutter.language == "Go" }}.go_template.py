// Advent of Code {{ cookiecutter.year }} - {{ cookiecutter.project_slug }}

package main

import (
    "time"
	"fmt"
	"os"
	"strings"
)

// Execute and time a function call.
func timeAndPrint(label string, fn func()) {
    fmt.Printf("--- %s ---\n", label)
    start := time.Now()
    
    fn() 
    
    elapsed := time.Since(start)
    fmt.Printf("Elapsed Time: %s\n\n", elapsed)
}


func readInputFile(filename string) ([]string, error) {
	content, err := os.ReadFile(filename)
	if err != nil {
		return nil, fmt.Errorf("failed to read input file: %w", err)
	}

	// Split the content into lines, trimming any trailing whitespace (like a final newline)
	inputData := strings.Split(strings.TrimSpace(string(content)), "\n")
	return inputData, nil
}


func parseInput([]string) ([]string, error) {
    // data wrangling logic
    return data, nil
}


func solvePartOne(data []string) int {

    return 0
}


func solvePartTwo(data []string int {

    return 0
}


func main() {

    // --- EXAMPLE TEST SETUP ---
    exampleInputRaw := `
`
    exampleOutputOne := 0
    exampleOutputTwo := 0

    // Run and print example tests
	fmt.Println("--- Example Test ---")
    fmt.Printf("Example Part 1 Answer: %d, Expected: %d\n", solvePartOne(exampleData), exampleOutputOne)
	fmt.Printf("Example Part 2 Answer: %d, Expected: %d\n\n", solvePartTwo(exampleData), exampleOutputTwo)

    // --- LIVE SOLUTION ---
    content, err := os.ReadFile("input.txt")

    if err != nil {
        fmt.Println("Error reading input file:", err)
        return
    }

    inputData, err := parseInput(content)

    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
    
    // Print solutions
    timeAndPrint("\nPart 1:\n", func() {
        solvePartOne(inputData)
    })
    
    timeAndPrint("\nPart 2:\n", func() {
        solvePartTwo(inputData)
    })
}