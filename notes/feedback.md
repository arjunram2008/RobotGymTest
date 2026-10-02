# RobotGym feedback

## What worked well

- Creating a basic scene from a text description was easy.
- The robot handled the basic pick-and-place task consistently.
- Moving the target cube did not cause a problem.
- It was able to choose the correct cube when similar red cubes were nearby.
- It was also able to follow a more specific instruction when the target cube was partly blocked by a mug.
- The different camera views were useful for seeing what the robot was doing during a run.

## Problem I ran into

After several scene changes and runs in the same session, I got this error:

`413 Payload Too Large`

The message came from the RobotGym backend. Starting again with a fresh session allowed me to continue testing.

It might be useful if longer sessions could avoid this error or show a clearer message about what needs to be restarted.

## Overall

I expected at least one of the harder setups to confuse the robot, but all of the tests I ran worked. The most interesting result for me was that it could still identify the correct cube when there were several similar cubes and the target was partly obstructed.
