#ifndef PYTHON_H
#define PYTHON_H

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

#endif
