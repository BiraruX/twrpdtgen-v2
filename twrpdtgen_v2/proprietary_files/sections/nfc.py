# BACKUP REPLACE FILE

#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from twrpdtgen_v2.proprietary_files.section import Section, register_section

class NfcSection(Section):
	name = "NFC"
	interfaces = [
		"android.hardware.nfc",
		"vendor.nxp.hardware.nfc",
		"vendor.oplus.hardware.nfcExtns",
		"vendor.oplus.hardware.nfc_aidl",
	]
	hardware_modules = [
		"nfc",
	]
	properties_prefixes = {
		"ro.nfc.": False,
	}

class NfcConfigsSection(Section):
	name = "NFC configs"
	folders = [
		"etc/nfc",
	]
	patterns = [
		"etc/libnfc-.*\.conf",
		"etc/sn100u_.*\.pnscr",
	]

register_section(NfcSection)
register_section(NfcConfigsSection)
