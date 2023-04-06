
#define PyCursesWindow_Type (*(PyTypeObject *) PyCurses_API[0])
#define PyCursesSetupTermCalled  {if (! ((int (*)(void))PyCurses_API[1]) () ) return NULL;}
#define PyCursesInitialised      {if (! ((int (*)(void))PyCurses_API[2]) () ) return NULL;}
#define PyCursesInitialisedColor {if (! ((int (*)(void))PyCurses_API[3]) () ) return NULL;}
