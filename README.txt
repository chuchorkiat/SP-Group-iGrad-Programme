SP Group's iGrad Programme
Pre-assessment Assignment
Candidate: Chu Chor Kiat


Please follow the following steps to execute the program:
1. Open run_program.py
2. Execute run_program.py
3. Select question to solve (1 or 2)
4. Enter the necessary parameters when prompted
5. An output will be given


The test questions are as follow:
## Test

On a Keypad, numbers and alphabets are placed on the same key. This is shown below:

| 1        	  | 2 (abc) 	  | 3 (def)  	   |
|-------------|-------------|--------------|
| **4 (ghi)** | **5 (jkl)** | **6 (mno)**  |
| **7 (pqrs)**| **8 (tuv)** | **9 (wxyz)** |
|          	  | **0**       |          	   |

Let's see how it works:

Key `2` contains `ABC` and if we want to type anything starting with `A` we need to press Key `2` once. 

If we want to type `B`, then we'll press Key `2` twice, and to type `C`, then we'll press Key `2` thrice.

### Your Task

Please write a program to solve the problem set below. 

Please include sufficient documentation (including "How to Run the Program") and explain your technical choices.

#### Traversing the Keypad

When you move along the Keypad, you are ONLY allowed to move up, down, left and right from the current Key, or stay on the current Key.

You are NOT allowed to move diagonally.

Example: You are on Key `2`. The next Keys that you can move to are `1`, `3`, and `5`, or remain at `2`.

#### Problem Set

##### Question 1

Given a starting digit and a word length, return all possible word combinations.

Sample: 

```
Starting Digit: 2
Word Length: 2
Output: ["aa" "ab", "ac", "ad", "ae", "af", "aj", "ak", "al", "ba", "bb", "bc", "bd", "be" "bf", "bj", "bk", "bl", "ca", "cb", "cc", "cd", "ce", "cf", "cj", "ck", "cl"] 

```

##### Question 2

Given a digit, the position of the digit in a word and a word length(Max: 5), return all possible word combinations.

This means the letter representations of a digit (i.e. `A`, `B` or `C`  for Key `2`) is constrained to the specified position within a word.

Suppose the specified position of the digit is `3`, then `A`, `B` or `C` can only appear as the 3rd letter within a word, i.e. GKA, GKB, GKC.

Sample:

```
Digit: 2
Position: 2
Word Length: 2
Output: ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc", "da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc", "ja", "jb", "jc", "ka", "kb, "kc", "la", "lb", "lc"]
```

### Evaluation

We'll be looking at the following:

1. Correctness
2. Code Quality
3. Performance
4. Documentation

### Constraints

#### Time

Please timebox yourself to a maximum of 4 hours for this activity.

#### Technology

You are required to use any of these languages: [Go](https://golang.org/), [Ruby](https://www.ruby-lang.org/en/), JavaScript, Java, PHP or Python.

You are allowed to use any frameworks for the language you chose.

#### Testing

Please approach this exercise as you would in your development workflow.

If you write tests in your daily work, we would love to see them in this exercise too.

#### Git and Commit History

Sync your app to BitBucket as a PRIVATE repo and allow access to `winstonyw`.

Please maintain a descriptive and clear Git commit history as it would allow us to better understand your thought process.

### Follow Up

In the event that you are selected for the next round of interview (onsite chat), please be expected to discuss your work further with us.

Looking forward to seeing your code!
