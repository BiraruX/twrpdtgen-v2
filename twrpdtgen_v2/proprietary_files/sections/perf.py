# BACKUP REPLACE FILE

#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from twrpdtgen_v2.proprietary_files.section import Section, register_section

class PerfSection(Section):
	name = "Perf"
	interfaces = [
		"vendor.qti.hardware.perf",
	]
	libraries = [
		"libqti-perfd-client",
	]
	filenames = [
		"powerhint.xml",
	]
	folders = [
		"etc/perf",
	]
	properties_prefixes = {
		"ro.vendor.extension_library": True,
	}

class PerfIopSection(Section):
	name = "Perf IOP"
	interfaces = [
		"vendor.qti.hardware.iop",
	]
	libraries = [
		"libqti-iopd-client",
	]

register_section(PerfSection)
register_section(PerfIopSection)
