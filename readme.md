# Whiteboard Wednesday - Sum of Squares

## Please Read!

Your mission is to solve a problem we'll describe below.

But your _real_ mission is to prepare to help someone else solve it.

## Help Someone Else Solve It?!

Tomorrow you'll be interviewing someone, helping them through the process of solving this problem. So as you solve this, think through your process. You'll be able to use that to, with the benefit of hindsight, guide your partner through that same process.

Also... that same person will interview you too!

## Things To Think About As You Do This

- As an interviewer, you'll have to think about how YOU solved the problem.
- Remember that you won't be solving the problem for them, but helping guide them there.
- Think about what helped get you unstuck on this problem. They may get stuck in the same places!
- This will be an amazing learning experience for YOU, as a teacher--you'll need to understand the problem enough to help someone though it.
- Don't forget that tomorrow you can give _them_ the advice below!

## When you're getting interviewed tomorrow

- Talk through the problem - it's about the process, not the solution
- Don't give up
- Ask about edge cases - 0 and negative numbers and empty strings and multiple words and all that!
- Solve the problem, don't build the app
  - Don't sweat syntax
  - Pseudocode
  - Invent helper functions if necessary... you don't need to actually _write_ those functions! Just imagine a function to, say, check if a string is in another string, use it, and if you ever code it FOR REAL you could always write it then.

## The Problem You'll Be Doing Tonight (And Interviewing Someone On Tomorrow!)

Create a function that squares every number passed into it and then sums those squares together.

For example, for `[1, 2, 2]` it should return `9`, because `1^2` + `2^2` + `2^2` = `9`.

## Hints

- Don't forget that we're adding up all the squares, NOT squaring the sum. For the above example, your result should NOT be `25` (the square of the sum of `1`, `2`, and `2`).
- There are some ways to do this using python list comprehensions, but a plain ol' `for` loop should do you fine!
