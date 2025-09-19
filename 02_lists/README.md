# List Concept Summary

This repository contains notes and practice problems related to Python lists, tuples, and iteration patterns.

## 1. Modifying, Adding, and Removing Elements
- How to update list elements.
- Removing all items sometimes requires using a loop.

## 2. Sorting Elements
- Sorting lists with `.sort()` and `sorted()`.
- Reverse order and custom key functions.

## 3. Iterating Through a List
- Using `for element in list`.
- Variations with tuples and strings.

## 4. Creating Numeric Lists with range()
- Generating sequences using `range(start, stop, step)`.
- Using `list(range(...))` to convert to a list.
- List comprehensions with conditions.

## 5. List Slicing
- Extracting sublists with `[start:end:step]`.
- Copies vs references: modifying a slice copy doesn’t affect the original, but direct assignment shares references.

## 6. List Operations
- Concatenation with `+`.
- Repetition with `*`.
- Nesting and shallow copies.

## 7. Tuples
- Immutable lists.
- Syntax differences and when to use them.

## 8. Various for Loop Patterns
- Iterating over lists, tuples, and strings.
- Emphasis on Python’s `for variable in iterable` structure.

---

## Practice Problems

- [01. Even Squares with List Comprehension](solutions/01_even_squares.py)  
  Generate squares of even numbers from 1 to 20 using a single list comprehension.

- [02. Multi-key Sorting (Length + Alphabetical)](solutions/02_multi_key_sort.py)  
  Sort words first by length and then alphabetically when lengths are the same.

- [03. Shallow Copy vs. Reference Sharing](solutions/03_shallow_vs_reference.py)  
  Compare shallow copy (`[:]`) with reference assignment in nested lists.

- [04. Word Frequency Counter (Dictionary)](solutions/04_word_frequency.py)  
  Count word occurrences in a sentence while ignoring case and punctuation.

- [05. Top-N Words by Frequency](solutions/05_top_n_words.py)  
  Find the top 3 most frequent words and sort ties alphabetically.

- [06. Flatten a Nested List](solutions/06_flatten_list.py)  
  Flatten a 2D list into a single list using list comprehension.

- [07. Sliding Window Sum](solutions/07_sliding_window_sum.py)  
  Compute sums of consecutive subarrays using a sliding window approach.

- [08. Multi-key Sorting (Name + Score)](solutions/08_name_score_sort.py)  
  Sort (name, score) pairs by name ascending and score descending.

- [09. Rotate a Matrix (90° Clockwise)](solutions/09_rotate_matrix.py)  
  Rotate a square matrix by 90 degrees clockwise.

- [10. Merge Overlapping Intervals](solutions/10_merge_intervals.py)  
  Merge overlapping ranges in a list of intervals.

- [11. Two-Sum Problem (O(n) Solution)](solutions/11_two_sum.py)  
  Solve the Two-Sum problem using a dictionary for O(n) time complexity.

- [12. Grouping by Key (e.g., Grade → Students)](solutions/12_group_by_grade.py)  
  Group elements into a dictionary by their keys.

- [13. Scoreboard Renderer (Formatted Table)](solutions/13_scoreboard_renderer.py)  
  Render a formatted scoreboard with totals and averages using f-strings.

- [14. Mini Log Analyzer (Frequency & Filtering)](solutions/14_log_analyzer.py)  
  Parse a log file to count levels, group by hour, and filter ERROR logs.

---

Refer to the text file in `datas/` for the original problem descriptions.