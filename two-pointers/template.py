# slow & fast runner: slow-> fast->->
def slow_fast_runner(self, seq):
    # initialize slow runner
    slow = seq[0]   # for index: slow = 0
    # fast-runner grows each iteration generally
    for fast in range(seq):     # for index: range(len(seq))
        #slow-runner grows with some restrictions
        if self.slow_condition(slow):
            slow = slow.next    # for index: slow += 1
        # process logic before or after pointers movement
        self.process_logic(slow, fast)