stringRange :: Int -> Int -> [Char] -> [Char]
stringRange init end text = [text !! x | x <- [init .. end]]

splitString :: Int -> [Char] -> [[Char]]
splitString n text = [stringRange (0 + x) ((n - 1) + x) text | x <- [0.. (length text - (n - 1)) - 1]]

charToString :: Char -> String
charToString c = [c]

multiplyList :: [Int] -> Int
multiplyList = foldl (*) 1

multiplyDigits :: [Char] -> Int
multiplyDigits text = multiplyList (map (read. charToString) text)

productSeries :: Int -> [Char] -> [Int]
productSeries n text = [multiplyDigits series | series <- splitString n text]

largestProductSeries :: Int -> Int -> Int
largestProductSeries n num = maximum (productSeries n (show num))
