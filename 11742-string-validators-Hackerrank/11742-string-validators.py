if __name__ == '__main__':
    s = input()
    alphaupper="ABCDEFGHIJKLMNOPQRSTUVWXYZS"
    alphalower="abcdefghijklmnopqrstuvwxyz"
    number="1234567890"
    alpha=alphalower+alphaupper
    alphanum=alphaupper+alphalower+number
  
n = False
a = False
d = False
l = False
u = False

for ch in s:
    if ch in alphanum:
        n = True
    if ch in alpha:
        a = True
    if ch in number:
        d = True
    if ch in alphalower:
        l = True
    if ch in alphaupper:
        u = True
print(n,a,d,l,u,sep="\n")   


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna