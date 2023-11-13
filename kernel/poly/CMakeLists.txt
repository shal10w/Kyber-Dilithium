
set (
    polySRCS
    Dilithiumpoly.cpp
    Kyberpoly.cpp
    poly.cpp
)

set(polyHEADERS
    Dilithiumpoly.h
    Kyberpoly.h
    poly.h
    reduce.h
    reduce_impl.h
    debug.h
)


#target_include_directories(poly PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>)
#set_target_properties(poly
#  PROPERTIES
#  PUBLIC_HEADER "${HEADERS}"
#)