#function for reading input, and returns a list of shares
def read():
    #list for shares
    shares = []

    #runs until share is 0, to exit
    share = None
    while share != 0:
        #prompting and reading shares
        share = int(input("Please enter the number of shares: "))

        #if input is invalid
        if share < 0:
            print("Invalid input!")

        #adding share to shares list
        elif share != 0:
            shares.append(share)

    return shares


#sort function, returns sorted list of shares, in descending order
def sort(shares):
    #sorting shares list using built-in sorted function
    return sorted(shares, reverse=True)


#totalShares function, returns total shares in shares list
def totalShares(shares):
    #calculating sum of shares in shares list using built-in sum
    return sum(shares)


#shareHolders functions, number of top shareholder needed
def shareHolders(shares, requiredShares):
    #sorting shares list using sort function
    shares = sort(shares)

    #variable for storing count of shareholders
    count = 0
    total = 0

    #iterating over shares list
    for share in shares:
        #incrementing total by adding share to it
        total += share
        #increment count by 1
        count += 1

        #if total reached requiredShare, returns count
        if total >= requiredShares:
            return count


#main program
#calling read() function
shares = read()

#calculating and printing total shares
total = totalShares(shares)
print(f"Thank you, there is a total of {total} shares represented here.")

#calculating requried shares to win
requiredShares = total//2 + 1
print(f"Shares needed for majority vote is {requiredShares}.")

#calling shareHolders function, to count top required shareholders
topShareHolders = shareHolders(shares, requiredShares)
print(f"You need the support of top {topShareHolders} shareholders for this number of votes.")



#bonus
#creating and opening text file named "Apple" in write mode
with open("Apple.txt", 'w') as file:
    #writing data to text file using wite method of file object(file)
    file.write(f"Thank you, there is a total of {total} shares represented here." + "\n")
    file.write(f"Shares needed for majority vote is {requiredShares}." + "\n")
    file.write(f"You need the support of top {topShareHolders} shareholders for " +
    "this number of votes.")

