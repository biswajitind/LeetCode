class Solution:
    def distMoney(self, money: int, children: int) -> int:

        ch8 = 0
        # if we have less money to even give $1 to each, we are done here
        if money < children:
            return(-1)
        money -= children
        # if money is over before giving $8 to a single person, we are done.
        if money == 0:
            return(0)

        print('After $1', children, money)
        # Now lets try to give $7 to as many children as possible.
        ch8 = min(children, money // 7)
 
        # how much money is left.
        money = money - ch8 * 7

        #check how many childrens are left
        children -= ch8

        print('after ch8', ch8, children, money)
        #If Money is left after after distributing everyone $8,
        if children == 0:
            if money == 0:
                return(ch8)

            return(ch8 - 1)

        # Money is over after distributing everyone $8
        
        
        if money / children == 3:
            if children == 1:
                return(ch8 - 1)
            else:
                return(ch8)


        return(ch8)
        



        