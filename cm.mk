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

# Inherit some common CM stuff.
$(call inherit-product, vendor/cm/config/common_full_tablet_wifionly.mk)
#$(call inherit-product, vendor/cm/config/common_full.mk)
# Inherit device configuration
$(call inherit-product, device/samsung/matissewifi/full_matissewifi.mk)


#TARGET_BOOTANIMATION_SIZE := 480x320

# Release name
PRODUCT_RELEASE_NAME := SM-T530
PRODUCT_NAME := cm_matissewifi
