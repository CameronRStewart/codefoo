class StairClimber:

    total_count = 0
    max_steps = 0
    n = 0

    def __init__(self):
        self.reinitialize()

    def reinitialize(self):
        self.total_count = 0
        self.max_steps = 0
        self.n = 0

    def climb_stairs(self, n, max_steps):
        self.reinitialize()
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            self.max_steps = max_steps
            self.n = n
            self.climb_step(0, [])
            return self.total_count

    def climb_step(self, branch_count, branch):
        if branch_count == self.n:
            self.total_count += 1
            print(branch)
            return
        elif branch_count > self.n:
            # We have overstepped, do not pass go, do not collect $100
            # this branch fails
            return
        else:  # keep going
            for i in range(1, self.max_steps + 1):
                new_count = branch_count + i
                branch.append(i)
                self.climb_step(new_count, branch)
                branch = []
            return
