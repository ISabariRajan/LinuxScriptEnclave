#!/usr/bin/env python3

import os
import sys
import json

MOUNT_DIR = "/mounts/"
sys.path.append(os.environ["DEV_HELPER_PY_SCRIPT_PATH"])
from Utilities.package import DeviceUtilities

print(sys.argv)
utils = DeviceUtilities("MountAllDisks")
utils.log("Started")
utils.check_and_create_dir(MOUNT_DIR)
utils.change_dir_owner(MOUNT_DIR, "sambare", "adm")
utils.change_file_permission(MOUNT_DIR + "*", permission="770")

drives = utils.get_connected_drives_by_type("part")
lvms = utils.get_connected_drives_by_type("lvm")

lvms_phy_vol = utils.get_lvm_physical_volumes(skip_vgs=["vgubuntu"])
for key in lvms_phy_vol:
    lvm = lvms_phy_vol[key]
    for device_path in lvm["devices"]:
        try:
            del drives[device_path]
        except KeyError:
            pass

        if(device_path in lvm["devices"]):
            l = lvms[key]
            l["label"] = lvm["vg_name"] + "--" + lvm["lv_name"]

            if not lvm["skip"]:
                drives[key] = lvms[key]

unmount_devices = {}
mount_devices = {}
process_devices = {}

for device_path in drives:
    device = drives[device_path]
    umount = False

    # Generate mount directory for partitions
    if(device["label"] != ""):
        mount_dir = os.path.join(MOUNT_DIR, device["label"])
    else:
        mount_dir = os.path.join(MOUNT_DIR, device["size"] + " Size Volume")
    mountpoint = device["mountpoint"]

    if("/media" in mountpoint):
        umount = True
        mountpoint = ""

    # Skip mounting if they are mounted in / or / boot
    # or If already mounted Skip mounting
    if(mountpoint == "/") or ("/boot" in mountpoint) or (len(mountpoint) > 0 ):
        continue

    # If there is mountpoint for the device
    if(mountpoint != ""):
        utils.log("Check and Unmount device " + device_path + " with label: " + device["label"])
        if(MOUNT_DIR in mountpoint):
            umount = False
        else:
            umount = True

    if (device_path not in process_devices):
        process_devices[device_path] = {
            "mount_dir": mount_dir,
            "fstype": "",
            "umount": umount,
            "mount": True
        }
    if("lvm" not in device["fstype"].lower()):
        process_devices[device_path]["fstype"] = device["fstype"]

if len(process_devices) < 1:
    print("No device to mount/ process")

utils.log("", "Processing Following Devices")
for device_path in process_devices:
    device = process_devices[device_path]
    utils.log("", device_path, " - ", "Umount: ", device["umount"], " - Mount: ", device["mount"], " - " , device["fstype"])

if len(sys.argv) == 2:
    if sys.argv[1].lower() == "-y":
        choice = "y"
    else:
        choice = input("Proceed?[y/n] ")
else:
    choice = input("Proceed?[y/n] ")

if(choice == "y"):
    change_mount_drives = []
    for device_path in process_devices:
        device = process_devices[device_path]
        mount_dir = device["mount_dir"]
        utils.log("", device_path, " - ", "Umount: ", device["umount"], " - Mount: ", device["mount"], " - " , device["fstype"])
        if(device["umount"]):
            utils.check_and_unmount_device_path(device_path, force_unmount=True)
        elif(device["mount"]):
            try:
                utils.check_and_create_dir(mount_dir)
            except:
                pass
            if utils.check_and_mount_device_to_path(mount_dir, device_path, device["fstype"]):
                change_mount_drives.append(mount_dir)
    
    support_path = os.path.join(os.environ["SUPPORT_PATH"], "mounts.json")
    with open(support_path, "w") as f:
        f.write(json.dumps(change_mount_drives, indent=2))

    # for mount_dir in change_mount_drives:
    #     utils.change_mount_drive_permissions(mount_dir)

