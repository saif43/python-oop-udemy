"""
Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a
given point of time. If there are more than 5 precious stones,
delete the first stone and store the new one.
"""


class Stone:
    stones = []

    def holdStone(self, stone):
        if len(self.stones) == 5:
            self.stones = self.stones[1::]

        self.stones.append(stone)
        return


instance = Stone()

instance.holdStone("1")
instance.holdStone("2")
instance.holdStone("3")
instance.holdStone("4")
instance.holdStone("5")
instance.holdStone("6")

print(instance.stones)
