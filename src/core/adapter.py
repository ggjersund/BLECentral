"""
Setup the local Bluetooth adapter.
Handle requests for turn on bluetooth, check version and if bluetooth is enabled etc.

The Bluetooth adapter must be accessed via loadBunlde

"""

import objc

objc.loadBundleFunctions(
    objc.loadBundle("IOBluetooth", globals(), bundle_path=objc.pathForFramework(u'/System/Library/Frameworks/IOBluetooth.framework')),
    globals(),
    [('IOBluetoothPreferenceGetControllerPowerState', b'oI'),('IOBluetoothPreferenceSetControllerPowerState', b'vI')]
)

# Turn bluetooth on
IOBluetoothPreferenceSetControllerPowerState(1)

# Turn bluetooth off
