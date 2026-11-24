if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    largest= float('-inf')
    seclargest= float('-inf')
    for i in range(len(arr)):
        if largest<arr[i]:
            largest,seclargest=arr[i],largest
        elif seclargest<arr[i] and largest >arr[i]:
            seclargest=arr[i]
    print(seclargest)    
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna