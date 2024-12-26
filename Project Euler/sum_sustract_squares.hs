-- 1`2 - 2`2 + 3^2 - 4^2 ... + 99^2 - 100^2

oddNumbers :: [Integer]
oddNumbers = [x | x <- [1..], x `mod` 2 == 0]

evenNumbers :: [Integer]
evenNumbers = [x - 1 | x <- oddNumbers]

square :: Integer -> Integer
square x = x * x

oddNumbersSquare :: [Integer]
oddNumbersSquare = map square (takeWhile (<=100) oddNumbers)

evenNumbersSquare :: [Integer]
evenNumbersSquare = map square (takeWhile (<=99) evenNumbers)

result :: Integer
result = sum evenNumbersSquare - sum oddNumbersSquare
