## ChickenAndEgg

#### About

A friend of mine had an idea: after asking, "Which came first the chicken or the
egg," the next natural step is to say, "Which came first, 'Which came first, the
chicken or the egg?' or 'Which came first, the egg or the chicken?' " He then
challeged me to solve for the general case: given a number, output the 
chicken-and-egg question with the corresponding nesting.

My initial solution is a simple recursive python program. In the future, I
hope to add more solutions in different programming languages. Perhaps I will
also figure out how to solve the problem in an iterative way.

--------------------------------------------------------------------------------

#### Sample Session

```
$ ./repl

Enter q to quit

Chicken And Egg
Deapth: 3

Which came first, "Which came first, 'Which came first, the chicken or the egg?' or 'Which came first, the egg or the chicken?'" or "Which came first, 'Which came first, the egg or the chicken?' or 'Which came first, the chicken or the egg?'"

Chicken And Egg
Deapth: 5

Which came first, "Which came first, 'Which came first, "Which came first, 'Which came first, the chicken or the egg?' or 'Which came first, the egg or the chicken?'" or "Which came first, 'Which came first, the egg or the chicken?' or 'Which came first, the chicken or the egg?'"' or 'Which came first, "Which came first, 'Which came first, the egg or the chicken?' or 'Which came first, the chicken or the egg?'" or "Which came first, 'Which came first, the chicken or the egg?' or 'Which came first, the egg or the chicken?'"'" or "Which came first, 'Which came first, "Which came first, 'Which came first, the egg or the chicken?' or 'Which came first, the chicken or the egg?'" or "Which came first, 'Which came first, the chicken or the egg?' or 'Which came first, the egg or the chicken?'"' or 'Which came first, "Which came first, 'Which came first, the chicken or the egg?' or 'Which came first, the egg or the chicken?'" or "Which came first, 'Which came first, the egg or the chicken?' or 'Which came first, the chicken or the egg?'"'"

Chicken And Egg
Deapth: q
Goodbye
```
