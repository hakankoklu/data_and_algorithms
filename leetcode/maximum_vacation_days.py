class Solution:
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        cache = {}
        return self._max_vacation_days(flights, days, 0, 0, cache)

    def _max_vacation_days(self, flights, days, cur_city, week_no, cache):
        if len(days[0]) == week_no:
            return 0
        max_vac = 0
        if cache.get((cur_city, week_no)):
            return cache.get((cur_city, week_no))
        for i in range(len(flights)):
            if flights[cur_city][i] == 1 or cur_city == i:
                vac = days[i][week_no] + self._max_vacation_days(flights, days, i, week_no + 1, cache)
                max_vac = max(vac, max_vac)
                cache[(cur_city, week_no)] = max_vac
        return max_vac


if __name__ == '__main__':
    s = Solution()
    flights = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    days = [[1, 3, 1], [6, 0, 3], [3, 3, 3]]
    print(s.maxVacationDays(flights, days))