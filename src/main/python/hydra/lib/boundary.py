__author__ = 'sushil'

# A class to do binary search and tune one
# parameter.

from pprint import pprint, pformat  # NOQA


class Scanner(object):
    def __init__(self, runfunction, starting_value, search_approx=2):
        self.start_value = starting_value
        self.runfn = runfunction
        self.threshold = search_approx

    def search(self, expected_result):
        value = self.start_value
        inc = 0
        last_increase = value
        first_toggle = False
        cnt = 0
        self.inital_toggle_count = 0
        status = True
        while True:
            (status, res) = self.runfn(value)
            if not status:
                break
            if res <= expected_result:
                if not first_toggle:
                    # aggressively increase in the begining
                    inc = value
                else:
                    # Once an area is found do search
                    inc = abs(last_increase / 2)
            else:
                inc = -1 * abs(last_increase / 2)
                first_toggle = True
            # pprint(" Iteration %d ::" % cnt + " value = %d res = %d inc = %f" % (value, res, inc) +
            #       " :: last_increase = %d" % last_increase)
            if abs(last_increase) < self.threshold:
                break
            last_increase = inc
            value += inc
            cnt += 1
            if not first_toggle:
                self.inital_toggle_count += 1
        return (status, cnt, value)
