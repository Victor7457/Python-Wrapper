import System.Environment

subtractBy255 :: [Int] -> [Int]
subtractBy255 [] = []
subtractBy255 (x:xs) = (255 - x) : subtractBy255 xs

main :: IO()
main = do
    args <- getArgs
    let numbers = map read args :: [Int]
        result = subtractBy255 numbers
        resultStrings = map show result
        outputString = unwords resultStrings
    putStrLn outputString