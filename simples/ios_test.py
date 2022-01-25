
from auto_test import AutoTest


def main():
    auto = AutoTest()

    auto.stepTextInScreen('任务中心')
    # auto.stepTextInScreen('Get X')
    # auto.stepTextInScreen('审核通过')
    auto.stepBack()


if __name__ == "__main__":
    main()
