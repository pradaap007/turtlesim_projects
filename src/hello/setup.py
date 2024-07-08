from setuptools import find_packages, setup

package_name = 'hello'

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
    maintainer='praveen',
    maintainer_email='praveen@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "hello_node=hello.hello_world:main",
            "make_circle=hello.turtle_circle:main",
            "go_to_goal=hello.gotogoal:main",
            "box_turtle=hello.border:main",
            "rec_turtle=hello.rectangle:main",
            "pen=hello.pentouch:main",
            "singel_sub=hello.subonly:main"
        ],
    },
)
