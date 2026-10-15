class PDController:
    def __init__(self, Kp=0.15, Kd=0.6):
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