countBits :: Int -> Int
countBits 0 = 0
countBits x = x `mod` 2 + countBits (x `div` 2)
