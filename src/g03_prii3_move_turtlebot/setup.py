from setuptools import find_packages, setup

package_name = 'g03_prii3_move_turtlebot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yanis',
    maintainer_email='yanis@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
        entry_points={
        'console_scripts': [
            'draw_number = g03_prii3_move_turtlebot.draw3:main',
            'collision_avoidance = g03_prii3_move_turtlebot.collision_avoidance:main',
            'obstacle_avoidance = g03_prii3_move_turtlebot.obstacle_avoidance:main',
        ],
    },
)
