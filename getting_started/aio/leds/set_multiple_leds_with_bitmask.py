import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import asyncio

from sphero_sdk import AsyncSpheroRvr
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups
from sphero_sdk import SerialAsyncDal

# Get a reference to the asynchronous program loop
loop = asyncio.get_event_loop()

# Create an AsyncSpheroRvr object and pass in a SerialAsyncDal object, which in turn takes a reference to the program loop
rvr = AsyncSpheroRvr(
    dal=SerialAsyncDal(
        loop
    )
)


async def main():
    """ This program demonstrates how to set multiple LEDs on RVR with one function call to set_all_leds_with_32_bit_mask.

    """
    await rvr.wake()

    # Give RVR time to wake up
    await asyncio.sleep(2)

    # Turn off all lights
    await rvr.set_all_leds_with_32_bit_mask(
        RvrLedGroups.all_lights.value, [color for _ in range(10) for color in Colors.off.value]
    )
    await asyncio.sleep(1)

    # Set both front and rear power buttons to blue
    led_group_bitmask = RvrLedGroups.power_button_front.value | RvrLedGroups.power_button_rear.value  # 0x1c0000

    await rvr.set_all_leds_with_32_bit_mask(
        led_group_bitmask, [0, 0, 255, 255, 0, 0]
    )
    await asyncio.sleep(1)


# Run program loop until the main function has completed
loop.run_until_complete(
    main()
)

loop.stop()
loop.close()
