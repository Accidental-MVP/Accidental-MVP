from datetime import datetime
import random

# Simulated data (you can make this real later)
languages = ["Python", "JavaScript", "Java", "TypeScript", "C++"]
moods = [
    "unhinged but productive",
    "aggressively calm",
    "debugging myself",
    "softly melting",
    "dangerously caffeinated"
]

# Fake log block
block = f"""```
[diagnostic.log]
> repo_count: 17
> primary_language: {random.choice(languages)}
> last_push: remember-through-me ({random.randint(1, 5)} days ago)
> commit_streak: ACTIVE ({random.randint(3, 14)} days)
> mood_estimate: \"{random.choice(moods)}\"

[threat assessment]
> suspicious activity detected in loopinator.js
> file count exceeds sanity threshold
```"""

# Read your README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Define the cursed block to replace
start_tag = "<!-- START:CURSED_METRICS -->"
end_tag = "<!-- END:CURSED_METRICS -->"

start = content.find(start_tag) + len(start_tag)
end = content.find(end_tag)

# New README with cursed logs
new_readme = content[:start] + "\n" + block + "\n" + content[end:]

# Save it
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

print("✅ Cursed metrics updated.")
