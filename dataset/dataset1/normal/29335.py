import subprocess
import tempfile

c_source = '''
#include <sys/types.h>
#include <sys/ptrace.h>

/* Needed for Darwin */
#ifndef PTRACE_TRACEME
#define PTRACE_TRACEME PT_TRACE_ME
#endif

int main() {
    int* cause_sigsegv = (int*) 0xcafebabe;
    ptrace(PTRACE_TRACEME, 0, 0, 0);
    *cause_sigsegv = 0xdeadbeef;
}
'''

with open('test.c', 'wt+') as test:
    test.write(c_source)

subprocess.check_call(['gcc', '-otest', 'test.c'])

subprocess.Popen(['./test']).wait()
