from regex_tool import find_matches

print("=" * 40)
print("🔍 Regex Playground")
print("=" * 40)

text = input("Enter text: ")
pattern = input("Enter regex pattern: ")

matches = find_matches(pattern, text)

if matches:
    print("\nMatches:")
    for i, match in enumerate(matches, 1):
        print(f"{i}. {match}")
else:
    print("\nNo matches found.")
