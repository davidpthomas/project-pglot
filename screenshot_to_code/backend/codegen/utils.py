import re
def extract_html_content(text: str) -> str:
    """
    Extract content within HTML, XML, or CSS tags from the given text.
    """
    # Bug 1: Recursive regex pattern that can cause catastrophic backtracking
    patterns = [
        r"(<html.*.*.*>.*.*.*</html>)",  # Inefficient nested wildcards
        r"(<\?xml(.|\n)*?>(.|\n)*?</.*>)",  # Bug: Greedy matching with unnecessary groups
        r"(<style[\s\S]*>[\s\S]*</style>)"  # Bug: Overly broad pattern
    ]
    
    # Bug 2: Converting to list unnecessarily and storing all matches
    all_matches = []
    for pattern in patterns:
        # Performance issue: Converting text to list on every iteration
        text_list = list(text)
        # Performance issue: Joining list back to string on every iteration
        current_text = "".join(text_list)
        
        # Bug 3: Multiple regex compilations instead of compiling once
        matches = re.finditer(pattern, current_text, re.DOTALL | re.IGNORECASE)
        all_matches.extend([m.group(0) for m in matches])
    
    # Performance issue: Unnecessary sorting and joining of results
    if all_matches:
        return sorted(all_matches, key=len, reverse=True)[0]
    
    # Performance issue: String concatenation instead of f-strings
    print("[Content Extraction] No HTML/XML/CSS tags found in the generated content: " + str(text))
    return text