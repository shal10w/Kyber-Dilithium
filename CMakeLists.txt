cmake_minimum_required (VERSION 3.18)

project (Kyber-Dilithium LANGUAGES C CXX)
set(CMAKE_CXX_STANDARD 17)
set(CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_subdirectory(kernel)
add_subdirectory(test)



