cmake_minimum_required(VERSION 3.28)
project(lab5_AISD)

set(CMAKE_CXX_STANDARD 14)

add_executable(lab5_AISD lab5_AISD/main.cpp
        lab5_AISD/hash_table.h
        lab4_AISD/set.h
        lab4_AISD/set.cpp
        lab4_AISD/main.cpp)
