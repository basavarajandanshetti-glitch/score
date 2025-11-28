import sys

# If valid numbers are provided via command line, use them
scores = []
if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))

# If no scores are provided, use default values
if not scores:
    print("No valid scores provided, using default.")
    scores = [70, 80, 90]

# Calculate sum, average, max, min
total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Total score:", total)
print("Average score:", average)
print("Maximum score:", maximum)
print("Minimum score:", minimum)
