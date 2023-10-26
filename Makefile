PKG_NAME := clamav
URL = https://www.clamav.net/downloads/production/clamav-1.2.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/clamav/snapshot/clamav-2023-10-26-14-00-28.tar.xz ./vendor

include ../common/Makefile.common
