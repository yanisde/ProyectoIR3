SPRINT 2 - Scripts de prueba para JetBot real (ROS 2)

Archivos:
 draw3.py                 - reproduce la secuencia de dibujo del 3
 collision_avoidance.py   - sigue el dibujo y se detiene al detectar un obstaculo
 obstacle_avoidance.py    - intenta rodear el obstaculo siguiendo puntos de paso

ADVERTENCIA: Estos programas no se han validado en el JetBot real.
Son adaptaciones de los scripts entregados para Gazebo.

REQUISITOS:
- ROS 2 y dependencias rclpy, geometry_msgs, sensor_msgs, nav_msgs, std_srvs.
- Controlador del robot iniciado: ros2 launch jetbot_pro_ros2 jetbot.py
- Confirmar ros2 topic type /cmd_vel, /scan, /odom. No asumir que /scan existe sin comprobarlo.
- No ejecutar simultaneamente joy.py, teleop u otro publicador de /cmd_vel.
- Revisar entorno, espacio despejado, bateria, comunicacion y medios de parada.
- Los tres programas ARRANCAN EN PAUSA: solo se mueven despues de /g03/resume.

EJECUCION (solo uno a la vez):
 python3 draw3.py
 python3 collision_avoidance.py
 python3 obstacle_avoidance.py

CONTROLES (desde otra terminal ROS con el mismo dominio):
 ros2 service call /g03/resume std_srvs/srv/Trigger '{}'
 ros2 service call /g03/pause std_srvs/srv/Trigger '{}'
 ros2 service call /g03/restart std_srvs/srv/Trigger '{}'

AL TERMINAR: pulsar Ctrl+C en el nodo y comprobar que los motores se detengan.
Ante cualquier comportamiento inesperado, emplear la parada fisica del robot.

LIMITACIONES:
- Duraciones y velocidades sin calibrar con el JetBot; el 3 puede salir diferente.
- restart no recoloca fisicamente el robot.
- Se depende de /scan para collision y de /scan y /odom para obstacle.
- Desvio por waypoints originalmente concebido para cubo simulado de 0.5 m;
  no es navegacion autonoma segura ni garantiza evitar otros obstaculos laterales.
- No ejecutar obstacle_avoidance en un entorno no controlado hasta validar distancias,
  orientacion y sensores a baja velocidad.
