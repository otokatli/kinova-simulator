import mujoco as mj
from mujoco.glfw import glfw
import numpy as np
import os

from mjSimulation import mjSimulation
from mjVisualization import mjVisualization

simend = 100


mjs = mjSimulation('kinova_gen3')
mjv = mjVisualization(mjs)

#set initial conditions
mjs.data.qpos[0] = 0




while not glfw.window_should_close(mjv.window):
    simstart = mjs.data.time

    while (mjs.data.time - simstart < 1.0/60.0):
        mjs.step()

    if (mjs.data.time>=simend):
        break;

    # get framebuffer viewport
    viewport_width, viewport_height = glfw.get_framebuffer_size(mjv.window)
    viewport = mj.MjrRect(0, 0, viewport_width, viewport_height)

    # Update scene and render
    mj.mjv_updateScene(mjs.model, mjs.data, mjv.opt, None, mjv.cam, mj.mjtCatBit.mjCAT_ALL.value, mjv.scene)
    mj.mjr_render(viewport, mjv.scene, mjv.context)

    # swap OpenGL buffers (blocking call due to v-sync)
    glfw.swap_buffers(mjv.window)

    # process pending GUI events, call GLFW callbacks
    glfw.poll_events()

glfw.terminate()