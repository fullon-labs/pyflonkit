
add_cython_target(_pyflonkit CXX)

add_library(_pyflonkit MODULE
    ${_pyflonkit}
)

python_extension_module(_pyflonkit)

add_dependencies(_pyflonkit build_pyflonkit)

target_include_directories(_pyflonkit PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/go-uuoskit
)

if (WIN32)
    add_compile_definitions(MS_WIN64)
    SET(BUILD_TARGET pyflonkit.lib)
    # SET(BUILD_LIB_CMD go build -o pyflonkit.dll -buildmode=c-shared && cmake -E copy pyflonkit.dll ${CMAKE_CURRENT_SOURCE_DIR}/../pysrc/pyflonkit.dll && cmake -E copy libpyflonkit.bk.h libpyflonkit.h)
    SET(BUILD_LIB_CMD go build -o pyflonkit.dll -buildmode=c-shared && cmake -E copy pyflonkit.dll ${CMAKE_CURRENT_SOURCE_DIR}/../pysrc/pyflonkit.dll && gendef pyflonkit.dll && lib /def:pyflonkit.def /machine:x64 /out:pyflonkit.lib)
else()
    SET(BUILD_TARGET libpyflonkit.a)
    SET(BUILD_LIB_CMD go build -o libpyflonkit.a -buildmode=c-archive)
endif()

target_link_libraries(_pyflonkit ${CMAKE_CURRENT_SOURCE_DIR}/go-uuoskit/${BUILD_TARGET})

add_custom_command(OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/go-uuoskit/${BUILD_TARGET}
    COMMAND ${BUILD_LIB_CMD}
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/go-uuoskit/lib.go
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/go-uuoskit/main.go
    COMMENT "Creating ${BUILD_TARGET}"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/go-uuoskit
)

add_custom_target(build_pyflonkit ALL
    COMMAND echo "Building ${BUILD_TARGET}"
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/go-uuoskit/${BUILD_TARGET}
    # to make quotes printable,for example
    VERBATIM
)

install(TARGETS _pyflonkit LIBRARY DESTINATION pysrc)
