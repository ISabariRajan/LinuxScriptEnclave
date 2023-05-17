#!/usr/bin/env python3

import os
import sys

sys.path.append(os.environ["PYUTILS_PATH"])
from Utilities.package import DeviceUtilities, FileUtilities, environ
# import Constants as const

SUPPORT_PATH = os.environ["SUPPORT_PATH"]
MOUNT_DIR = "/mounts/"
CONFIG_PATH = SUPPORT_PATH + "/conf/samba/"
utils = DeviceUtilities("ShareMountedDisks")
fileutils = FileUtilities("ShareMountedDisks")
utils.log("Started")

lines = utils.generate_samba_config_from_connected_devices()
fileutils.check_and_create_dir(CONFIG_PATH)

utils.log(lines)

SAMBA_CONFIG_PATH = CONFIG_PATH + "program_samba_conf.config"
utils.log("Writing samba config in : " + SAMBA_CONFIG_PATH)
with open(SAMBA_CONFIG_PATH, "w") as f:
    f.writelines("\n".join(lines))

utils.log("Copy Samba Configuration")
utils.run_process(["cp " + CONFIG_PATH + "smb.conf.orig /etc/samba/smb.conf"])
utils.run_process(["cat " + SAMBA_CONFIG_PATH + " | tee -a /etc/samba/smb.conf > /dev/null"], True)
utils.run_process(["systemctl restart smbd"])
utils.run_process(["systemctl restart smb"])

utils.log("Ended")

