# RobotGym Test

I used RobotGym to test a simple pick-and-place task with a Franka Panda robot.

The task was to pick up a red cube and place it in a tray.

I tried a few different versions of the scene:

- normal setup
- cube moved 10 cm to the right
- another similar red cube nearby
- multiple red cubes
- target cube partly blocked by a mug

All of the tests worked successfully.

I also ran into a 413 Payload Too Large error after doing several edits and runs in the same session.

The results are in `results/results.csv`.
