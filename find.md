# Some useful find commands

## Search recursively with several keywords

`find . -type d \( -name "*sample*" -o -name "normed-scores" -o -name "scores" -o -name "biometric_references" \)`

## Find files smaller than bytes

`find . -type f -size -100c`
