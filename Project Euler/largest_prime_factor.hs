sieve :: [Int] -> [Int]
sieve [] = []
sieve (p : xs) = p : sieve [x | x <- xs, x `mod` p /= 0]

factors :: Int -> [Int]
factors a = [x | x <- [1..a], a `mod` x == 0]

primeFactors :: Int -> [Int]
primeFactors a = sieve (tail (factors a))

maxPrimeFactor :: Int -> Int
maxPrimeFactor a = maximum (primeFactors a)
