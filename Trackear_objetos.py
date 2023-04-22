import bpy

#Parametros
cube_count = 10
location_offset = 3
frame_count = 300

#Seteamos cantidad de Frames
bpy.context.scene.frame_end = frame_count

#Crear una fila de cubos
for i in range (cube_count):
    x = 0 
    y = i*location_offset
    z = 0
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))

#Crear un objeto vacio para trackear
bpy.ops.object.empty_add()
empty = bpy.context.active_object

#Animar las propiedades de posicion del objeto vacio
empty.location.y = location_offset*cube_count / 2

#Añadir una camara
bpy.ops.object.camera_add()
camera = bpy.context.active_object
camera.location.x = 15
camera.location.z = 2

#Mover la camara junto al objeto vacio
camera.keyframe_insert("location",frame=1)
camera.location.y = location_offset*cube_count
camera.keyframe_insert("location",frame=frame_count)

#Agregar el apuntado para que la camara siga al objeto vacio
bpy.ops.object.constraint_add(type='TRACK_TO')
camera.constraints["Apuntar"].target = empty