# robot_sim_demo



## 运行方法
roslaunch why_robot_sim robot_spawn.launch
rosrun why_robot_sim robot_keyboard_teleop.py
### 显示八叉树地图
roslaunch display.launch
rosrun rviz rviz

## 注意事项
确认升级Gazebo到**7.0及以上版本**

查看Gazebo版本方法：

```sh
$ gazebo -v
```

如果版本低于7.0，请升级Gazebo：

```sh
$ sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
$ wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get install gazebo7
```
