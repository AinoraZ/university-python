#include <Python.h>
#include "structmember.h"

typedef struct
{
    PyObject_HEAD int numerator;
    int denominator;
} RationalNumber;

static void RationalNumber_dealloc(RationalNumber *self)
{
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *RationalNumber_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    RationalNumber *self;

    self = (RationalNumber *)type->tp_alloc(type, 0);
    if (self != NULL)
    {
        self->numerator = 0;
        self->denominator = 0;
    }

    return (PyObject *)self;
}

static int RationalNumber_init(RationalNumber *self, PyObject *args, PyObject *kwds)
{
    if (!PyArg_ParseTuple(args, "ii", &self->numerator, &self->denominator))
        return -1;
    return 0;
}

static PyMemberDef RationalNumber_members[] = {
    {"numerator", T_INT, offsetof(RationalNumber, numerator), 0, "numerator of fraction"},
    {"denominator", T_INT, offsetof(RationalNumber, denominator), 0, "denominator of fraction"},
    {NULL} /* Sentinel */
};

static PyObject *RationalNumber_add(RationalNumber *self, PyObject *args)
{
    RationalNumber *bNumber;

    if (!PyArg_ParseTuple(args, "O", &bNumber))
    {
        return NULL;
    }

    if (self->denominator != bNumber->denominator)
    {
        int tempDenom = self->denominator;
        self->numerator *= bNumber->denominator;
        self->denominator *= bNumber->denominator;

        bNumber->numerator *= tempDenom;
        bNumber->denominator *= tempDenom;
    }

    self->numerator += bNumber->numerator;

    return Py_BuildValue("O", (PyObject *)self);
}

static PyMethodDef RationalNumber_methods[] = {
    {"add", (PyCFunction)RationalNumber_add, METH_VARARGS, "Adds given rational number to self"},
    {NULL} /* Sentinel */
};

static PyObject *RationalNumber_str(RationalNumber *self)
{
    return PyUnicode_FromFormat("(%i %i)", self->numerator, self->denominator);
}

static PyTypeObject num_RationalNumberType = {
    PyVarObject_HEAD_INIT(NULL, 0) "num.RationalNumber",   /*tp_name*/
    sizeof(RationalNumber),                                /*tp_basicsize*/
    0,                                                     /*tp_itemsize*/
    (destructor)RationalNumber_dealloc,                    /*tp_dealloc*/
    0,                                                     /*tp_print*/
    0,                                                     /*tp_getattr*/
    0,                                                     /*tp_setattr*/
    0,                                                     /*tp_reserved*/
    0,                                                     /*tp_repr*/
    0,                                                     /*tp_as_number*/
    0,                                                     /*tp_as_sequence*/
    0,                                                     /*tp_as_mapping*/
    0,                                                     /*tp_hash */
    0,                                                     /*tp_call*/
    (reprfunc)RationalNumber_str,                          /*tp_str*/
    0,                                                     /*tp_getattro*/
    0,                                                     /*tp_setattro*/
    0,                                                     /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,              /*tp_flags*/
    "Class for calculating rational numbers",                /* tp_doc */
    0,
    0,
    0,
    0,
    0,
    0,
    RationalNumber_methods, //cia bus metodai
    RationalNumber_members,
    0,
    0,
    0,
    0,
    0,
    0,
    (initproc)RationalNumber_init,
    0,
    RationalNumber_new,
};

static struct PyModuleDef nummodule = {
    PyModuleDef_HEAD_INIT,
    "rationalNumber",      // name of module
    "Module for calculating rational numbers", // module documentation, may be NULL
    -1,                    // size of per- interpreter state of the module, or -1 if the module keeps state in global variables.
    NULL, NULL, NULL, NULL, NULL};

PyMODINIT_FUNC PyInit_rationalNumber(void)
{
    PyObject *m;
    if (PyType_Ready(&num_RationalNumberType) < 0)
        return NULL;
    m = PyModule_Create(&nummodule);
    if (m == NULL)
        return NULL;
    Py_INCREF(&num_RationalNumberType);
    PyModule_AddObject(m, "RationalNumber", (PyObject *)&num_RationalNumberType);
    return m;
}