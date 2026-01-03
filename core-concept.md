# Core Concepts & Architecture
> The following has been adopted from the official documentation for the bot architecture, which can be referred [here](https://github.com/pollen-robotics/reachy_mini/blob/develop/docs/SDK/core-concept.md).
## Coordinate Systems

When moving the robot, you will work with two main reference frames:

### 1. Head Frame
Located at the base of the head. Used for `goto_target` and `set_target` commands.

### 2. World Frame
Fixed relative to the robot's base. Used for `look_at_world` commands.

## Safety Limits ⚠️

Reachy Mini has physical and software limits to prevent self-collision and damage. The SDK will automatically clamp values to the closest valid position.

| Joint / Axis | Limit Range |
| :--- | :--- |
| **Head Pitch/Roll** | [-40°, +40°] |
| **Head Yaw** | [-180°, +180°] |
| **Body Yaw** | [-160°, +160°] |
| **Yaw Delta** | Max 65° difference between Head and Body Yaw |

## Motor Modes

You can change how the motors behave:
* **`mini.enable_motors()`**: Stiff. Holds position.
* **`mini.disable_motors()`**: Limp. No power.
* **`mini.enable_gravity_compensation()`**: "Soft" mode. You can move the head by hand, and it will stay where you leave it. (Only works with the Placo kinematics backend.)
