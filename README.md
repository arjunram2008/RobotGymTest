# RobotGym Test

I made this project to try out RobotGym and learn more about robot simulation and manipulation.

The main task was simple: have the robot pick up a red cube and place it inside a tray. I started with an easy setup and then changed the scene to see how well the robot handled different situations.

## What I tested

- normal pick and place
- moving the cube 10 cm to the right
- adding another similar red cube nearby
- adding several similar red cubes and asking for the one closest to the tray
- partially blocking the target cube with a mug

The robot completed every test I tried successfully.

## Results

| Test | Result |
| --- | --- |
| Baseline setup | 3/3 successful |
| Cube moved 10 cm right | 3/3 successful |
| Similar red cube nearby | 3/3 successful |
| Multiple similar red cubes | 3/3 successful |
| Target partly blocked by a mug | 1/1 successful |

The last test was the most difficult one. There were several red cubes on the table, and a mug was partly blocking the target cube. The robot still picked the correct cube and placed it in the tray.

I also ran into a `413 Payload Too Large` error after working in the same session for a while. Starting again with a fresh session fixed the issue.

The individual runs are saved in `results/results.csv`.

## Files

- `test-plan.md` - the tests I ran
- `results/results.csv` - results from each run
- `scripts/analyze_results.py` - simple script to summarize the results
- `notes/feedback.md` - notes from using RobotGym

## Run the results script

```bash
python scripts/analyze_results.py
```
