# Test plan

## Basic test

The robot needs to pick up one object and place it inside a target area.

I will first try to get the same basic setup working a few times.

## Tests

### Move the object

Try the same task after moving the object:

- 10 cm right
- 10 cm left
- 15 cm farther away

### Add clutter

Add other objects around the target object:

- 2 extra objects
- 4 extra objects

### Similar objects

Put similar-looking objects near each other and ask the robot to pick one specific object.

Try different spacing between the objects, such as 10 cm and 5 cm.

### Camera and lighting

If the earlier tests work, try changing the camera angle or lighting and see if that affects the result.

## What I will record

For each run I will record whether it worked, the RobotGym run ID if there is one, and a short note about what happened.

If something fails in an interesting way, I will try it again to see if the same failure happens more than once.
