import time


class TrafficLight:
    __color: str

    def __init__(self, color):
        self.__color = color

    def running(self):

        while True:
            if self.color == "red":
                print(self.color)
                time.sleep(1)
                self.color = "yellow"
            elif self.color == "yellow":
                print(self.color)
                time.sleep(1)
                self.color = "green"
            elif self.color == "green":
                print(self.color)
                time.sleep(1)
                self.color = "red"

        # if self.color == "red":
        #     print(self.color)
        #     time.sleep(1)
        #     self.color = "yellow"
        #     print(self.color)
        #     time.sleep(1)
        #     self.color = "green"
        #     print(self.color)
        #     time.sleep(1)
        #     self.running()
        # elif self.color == "yellow":
        #     print(self.color)
        #     time.sleep(1)
        #     self.color = "green"
        #     print(self.color)
        #     time.sleep(1)
        #     self.running()
        # elif self.color == "green":
        #     # print(self.color)
        #     time.sleep(1)
        #     self.color = "red"
        #     self.running()


my_traffic_light = TrafficLight("green")
my_traffic_light.running()
