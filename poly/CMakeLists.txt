
set (
    SRCS
    Dilithiumpoly.cpp
    kyberpoly.cpp
    poly.cpp
)

set(HEADERS
    Dilithiumpoly.h
    kyberpoly.h
    poly.h
    reduce.h
    reduce_impl.h
    debug.h
)

add_library (
    poly
    STATIC
    ${SRCS}
    ${HEADERS}
)

target_include_directories(poly PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>)
set_target_properties(poly
  PROPERTIES
  PUBLIC_HEADER "${HEADERS}"
)