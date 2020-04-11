"""
You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.


int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp. However, granularity means the time level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.
"""


class LogSystem:

    def __init__(self):
        """
        T(n) = O(1)
        S(n) = O(n)
        """
        self.log = {}
        self.gran_map = m = dict(zip(
            ["Year", "Month", "Day", "Hour", "Minute", "Second"], [i for i in range(1, 7)]))

    def put(self, id: int, timestamp: str) -> None:
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        self.log[id] = timestamp.split(":")

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        """
        T(n) = O(n)
        S(n) = O(n) -- size of solution
        """
        idx = self.gran_map[gra]
        start = s.split(":")[:idx]
        end = e.split(":")[:idx]

        ids = []
        for (log_id, ts) in self.log.items():
            if start <= ts[:idx] <= end:
                ids.append(log_id)
        return ids


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
