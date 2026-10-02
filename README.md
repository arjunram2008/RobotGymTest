# RobotGym Test

I made this repo to test RobotGym and learn more about robot simulation.

The main test is simple: have the robot pick up an object and place it in a target area. After I get that working, I want to change the scene a little at a time and see when the robot starts having trouble.

I plan to test:

- moving the object
- adding other objects around it
- putting similar objects close together
- changing the camera or lighting

I will save the results in `results/results.csv` and keep useful feedback in `notes/feedback.md`.

## Files

- `test-plan.md` - what I am testing
- `results/results.csv` - results from each run
- `scripts/analyze_results.py` - simple script to summarize the results
- `notes/feedback.md` - things I notice while using RobotGym

## Running the analysis

```bash
python scripts/analyze_results.py
```

I have not filled in the results yet. I will update this repo as I run the tests in RobotGym.
