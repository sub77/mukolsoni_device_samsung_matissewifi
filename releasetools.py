# Copyright (C) 2014 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

""" Custom OTA commands for matisse devices """

def FullOTA_InstallEnd(info):
  info.script.Mount("/system")
  info.script.AppendExtra('ifelse(is_substring("T530", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/blobs/matissewifi/* /system/"));')
  info.script.AppendExtra('ifelse(is_substring("T535", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/blobs/matisselte/* /system/"));')
  info.script.AppendExtra('ifelse(is_substring("T531", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/blobs/matisse3g/* /system/"));')
  info.script.AppendExtra('set_metadata("/system/bin/ATFWD-daemon", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  info.script.AppendExtra('set_metadata("/system/bin/ds_fmc_appd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  info.script.AppendExtra('set_metadata("/system/bin/qmuxd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  info.script.AppendExtra('set_metadata("/system/bin/radish", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  info.script.AppendExtra('set_metadata("/system/bin/rild", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:rild_exec:s0");')
  info.script.Unmount("/system")
