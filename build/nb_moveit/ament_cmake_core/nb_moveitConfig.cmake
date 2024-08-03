# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_nb_moveit_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED nb_moveit_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(nb_moveit_FOUND FALSE)
  elseif(NOT nb_moveit_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(nb_moveit_FOUND FALSE)
  endif()
  return()
endif()
set(_nb_moveit_CONFIG_INCLUDED TRUE)

# output package information
if(NOT nb_moveit_FIND_QUIETLY)
  message(STATUS "Found nb_moveit: 0.3.0 (${nb_moveit_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'nb_moveit' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${nb_moveit_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(nb_moveit_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${nb_moveit_DIR}/${_extra}")
endforeach()
