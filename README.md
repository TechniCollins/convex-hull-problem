
## Pending Research


### Class Definition

#### Class 1
    class Point:
        def __init__(self):
            self.xpoint = self.get_random()
            self.ypoint = self.get_random()

        def get_random(self):
            return random.randrange(1, 100)

#### Vs Class 2

    class Point:
        def get_random(self):
            return random.randrange(1, 100)

        xpoint = self.get_random()
        ypoint = self.get_random()

Why does creating a list result in the same values for option 2 ?


### Other Questions

1. What's the significance of calculating angles? What's the logic?

2. Why Counterclockwise turns? What's the logic?

### Concepts

Trigonometry -> Law of cosines

Linear Algebra -> Vectors -> Cross products
