isPrime :: Int -> Bool
isPrime n = and [mod n x /= 0 | x <- [2..n-1]]

primes :: [Int]
primes = [x | x <- [2..], isPrime x]

nstPrime :: Int -> Int
nstPrime n = primes !! (n - 1) 
