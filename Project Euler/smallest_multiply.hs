smallestMultiply :: Int -> Int
smallestMultiply a = head [x | x <- [1..], all (== 0) (map (mod x) [1..a])]
