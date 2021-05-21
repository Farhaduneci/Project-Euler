# Hello DEV

Project Euler is a series of challenging mathematical/computer programming problems that I like to start. I'm sure there will be a lot to learn for me, and I would like to share my solutions here in DEV.

❓ Here is problem 002:

> Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
>
> 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
>
> By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

💡 For solving this problem, we can use a combination of the Modulo operation and also Addition.

❗ The first solution you might think of when working with Fibonacci sequence or other similar concepts in programming is for sure,
the recursive approach. but we always need to remember that these functions may be called a thousand times and this simply means
you will face one of those `Maximum call stack size exceeded` like errors!

This happens because of 💀 the space complexity of these algorithms ([Have a 👀 at this article on this topic](https://syedtousifahmed.medium.com/fibonacci-iterative-vs-recursive)), so I use the Iterative approach instead here.

This is the formula for the Fibonacci sequence:

```
fib(n) = fib(n-1) + fib(n-2) → for n > 1
fib(n) = 1 → for n = 0, 1
```

we can suppose we have these variables:

```python
MAX = 4000000

first_number = 1
second_number = 1

sum = 0
```

then we calculate the answer by calculating every next term by its previous terms that we simply store in 2 different variables!
and then filtering out the even numbers and summing them all up.

💻 So, my solution in Python is:

```python
while second_number <= MAX:
    temp = second_number
    second_number += first_number
    first_number = temp

    if second_number % 2 == 0:
        sum += second_number
print(sum)
```

This might not be the best answer to this problem, but it only calculates 32 numbers (odd numbers also included) for this problem,
which is much better than the recursive approach. clearly if you be able to find a way not calculating the odd numbers at all! that
will be a perfect improvement, Can't wait to see if you have any ideas about this.

✅ The answer to this problem is **`4613732`**.

## **Thank You** ❤️

I wish my posts to be useful to anyone new to the world of programming or anybody curious 🧐!
If you find the content useful to you, please comment your thoughts, I would love to learn from you all.

Thank you for your loving directions.