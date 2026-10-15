class PDController:
    def __init__(self, Kp, Kd):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0

    def __call__(self, reference, observation):
        error = reference - observation
        control_action = (
            self.Kp * error + self.Kd * (error - self.previous_error)
        )
        self.previous_error = error
        return control_action