def sliding_window(arr,window_size):
    for i in range(len(arr)-window_size+1):
        yield arr[i:i+window_size]  #yield is a keyword in python which is used to return a value from a function without causing the function to end.



        