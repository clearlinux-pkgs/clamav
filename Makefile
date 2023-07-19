PKG_NAME := clamav
URL = https://www.clamav.net/downloads/production/clamav-1.1.0.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/clamav/snapshot/clamav-2023-07-19-20-01-21.tar.xz ./vendor

include ../common/Makefile.common
