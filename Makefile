PKG_NAME := clamav
URL = https://www.clamav.net/downloads/production/clamav-1.2.0.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/clamav/snapshot/clamav-2023-08-29-14-08-10.tar.xz ./vendor

include ../common/Makefile.common
