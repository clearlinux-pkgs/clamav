PKG_NAME := clamav
URL = https://www.clamav.net/downloads/production/clamav-1.2.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/clamav/snapshot/clamav-2024-04-24-21-48-13.tar.xz ./vendor

include ../common/Makefile.common
