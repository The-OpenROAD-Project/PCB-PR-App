cmake_minimum_required(VERSION 3.1)

project(PCBAPP)
include(ExternalProject)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(THREADS_PREFER_PTHREAD_FLAG ON)
set(ALLOW_DUPLICATE_CUSTOM_TARGETS TRUE)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -pthread -O3 -fpermissive -fPIC")
set(CMAKE_CXX_FLAGS_DEBUG "-g -ggdb")

find_package(Boost REQUIRED)
set(SWIG_EXECUTABLE "/bin/swig")
#find_package(Swig REQUIRED)
#set(SWIG_EXECUTABLE "/usr/local/bin/swig")
find_package( PythonInterp 2.7 REQUIRED )
find_package( PythonLibs 2.7 REQUIRED )

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARYDIR})

set(APP_HOME ${PROJECT_SOURCE_DIR} )

set(KICADPARSER_HOME
  ${PROJECT_SOURCE_DIR}/module/KicadParser
)
set(PCBPLACER_HOME 
  ${PROJECT_SOURCE_DIR}/module/SA-PCB
)
set(PCBROUTER_HOME
  ${PROJECT_SOURCE_DIR}/module/PcbRouter
)
ExternalProject_Add(pcbplacer
  PREFIX ${PCBPLACER_HOME}
  SOURCE_DIR ${PCBPLACER_HOME}
  BINARY_DIR ${PCBPLACER_HOME}/bin
  INSTALL_DIR ${PCBPLACER_HOME}/bin
  DOWNLOAD_COMMAND ""
  INSTALL_COMMAND ""
)
ExternalProject_Add(pcbrouter
  PREFIX ${PCBROUTER_HOME}
  SOURCE_DIR ${PCBROUTER_HOME}
  BINARY_DIR ${PCBROUTER_HOME}/bin
  INSTALL_DIR ${PCBROUTER_HOME}/bin
  DOWNLOAD_COMMAND ""
  INSTALL_COMMAND ""
)
ExternalProject_Add(kicadparser
  PREFIX ${KICADPARSER_HOME}
  SOURCE_DIR ${KICADPARSER_HOME}
  BINARY_DIR ${KICADPARSER_HOME}/bin
  INSTALL_DIR ${KICADPARSER_HOME}/bin
  DOWNLOAD_COMMAND ""
  INSTALL_COMMAND ""
)
#add_subdirectory(${PCBPLACER_HOME} EXCLUDE_FROM_ALL)
#add_subdirectory(${PCBROUTER_HOME} EXCLUDE_FROM_ALL)
#add_subdirectory(${KICADPARSER_HOME} EXCLUDE_FROM_ALL)

############################################################
# Install
############################################################
