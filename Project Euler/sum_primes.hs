sieve :: [Int] -> [Int]
sieve [] = []
sieve (x : y) = x : sieve [z | z <- y, z `mod` x /= 0] 

result :: Int -> Int
result x = sum (sieve [2..x])
