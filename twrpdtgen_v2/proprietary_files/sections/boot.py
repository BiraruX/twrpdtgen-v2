# BACKUP REPLACE FILE

#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from twrpdtgen_v2.proprietary_files.section import Section, register_section

class BootSection(Section):
	name = "Boot"
	interfaces = [
		"android.hardware.boot",
	]

register_section(BootSection)
