
add_subdirectory(poly)
add_subdirectory(vec)


add_library (
    kernel
    STATIC
    ${polySRCS}
    ${polyHEADERS}
    ${vecSRCS}
    ${vecHEADERS}
)
