squares :: [Int]
squares = [x ^ 2 | x <- [1..]]

sumSquares :: Int -> Int
sumSquares a = sum (take a squares)

sumNumbers :: (Num a, Enum a) => Int -> a
sumNumbers a = sum (take a [1..])

absoluteDifference :: Int -> Int
absoluteDifference a = sumNumbers a ^ 2 - sumSquares a
