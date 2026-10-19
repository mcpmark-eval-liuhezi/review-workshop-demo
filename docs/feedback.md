# Reviewer Checklist

Three questions to ask yourself before approving a pull request:

1. **Does the change do what the PR says it does?** Read the title and description, then walk the diff and confirm the code actually matches the stated intent.

2. **What could break?** Look for edge cases, missing error handling, and paths that are not covered by tests.

3. **Would the next reader understand this?** Check naming, comments, and docs — if you have to re-read a hunk three times, leave a comment.

Happy reviewing!
