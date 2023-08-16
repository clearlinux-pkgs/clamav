PKG_NAME := clamav
URL = https://www.clamav.net/downloads/production/clamav-1.1.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/clamav/snapshot/clamav-2023-08-16-16-46-09.tar.xz ./vendor

include ../common/Makefile.common
