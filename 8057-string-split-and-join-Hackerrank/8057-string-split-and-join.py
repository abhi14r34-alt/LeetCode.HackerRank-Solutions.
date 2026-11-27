

def split_and_join(line):
   line="-".join(line.split(" "))
   return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna