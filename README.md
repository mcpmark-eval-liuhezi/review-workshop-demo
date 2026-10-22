# review-workshop-demo

This is a **demo repository** for our internal **code review workshop** for new hires.

It exists purely as a live sandbox so we can walk through the GitHub pull request and code review workflow together — branching, opening a PR, requesting reviews, leaving review comments, and submitting them.

Feel free to click around: nothing here is production code. 🙂

## The `utils` module

This PR adds `utils.py` at the repo root — a small set of everyday helpers. `slugify(text)` turns a heading into a URL-friendly slug, `word_count(text)` counts the words in a string, and `clamp(value, low, high)` pins a number inside a range. It is deliberately simple: the point of the workshop is to practice reading a diff and writing good review comments, not to admire the code.
