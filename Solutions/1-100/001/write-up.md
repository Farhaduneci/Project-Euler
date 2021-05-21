# Hey folks

Project Euler is a series of challenging mathematical/computer programming problems that I like to start. I'm sure there will be a lot to learn for me, and I would like to share my solutions here in DEV.

❓ Here is problem 001:

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
> Find the sum of all the multiples of 3 or 5 below 1000.

💡 For solving this problem, we can simply use the Modulo operation and calculate the numbers which are multiples of 3 or 5.

> ❗ Modulo is a math operation that finds the remainder when one integer is divided by another. In writing, it is frequently abbreviated as a mod, or represented by the symbol %.
> For two integers a and b:
> a mod b = r
> Where a is the dividend, b is the divisor (or modulus), and r is the remainder.

Here is an example:

11 mod 4 = 3, because 11 divides by 4 (twice), with 3 remaining.

💻 So, my solution in Python is:

```python
sum = 0

for integer in range(1, 1000):
    if integer % 3 == 0 or integer % 5 == 0:
        sum += integer
print(sum)
```

✅ The answer to this problem is **`233168`**.

## **Thank You** ❤️

I wish my posts to be useful to anyone new to the world of programming or anybody curious 🧐!
If you find the content useful to you, please comment your thoughts, I would love to learn from you all.

Thank you for your loving directions.
