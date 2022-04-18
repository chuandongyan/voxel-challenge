from scene import Scene
import taichi as ti
from taichi.math import *
scene = Scene(exposure=1)
scene.set_floor(-1, (1.0, 1.0, 1.0))
scene.set_directional_light((1, 1, 1), 0.1, (1, 1, 1))
scene.set_background_color((0.3, 0.4, 0.6))
n = 60
@ti.kernel
def initialize_voxels():
    for x in range(n+1):
        scene.set_voxel(vec3(x,0,0), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(0,x,0), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(0,0,x), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(n,x,0), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(x,n,0), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(0,x,n), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(n,0,x), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(0,n,x), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(x,0,n), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(x,n,n), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(n,x,n), 2, vec3(0.9, 0.1, 0.1))
        scene.set_voxel(vec3(n,n,x), 2, vec3(0.9, 0.1, 0.1))
    for i,j,k in ti.ndrange((-n,0), (-n,0), (-n,0)):
        x = ivec3(i, j, k)
        if x.dot(x) < n*n*0.25 :
            scene.set_voxel(vec3(i, j, k), 1, vec3(0.9, 0.3, 0.3))
    for i,j,k in ti.ndrange(n, n, n):
        x = ivec3(i, j, k)
        if x.dot(x) < n*n*0.25 :
            scene.set_voxel(vec3(i, j,k), 1, vec3(0.2, 0.8, 0.3))
initialize_voxels()
scene.finish()
