cmake_minimum_required(VERSION 3.5)

project(average_calculate)

file(GLOB average_calculate "./*.c")
add_executable(average ${average_calculate})