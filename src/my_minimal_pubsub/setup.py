from setuptools import setup

package_name = 'my_minimal_pubsub'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/pubsub.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jagan',
    maintainer_email='jaganus006@gmail.com',
    description='Tiny ROS 2 pub/sub example',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_minimal_pubsub.talker:main',
            'listener = my_minimal_pubsub.listener:main',
        ],
    },
)

