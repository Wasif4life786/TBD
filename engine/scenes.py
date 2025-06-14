import math
from core.vector import Vec3
from core.gameobject import GameObject
from core.geometry import create_cube, create_sphere
from core.utility import linspace
from render.parametric_curves import ParametricCurve
from render.vectorfield import VectorField

def setup_spinning_shapes_scene():
    cube_geom = create_cube(size=1.5)
    sphere_geom = create_sphere(radius=1.0, rings=12, sectors=24)
    
    cube_obj = GameObject(vertices=cube_geom[0], triangles=cube_geom[1])
    cube_obj.position = Vec3(-2, 0, 0)
    
    sphere_obj = GameObject(vertices=sphere_geom[0], triangles=sphere_geom[1])
    sphere_obj.position = Vec3(2, 0, 0)
    
    scene_objects = [cube_obj, sphere_obj]
    light = Vec3(0.5, -1, -1).normalize()
    
    def update_scene():
        cube_obj.rotation.y += 0.01
        cube_obj.rotation.x += 0.005
        sphere_obj.rotation.z += 0.015

    return {
        "type": "meshes",
        "objects": scene_objects,
        "light": light,
        "update": update_scene
    }

def setup_vector_field_scene():
    bounds = (-3, 3, -3, 3, -1, 1)
    field = VectorField(VectorField.swirl_vector_field, bounds, resolution=8)
    return {
        "type": "lines",
        "lines": field.lines,
        "color": (100, 200, 255)
    }

def x_helix(t): return math.cos(t * 2) * 2
def y_helix(t): return math.sin(t * 2) * 2
def z_helix(t): return t * 0.5

def setup_parametric_curve_scene():
    helix = ParametricCurve(x_helix, y_helix, z_helix)
    helix.generate_points(t_min=-10, t_max=10, resolution=200)
    return {
        "type": "lines",
        "lines": helix.get_line_segments(),
        "color": (255, 100, 100)
    }
