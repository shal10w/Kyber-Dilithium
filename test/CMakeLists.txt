add_executable(dilithium_test dilithium_test.cpp)
target_link_libraries(dilithium_test PRIVATE poly)

add_executable(kyber_test kyber_test.cpp)
target_link_libraries(kyber_test PRIVATE poly)

add_executable(polyvec_test polyvec_test.cpp)
target_link_libraries(polyvec_test PRIVATE poly)