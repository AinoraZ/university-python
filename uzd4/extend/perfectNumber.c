#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>

int perfectNumber(int number)
{
	if (number <= 0)
		return 0;

	int sum = 0;
	for (int possibleDivisor = 1; possibleDivisor < number; possibleDivisor++)
	{
		if (number % possibleDivisor == 0)
			sum += possibleDivisor;
	}

	return number == sum;
}

static PyObject *perfectNumberError;

static PyObject *py_perfectNumber(PyObject *self, PyObject *args)
{
	int number = 0;
	if (!PyArg_ParseTuple(args, "i", &number))
	{
		PyErr_SetString(perfectNumberError, "Input must be an integer");
		return NULL;
	}

	int isPerfectNumber = perfectNumber(number);
	return Py_BuildValue("O", isPerfectNumber ? Py_True : Py_False);
}

static PyMethodDef perfectNumberModuleMethods[] = {
	{"perfectNumber", py_perfectNumber, METH_VARARGS, "Checks if given number is perfect number (sum of all its divisors excluding itself)"},
	{NULL, NULL, 0, NULL}};

static struct PyModuleDef perfectNumberModule = {
	PyModuleDef_HEAD_INIT,
	"perfectNumberModule",
	"Module that checks if given number is perfect number (sum of all its divisors excluding itself)",
	-1,
	perfectNumberModuleMethods};

PyMODINIT_FUNC PyInit_perfectNumber(void)
{
	PyObject *mod = PyModule_Create(&perfectNumberModule);
	perfectNumberError = PyErr_NewException("perfectNumberModule.error", NULL, NULL);
	Py_INCREF(perfectNumberError);
	PyModule_AddObject(mod, "error", perfectNumberError);
	return mod;
}