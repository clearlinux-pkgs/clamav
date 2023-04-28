PKG_NAME := clamav
URL = https://www.clamav.net/downloads/production/clamav-1.0.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/clamav/snapshot/clamav-2023-04-28-17-57-23.tar.xz ./vendor

include ../common/Makefile.common
