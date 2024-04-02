squares :: Int -> [Int]
squares a = [x * x | x <- [1..a]]

squareTriplets :: Int -> [[Int]]
squareTriplets a = [[round (sqrt (fromIntegral x)), round (sqrt (fromIntegral y)), round (sqrt (fromIntegral z))] |
                   x <- squares a, 
                   y <- squares a,
                   x < y,
                   z <- squares a,
                   y < z,
                   x + y == z,
                   round (sqrt (fromIntegral x)) + round (sqrt (fromIntegral y)) + round (sqrt (fromIntegral z)) == a]

calculateProduct :: [Int] -> Int
calculateProduct = product

head' :: [[a]] -> [a]
head' [] = []
head' x = x !! 0

getMax :: [[a]] -> [a]
getMax x = head' (reverse x)

approved :: Int -> Int
approved x
  | x == 1 = -1
  | otherwise = x

calculateProductPythagoreanTriplet :: Int -> Int
calculateProductPythagoreanTriplet a = approved (calculateProduct (getMax (squareTriplets a)))
