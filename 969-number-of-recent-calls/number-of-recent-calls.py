from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()  # \U0001f4e6 Queue to hold ping times

    def ping(self, t: int) -> int:
        self.queue.append(t)  # \U0001f4dd Add new ping

        # \U0001f9f9 Remove pings older than 3000ms
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)  # \U0001f3af Number of valid pings
