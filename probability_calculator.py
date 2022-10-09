import random
import copy


class Hat:
    def __init__(self, **balls):
        if len(balls) == 0:
            raise TypeError("At least one keyword argument expected!")
        self.contents = []
        for value in balls:
            for t in range(balls[value]):
                self.contents.append(value)

    def draw(self, no_of_balls):
        if len(self.contents) < no_of_balls:
            return self.contents
        return [self.contents.pop(random.randint(0, len(self.contents) - 1)) for x in range(no_of_balls)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    got_expected = 0
    for i in range(num_experiments):
        result = True
        copied_hat = copy.deepcopy(hat)
        actual = copied_hat.draw(num_balls_drawn)
        expected = copy.deepcopy(expected_balls)
        for ball in actual:
            if expected.get(ball) is not None:
                expected[ball] -= 1
        for x in expected.values():
            if x > 0:
                result = False
        if result:
            got_expected += 1
    return got_expected / num_experiments


if __name__ == '__main__':
    hat1 = Hat(yellow=3, blue=2, green=6)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    hat1.draw(2)
    hat4 = Hat(black=6, red=4, green=3)
    prob = experiment(hat=hat4,
                      expected_balls={"red": 2, "green": 1},
                      num_balls_drawn=5,
                      num_experiments=2000)
    print(prob)
