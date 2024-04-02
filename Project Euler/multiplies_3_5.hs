-- multiplies :: Int -> [Int]
-- multiplies a = [x | x <- [0..((abs a) - 1)], x `mod` 3 == 0 || x `mod` 5 == 0]

-- multipliesSum :: Int -> Int
-- multipliesSum a = sum (multiplies a)

multiplies3 :: Int -> [Int]
multiplies3 a = [x | x <- [0, 3..a], x < a]

multiplies5 :: Int -> [Int]
multiplies5 a = [x | x <- [0, 5 ..a], x < a]

removeDuplicates :: [Int] -> [Int]
removeDuplicates [] = []
removeDuplicates (x : xs)
  | x `elem` xs = removeDuplicates xs
  | otherwise = x : removeDuplicates xs

multiplies3And5 :: Int -> [Int]
multiplies3And5 a = removeDuplicates (multiplies3 a ++ multiplies5 a)

multipliesSum :: Int -> Int
multipliesSum a = sum (multiplies3And5 a)
