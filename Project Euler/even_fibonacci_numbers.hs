fib :: [Integer]
fib = 1 : 2 : zipWith (+) fib (tail fib)

fibEven :: [Integer]
fibEven = [x | x <- fib, even x]

fibEvenSum :: Integer -> Integer
fibEvenSum a = sum (takeWhile (< a) fibEven)
