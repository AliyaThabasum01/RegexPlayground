# 🔍 Regex Playground

A lightweight Python CLI tool to test regular expressions instantly.

## Features

- Test any regex pattern
- Find all matches
- Handles invalid regex gracefully
- Uses Python's built-in `re` module

## Run

```bash
python main.py
```

### Example

Input:

```
Text: contact me at test@gmail.com
Pattern: \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b
```

Output:

```
1. test@gmail.com
```
