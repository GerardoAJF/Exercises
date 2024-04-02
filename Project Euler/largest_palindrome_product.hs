charNumbers :: [String]
charNumbers = [show x | x <- [1 ..]]

isThreeDigitNumbers :: Int -> Bool
isThreeDigitNumbers a = length (show a) == 3

palindromeNumbers :: [String]
palindromeNumbers = [x | x <- charNumbers, x == reverse x]

palindromeNumbersTo :: Int -> [Int]
palindromeNumbersTo a = takeWhile (<= a) (map read palindromeNumbers)

factors :: Int -> [Int]
factors a = [x | x <- [1 .. a], a `mod` x == 0]

threeFactors :: Int -> [(Int, Int)]
threeFactors a = [(x, a `div` x) | x <- filter isThreeDigitNumbers (factors a), isThreeDigitNumbers (a `div` x)]

palindromeProducts :: Int -> [Int]
palindromeProducts a = [x | x <- reverse (palindromeNumbersTo a), not (null (threeFactors x))]
                       
head' [] = 0
head' (x:xs) = x

largestPalindromeProduct :: Int -> Int
largestPalindromeProduct a = head' (take 1 (palindromeProducts a))
