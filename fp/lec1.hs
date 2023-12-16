get_first_5 :: [String]
get_first_5 = fmap format elems
    where
        elems_inf = filter (\x -> x `mod` 100 == 0) [1..]
        elems = take 5 elems_inf
        format num = "Number is " ++ show (num :: Int)

main :: IO ()
main = do
    putStrLn $ show get_first_5
