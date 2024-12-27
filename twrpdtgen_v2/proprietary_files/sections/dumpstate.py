# BACKUP REPLACE FILE

#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from twrpdtgen_v2.proprietary_files.section import Section, register_section

class DumpstateSection(Section):
	name = "Dumpstate"
	interfaces = [
		"android.hardware.dumpstate",
	]

register_section(DumpstateSection)
