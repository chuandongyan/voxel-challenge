from scene import Scene
import taichi as ti
from taichi.math import *
scene = Scene(exposure=1)
scene.set_floor(-1, (1.0, 1.0, 1.0))
#scene.set_background_color((0.5, 0.5, 0.5))
scene.set_directional_light((1, 1, 1), 0.1, (1, 1, 1))
scene.set_background_color((0.3, 0.4, 0.6))
n = 60
@ti.kernel
def magicsquare():
    #rgb
    for x,y,z in ti.ndrange((n//3),(n//3),(n//3)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 0, 1.0))
    for x,y,z in ti.ndrange((n//3),(n//3,n//3*2),(n//3)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 1.0, 0))
    for x,y,z in ti.ndrange((n//3),(n//3*2,n),(n//3)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(1.0, 0, 0))
    for x,y,z in ti.ndrange((n//3*2,n),(n//3),(n//3,n//3*2)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 0, 1.0))
    for x,y,z in ti.ndrange((n//3*2,n),(n//3,n//3*2),(n//3,n//3*2)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 1.0, 0))
    for x,y,z in ti.ndrange((n//3*2,n),(n//3*2,n),(n//3,n//3*2)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(1.0, 0, 0))
    for x,y,z in ti.ndrange((n//3,n//3*2),(n//3),(n//3*2,n)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 0, 1.0))
    for x,y,z in ti.ndrange((n//3,n//3*2),(n//3,n//3*2),(n//3*2,n)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 1.0, 0))
    for x,y,z in ti.ndrange((n//3,n//3*2),(n//3*2,n),(n//3*2,n)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(1.0, 0, 0))
    #gbr
    for x,y,z in ti.ndrange((n//3,n//3*2),(n//3),(n//3)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(1.0, 0, 0))
    for x,y,z in ti.ndrange((n//3,n//3*2),(n//3,n//3*2),(n//3)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 0, 1.0))
    for x,y,z in ti.ndrange((n//3,n//3*2),(n//3*2,n),(n//3)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 1.0, 0))
    for x,y,z in ti.ndrange((n//3),(n//3),(n//3,n//3*2)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(1.0, 0, 0))
    for x,y,z in ti.ndrange((n//3),(n//3,n//3*2),(n//3,n//3*2)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 0, 1.0))
    for x,y,z in ti.ndrange((n//3),(n//3*2,n),(n//3,n//3*2)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 1.0, 0))
    for x,y,z in ti.ndrange((n//3*2,n),(n//3),(n//3*2,n)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(1.0, 0, 0))
    for x,y,z in ti.ndrange((n//3*2,n),(n//3,n//3*2),(n//3*2,n)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 0, 1.0))
    for x,y,z in ti.ndrange((n//3*2,n),(n//3*2,n),(n//3*2,n)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 1.0, 0))
    #brg  
    for x,y,z in ti.ndrange((n//3*2,n),(n//3),(n//3)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 1.0, 0))
    for x,y,z in ti.ndrange((n//3*2,n),(n//3,n//3*2),(n//3)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(1.0, 0, 0))
    for x,y,z in ti.ndrange((n//3*2,n),(n//3*2,n),(n//3)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 0, 1.0))
    for x,y,z in ti.ndrange((n//3,n//3*2),(n//3),(n//3,n//3*2)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 1.0, 0))
    for x,y,z in ti.ndrange((n//3,n//3*2),(n//3,n//3*2),(n//3,n//3*2)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(1.0, 0, 0))
    for x,y,z in ti.ndrange((n//3,n//3*2),(n//3*2,n),(n//3,n//3*2)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 0, 1.0))
    for x,y,z in ti.ndrange((n//3),(n//3),(n//3*2,n)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 1.0, 0))
    for x,y,z in ti.ndrange((n//3),(n//3,n//3*2),(n//3*2,n)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(1.0, 0, 0))
    for x,y,z in ti.ndrange((n//3),(n//3*2,n),(n//3*2,n)):
        scene.set_voxel(vec3(x,y,z), 1, vec3(0, 0, 1.0))
magicsquare()
scene.finish()