# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_nb_new1_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED nb_new1_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(nb_new1_FOUND FALSE)
  elseif(NOT nb_new1_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(nb_new1_FOUND FALSE)
  endif()
  return()
endif()
set(_nb_new1_CONFIG_INCLUDED TRUE)

# output package information
if(NOT nb_new1_FIND_QUIETLY)
  message(STATUS "Found nb_new1: 0.3.0 (${nb_new1_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'nb_new1' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${nb_new1_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(nb_new1_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${nb_new1_DIR}/${_extra}")
endforeach()
