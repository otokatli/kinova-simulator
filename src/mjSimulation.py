import mujoco as mj
import numpy as np
import os


class mjSimulation:
    def __init__(self, robot_name):

        if robot_name == 'kinova_gen3':
            self._robot_xml_path = os.path.join('assets', 'kinova_gen3', 'robot.xml')
        else:
            self._robot_xml_path = ''
        
        self.model = mj.MjModel.from_xml_path(self._robot_xml_path)
        self.data = mj.MjData(self.model)

        mj.set_mjcb_control(self.controller)

    def controller(self, model, data):
        Kp = 100
        Kd = 8

        self.data.ctrl = Kp * (np.zeros(7) - self.data.qpos) + Kd * (np.zeros(7) - self.data.qvel)

    def init_controller(self):
        pass

    def init_sensor(self):
        pass

    def step(self):
        mj.mj_step(self.model, self.data)
    